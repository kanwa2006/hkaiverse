"""ResultFlow reference rules engine -- SYNTHETIC DATA ONLY, stdlib only.
Deterministic rules; no AI is used for any decision. Not an official IFHE system.

Grade-improvement rule (verbal staff guidance, REPORTED -- written regulation not supplied):
  When a new grade-improvement result is officially approved and published,
  that newly published grade becomes the effective grade for that student and course,
  even if it is lower than the previously published grade.

Timestamp note: audit records include an ISO-8601 timestamp generated at call time
(real wall-clock UTC). Timestamps are part of the hash, so they cannot be altered
without breaking the chain within a single run. They are NOT a durable tamper-proof
time source across restarts.
"""
import hashlib, json
from datetime import datetime, timezone

STAGES = [
    "REGISTERED", "EXAM_COMPLETED", "RESULT_PROCESSING",
    "UNDER_VERIFICATION", "AWAITING_APPROVAL", "PUBLISHED",
]
ATTEMPT_TYPES = {"regular", "repeat", "grade_improvement"}
STAFF_ROLES   = {"exam_staff", "exam_approver"}
RETRY_ROLES   = {"sysadmin", "exam_approver"}


def _now_iso():
    """Return current UTC time as ISO-8601 string for audit records."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class ResultFlow:
    """
    In-memory reference implementation. State is lost on restart.
    Hash-chained audit log is tamper-evident within a single run only.

    Storage layout
    --------------
    attempts        : {attempt_key -> attempt_dict}
                      attempt_key = student|course|attempt_type|exam_date
                      Each dict holds: student, course, type, exam_date, status,
                        published_grade (grade on this attempt), attempt_history
                        (superseded grades on this same key), sync_status.

    effective_grades: {(student, course) -> grade}
                      Authoritative effective grade for that student+course pair.
                      Updated ONLY after authorized publication.

    placement       : {(student, course) -> grade}
                      Synced copy of effective_grade for the placement system.
                      Updated ONLY after a successful sync post-publication.

    audit           : append-only, SHA-256 hash-chained list of event records,
                      each including a real generated timestamp.
    """

    def __init__(self, users):
        self.users            = users           # {synthetic_id: role}
        self.attempts         = {}              # attempt_key -> attempt_dict
        self.effective_grades = {}              # (student, course) -> grade
        self.placement        = {}              # (student, course) -> grade
        self.audit            = []
        self.sync_fault       = False           # test hook: simulate placement-sync failure
        self.employer_consent = set()           # {(employer_id, student_id)}

    # ── audit helpers ─────────────────────────────────────────────────────────

    def _log(self, actor, event, ref, detail=""):
        """Append a hash-linked audit record with a real generated timestamp."""
        prev = self.audit[-1]["hash"] if self.audit else "0" * 64
        rec  = {
            "n":      len(self.audit) + 1,
            "ts":     _now_iso(),
            "actor":  actor,
            "event":  event,
            "ref":    str(ref),
            "detail": detail,
            "prev":   prev,
        }
        rec["hash"] = hashlib.sha256(
            json.dumps(rec, sort_keys=True).encode()
        ).hexdigest()
        self.audit.append(rec)

    def verify_audit(self):
        """
        Return True if every record in the chain has an intact hash link.
        The 'ts' field is included in the hash, so timestamps cannot be silently
        altered without breaking the chain within the same in-memory run.
        """
        prev = "0" * 64
        for r in self.audit:
            body = {k: v for k, v in r.items() if k != "hash"}
            computed = hashlib.sha256(
                json.dumps(body, sort_keys=True).encode()
            ).hexdigest()
            if r["prev"] != prev or computed != r["hash"]:
                return False
            prev = r["hash"]
        return True

    # ── input helpers ─────────────────────────────────────────────────────────

    def _require_key(self, key):
        """Return (attempt_dict, None) if key exists, else (None, 'UNKNOWN_KEY')."""
        if not key or key not in self.attempts:
            return None, "UNKNOWN_KEY"
        return self.attempts[key], None

    # ── registration ──────────────────────────────────────────────────────────

    def register(self, actor, student, course, attempt_type, exam_date):
        """
        Register a new attempt.
        Returns the attempt key string on success, or:
          DENIED          -- actor not authorized to register
          ACTION_REQUIRED -- a required field is missing or invalid
          DUPLICATE       -- identical key already registered
        """
        if self.users.get(actor) not in STAFF_ROLES:
            self._log(actor, "DENIED_REGISTER",
                      (student or "") + "/" + (course or ""),
                      "actor role not authorized")
            return "DENIED"

        if not student or not course or attempt_type not in ATTEMPT_TYPES or not exam_date:
            self._log(actor, "ACTION_REQUIRED",
                      (student or "") + "/" + (course or ""),
                      "missing or invalid field")
            return "ACTION_REQUIRED"

        key = "|".join([student, course, attempt_type, exam_date])
        if key in self.attempts:
            self._log(actor, "DUPLICATE_IGNORED", key)
            return "DUPLICATE"

        self.attempts[key] = {
            "student":         student,
            "course":          course,
            "type":            attempt_type,
            "exam_date":       exam_date,
            "status":          "REGISTERED",
            "published_grade": None,   # grade set on this attempt after publication
            "attempt_history": [],     # previous published_grade values on this key
            "sync_status":     None,
        }
        self._log(actor, "REGISTERED", key)
        return key

    # ── stage movement ────────────────────────────────────────────────────────

    def advance(self, actor, key):
        """
        Move an attempt one stage forward (exam_staff or exam_approver).
        The final transition to PUBLISHED is reserved for publish() alone.
        Returns the new status string, or DENIED / UNKNOWN_KEY.
        """
        a, err = self._require_key(key)
        if err:
            self._log(actor, "DENIED_ADVANCE", str(key), err)
            return err

        role = self.users.get(actor)
        nxt  = (STAGES[STAGES.index(a["status"]) + 1]
                if a["status"] != "PUBLISHED" else None)

        if nxt is None or nxt == "PUBLISHED" or role not in STAFF_ROLES:
            self._log(actor, "DENIED_ADVANCE", key,
                      "role=" + str(role) + " next=" + str(nxt))
            return "DENIED"

        a["status"] = nxt
        self._log(actor, "STATUS_" + nxt, key)
        return nxt

    # ── publication ───────────────────────────────────────────────────────────

    def publish(self, actor, key, grade):
        """
        Publish an approved grade. Only exam_approver may call this, and only
        when the attempt is at AWAITING_APPROVAL.

        Grade-replacement rule (REPORTED -- verbal staff guidance):
          The newly published grade becomes the effective_grade for the
          student+course pair, even if it is lower than the previous effective grade.
          The previous effective grade is preserved in attempt_history (never deleted).

        Sequence (order matters for consistency):
          1. Archive previous published_grade on this attempt (if any).
          2. Set published_grade on the attempt and mark status PUBLISHED.
          3. Update effective_grades[(student, course)] to the new grade.
          4. Run sync -- a failure here never undoes steps 1-3.
        Returns attempt status string, or DENIED / UNKNOWN_KEY.
        """
        a, err = self._require_key(key)
        if err:
            self._log(actor, "DENIED_PUBLISH", str(key), err)
            return err

        if (self.users.get(actor) != "exam_approver"
                or a["status"] != "AWAITING_APPROVAL"
                or not grade):
            self._log(actor, "DENIED_PUBLISH", key,
                      "role=" + str(self.users.get(actor)) + " status=" + a["status"])
            return "DENIED"

        student, course = a["student"], a["course"]
        course_key = (student, course)

        # 1. Archive any previous published_grade on this attempt
        if a["published_grade"] is not None:
            a["attempt_history"].append({
                "grade":        a["published_grade"],
                "replaced_by":  grade,
                "published_by": actor,
                "note":         "superseded by newer authorized publication",
            })

        # 2. Update the attempt record
        a["status"]         = "PUBLISHED"
        a["published_grade"] = grade

        # 3. Update the authoritative effective-grade for this student+course
        prev_effective = self.effective_grades.get(course_key)
        self.effective_grades[course_key] = grade
        self._log(actor, "PUBLISHED", key,
                  "grade=" + grade + " prev_effective=" + str(prev_effective))

        # 4. Sync to placement (failure does not undo steps 1-3)
        self._sync(actor, key)
        return a["status"]

    # ── sync ──────────────────────────────────────────────────────────────────

    def _sync(self, actor, key):
        """
        Copy the effective grade for the attempt's student+course into placement.
        Idempotent: writing the same value twice has no additional side effects.
        A failure NEVER removes or modifies effective_grades or the attempt record.
        """
        a = self.attempts[key]
        course_key = (a["student"], a["course"])
        grade = self.effective_grades.get(course_key)

        if self.sync_fault:
            a["sync_status"] = "SYNC_FAILED"
            self._log(actor, "SYNC_FAILED", key,
                      "effective grade retained in academic record; "
                      "placement NOT updated")
            return

        self.placement[course_key] = grade
        a["sync_status"] = "SYNCED"
        self._log(actor, "SYNCED", key)

    def retry_sync(self, actor, key):
        """
        Retry a failed sync. Only RETRY_ROLES (sysadmin, exam_approver) may call this.
        Returns current sync_status string, or DENIED / UNKNOWN_KEY.
        """
        a, err = self._require_key(key)
        if err:
            self._log(actor, "DENIED_RETRY_SYNC", str(key), err)
            return err

        role = self.users.get(actor)
        if role not in RETRY_ROLES:
            self._log(actor, "DENIED_RETRY_SYNC", key, "role=" + str(role))
            return "DENIED"

        if a["status"] == "PUBLISHED" and a["sync_status"] == "SYNC_FAILED":
            self._sync(actor, key)

        return a["sync_status"]

    # ── read access ───────────────────────────────────────────────────────────

    def view(self, actor, student):
        """
        Return attempt records for student if actor is authorized, else None.
        Students see only their own records.
        Employers require explicit per-student consent in employer_consent.
        attempt_history is stripped from placement and employer views.
        """
        if not student:
            self._log(actor, "DENIED_VIEW", "", "missing student id")
            return None

        role    = self.users.get(actor)
        allowed = (
            (role == "student" and actor == student)
            or role in STAFF_ROLES
            or role == "placement"
        )
        if role == "employer" and (actor, student) in self.employer_consent:
            allowed = True

        if not allowed:
            self._log(actor, "DENIED_VIEW", student)
            return None

        self._log(actor, "VIEW", student)
        sensitive = {"placement", "employer"}
        result = []
        for a in self.attempts.values():
            if a["student"] != student:
                continue
            record = {k: v for k, v in a.items() if k != "student"}
            if role in sensitive:
                record.pop("attempt_history", None)
            result.append(record)
        return result

    def get_effective_grade(self, actor, student, course):
        """
        Return the current effective grade for a student+course pair, or None.
        Access authorization follows the same rules as view().
        """
        if not student or not course:
            return None
        role    = self.users.get(actor)
        allowed = (
            (role == "student" and actor == student)
            or role in STAFF_ROLES
            or role == "placement"
        )
        if role == "employer" and (actor, student) in self.employer_consent:
            allowed = True
        if not allowed:
            self._log(actor, "DENIED_VIEW", student + "/" + course)
            return None
        return self.effective_grades.get((student, course))

    # ── deadline flag ─────────────────────────────────────────────────────────

    def deadline_flags(self, today, deadline, window_days=14):
        """
        Return attempt keys not yet PUBLISHED where the placement deadline is
        within window_days. Informational flag only.
        Does NOT approve grades, change statuses, or grant eligibility.
        """
        try:
            left = (deadline - today).days
        except (TypeError, AttributeError):
            return []
        if left < 0 or left > window_days:
            return []
        return [k for k, a in self.attempts.items() if a["status"] != "PUBLISHED"]
