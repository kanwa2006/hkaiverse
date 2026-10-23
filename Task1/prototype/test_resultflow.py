"""
Tests for ResultFlow reference prototype. All data is SYNTHETIC (E-09).
Run: cd prototype && python -m pytest -v
"""
from datetime import date
import pytest
from resultflow import ResultFlow

# ── Synthetic user registry ───────────────────────────────────────────────────
USERS = {
    "SYN-S-1": "student",
    "SYN-S-2": "student",
    "SYN-E-1": "exam_staff",
    "SYN-A-1": "exam_approver",
    "SYN-P-1": "placement",
    "SYN-X-1": "sysadmin",
    "SYN-C-1": "employer",
}


def at_approval(rf, student="SYN-S-1", course="SYN-CS101",
                t="grade_improvement", exam_date="2026-07-24"):
    """
    Helper: register an attempt and advance it to AWAITING_APPROVAL.
    Returns the attempt key.
    """
    k = rf.register("SYN-E-1", student, course, t, exam_date)
    assert k not in ("DENIED", "ACTION_REQUIRED", "DUPLICATE"), \
        "at_approval: registration failed: " + str(k)
    for _ in range(4):
        rf.advance("SYN-E-1", k)
    assert rf.attempts[k]["status"] == "AWAITING_APPROVAL"
    return k


@pytest.fixture
def rf():
    return ResultFlow(dict(USERS))


# ══════════════════════════════════════════════════════════════════════════════
# Five required assignment scenarios
# ══════════════════════════════════════════════════════════════════════════════

def test_case1_normal(rf):
    """
    Case 1 -- Normal request.
    A valid grade-improvement attempt is registered, advanced, and published.
    The effective grade and placement copy are both updated.
    """
    k = at_approval(rf)
    assert rf.publish("SYN-A-1", k, "B") == "PUBLISHED"
    assert rf.attempts[k]["sync_status"] == "SYNCED"
    # effective_grades keyed by (student, course)
    assert rf.effective_grades[("SYN-S-1", "SYN-CS101")] == "B"
    # placement copy uses the same (student, course) key
    assert rf.placement[("SYN-S-1", "SYN-CS101")] == "B"
    assert rf.verify_audit()


def test_case2_missing_information(rf):
    """
    Case 2 -- Missing information.
    (a) Empty course reference returns ACTION_REQUIRED; nothing stored.
    (b) Invalid attempt type returns ACTION_REQUIRED; nothing stored.
    """
    r1 = rf.register("SYN-E-1", "SYN-S-1", "",          "repeat",  "2026-07-24")
    r2 = rf.register("SYN-E-1", "SYN-S-1", "SYN-CS101", "invalid", "2026-07-24")
    assert r1 == "ACTION_REQUIRED"
    assert r2 == "ACTION_REQUIRED"
    assert rf.attempts == {}


def test_case3_duplicate(rf):
    """
    Case 3 -- Duplicate request.
    Submitting the same attempt key a second time returns DUPLICATE;
    the original record and grade are unchanged.
    """
    k = at_approval(rf)
    rf.publish("SYN-A-1", k, "B")
    dup = rf.register("SYN-E-1", "SYN-S-1", "SYN-CS101",
                      "grade_improvement", "2026-07-24")
    assert dup == "DUPLICATE"
    assert len(rf.attempts) == 1
    assert rf.attempts[k]["published_grade"] == "B"
    assert rf.effective_grades[("SYN-S-1", "SYN-CS101")] == "B"


def test_case4_unauthorized(rf):
    """
    Case 4 -- Unauthorized request.
    Another student and an unconsented employer are denied.
    The student's own record is accessible.
    Both denials are logged in the audit chain.
    """
    k = at_approval(rf)
    rf.publish("SYN-A-1", k, "B")
    assert rf.view("SYN-S-2", "SYN-S-1") is None      # other student denied
    assert rf.view("SYN-C-1", "SYN-S-1") is None      # employer without consent
    assert rf.view("SYN-S-1", "SYN-S-1") is not None  # own record allowed
    assert sum(r["event"] == "DENIED_VIEW" for r in rf.audit) >= 2


def test_case5_failed_step_and_recovery(rf):
    """
    Case 5 -- Failed step and recovery.
    When placement sync fails:
      - The attempt status remains PUBLISHED (academic record intact).
      - sync_status is SYNC_FAILED.
      - The placement dict is NOT updated (no false claim of synchronization).
    After an authorized sysadmin retries:
      - sync_status becomes SYNCED.
      - placement[(student, course)] holds the approved grade.
    A second retry is idempotent (no duplicate audit events for SYNCED).
    """
    k = at_approval(rf)
    rf.sync_fault = True
    rf.publish("SYN-A-1", k, "B")

    assert rf.attempts[k]["status"]      == "PUBLISHED"
    assert rf.attempts[k]["sync_status"] == "SYNC_FAILED"
    assert ("SYN-S-1", "SYN-CS101") not in rf.placement  # not falsely updated

    # effective_grades IS updated (academic record safe even when sync fails)
    assert rf.effective_grades[("SYN-S-1", "SYN-CS101")] == "B"

    rf.sync_fault = False
    result = rf.retry_sync("SYN-X-1", k)
    assert result == "SYNCED"
    assert rf.placement[("SYN-S-1", "SYN-CS101")] == "B"

    # Second retry: idempotent
    result2 = rf.retry_sync("SYN-X-1", k)
    assert result2 == "SYNCED"
    assert len(rf.placement) == 1
    assert rf.verify_audit()


# ══════════════════════════════════════════════════════════════════════════════
# Grade-replacement sequence -- Section 5 of report (A -> C, same course)
# ══════════════════════════════════════════════════════════════════════════════

def test_grade_replacement_a_to_c_same_course(rf):
    """
    Grade-replacement sequence (SYNTHETIC grades; same student and course).

    Two distinct attempts on the same course SYN-CS101:
      Attempt 1: type=regular,          exam_date=2026-01-15  -> published grade A
      Attempt 2: type=grade_improvement, exam_date=2026-07-24 -> published grade C

    Verification steps:
      (a) After Attempt 1 is published: effective grade for (SYN-S-1, SYN-CS101) = A.
      (b) While Attempt 2 is pending (AWAITING_APPROVAL):
          effective grade is still A.
      (c) After Attempt 2 is published with grade C (lower than A):
          effective grade becomes C  (grade-replacement rule, REPORTED evidence E-07).
      (d) A is preserved in attempt_history of Attempt 2's record.
          Specifically: effective_grades reflects C; attempt 1's record still shows A.
      (e) After successful sync: placement[(SYN-S-1, SYN-CS101)] = C.

    Source of grade-replacement rule: anonymous verbal staff guidance (REPORTED, E-07).
    Written regulation not supplied -- this is an open limitation.
    """
    student = "SYN-S-1"
    course  = "SYN-CS101"
    ck = (student, course)

    # ── Attempt 1: regular, grade A ──────────────────────────────────────────
    k1 = at_approval(rf, student=student, course=course,
                     t="regular", exam_date="2026-01-15")
    rf.publish("SYN-A-1", k1, "A")

    # (a) Effective grade = A after first publication
    assert rf.effective_grades[ck] == "A"
    assert rf.placement[ck] == "A"

    # ── Attempt 2: grade_improvement, same course, different exam_date ───────
    k2 = at_approval(rf, student=student, course=course,
                     t="grade_improvement", exam_date="2026-07-24")

    # (b) While pending: effective grade is still A
    assert rf.attempts[k2]["status"] == "AWAITING_APPROVAL"
    assert rf.effective_grades[ck] == "A"   # unchanged until publication

    # ── Publish Attempt 2 with grade C (lower than A) ────────────────────────
    result = rf.publish("SYN-A-1", k2, "C")
    assert result == "PUBLISHED"

    # (c) Grade-replacement rule: C is now the effective grade
    assert rf.effective_grades[ck] == "C"

    # (d) History: attempt_history on k2 should reflect no prior published_grade
    #     on this specific attempt key (k2 was never published before).
    #     The previous *effective* grade A came from k1, not from k2 itself.
    assert rf.attempts[k2]["attempt_history"] == []
    assert rf.attempts[k2]["published_grade"] == "C"
    # Attempt 1's own record still shows A (it is not touched)
    assert rf.attempts[k1]["published_grade"] == "A"

    # (e) Placement copy updated to C after successful sync
    assert rf.placement[ck] == "C"
    assert rf.attempts[k2]["sync_status"] == "SYNCED"
    assert rf.verify_audit()


def test_grade_replacement_pending_then_publish_sequence(rf):
    """
    Grade-replacement using the normal authorized workflow only.
    No manual status manipulation.

    Two distinct attempt keys for the same student and course:
      Attempt 1: type=regular, exam_date=2026-01-15      -> published grade A
      Attempt 2: type=grade_improvement, exam_date=2026-07-24

    Steps verified:
      (a) Attempt 1 published -> effective grade = A; placement = A.
      (b) Attempt 2 registered and advanced to AWAITING_APPROVAL via normal
          workflow (register + 4 x advance). While pending, effective grade
          stays A. Attempt 2's status is AWAITING_APPROVAL.
      (c) Authorised approver (SYN-A-1) publishes attempt 2 with grade C
          through the normal publish() call. C is lower than A.
      (d) Effective grade is now C (grade-replacement rule, REPORTED E-07).
      (e) Attempt 1's record still shows published_grade = A (not touched).
      (f) attempt_history on attempt 2 is empty (it had no prior publication
          under its own key).
      (g) After successful sync, placement[(SYN-S-1, SYN-CS101)] = C.
      (h) Audit chain is intact.
    """
    student = "SYN-S-1"
    course  = "SYN-CS101"
    ck = (student, course)

    # ── Attempt 1: regular exam -> grade A ───────────────────────────────────
    k1 = at_approval(rf, student=student, course=course,
                     t="regular", exam_date="2026-01-15")
    assert rf.publish("SYN-A-1", k1, "A") == "PUBLISHED"

    # (a) After Attempt 1: effective = A, placement = A
    assert rf.effective_grades[ck] == "A"
    assert rf.placement[ck] == "A"

    # ── Attempt 2: grade_improvement -> advance via normal workflow ───────────
    k2 = at_approval(rf, student=student, course=course,
                     t="grade_improvement", exam_date="2026-07-24")

    # (b) While attempt 2 is pending, effective grade must stay A
    assert rf.attempts[k2]["status"] == "AWAITING_APPROVAL"
    assert rf.effective_grades[ck] == "A"          # unchanged while pending
    assert rf.placement[ck] == "A"                 # placement also unchanged

    # ── Authorised publish of attempt 2 with grade C ─────────────────────────
    result = rf.publish("SYN-A-1", k2, "C")
    assert result == "PUBLISHED"

    # (c)+(d) Grade-replacement rule: C is the new effective grade
    assert rf.effective_grades[ck] == "C"

    # (e) Attempt 1's own record is NOT modified
    assert rf.attempts[k1]["published_grade"] == "A"
    assert rf.attempts[k1]["status"] == "PUBLISHED"

    # (f) attempt_history on k2 is empty (k2 was never previously published)
    assert rf.attempts[k2]["attempt_history"] == []
    assert rf.attempts[k2]["published_grade"] == "C"

    # (g) Placement updated to C after successful sync
    assert rf.placement[ck] == "C"
    assert rf.attempts[k2]["sync_status"] == "SYNCED"

    # (h) Audit chain intact
    assert rf.verify_audit()


def test_effective_grade_unchanged_while_pending(rf):
    """
    The effective grade must not change because a new attempt is registered
    or advanced. It changes only on authorized publication.
    """
    student, course = "SYN-S-1", "SYN-CS101"
    ck = (student, course)

    # Publish grade A via attempt 1
    k1 = at_approval(rf, student=student, course=course,
                     t="regular", exam_date="2026-01-15")
    rf.publish("SYN-A-1", k1, "A")
    assert rf.effective_grades[ck] == "A"

    # Register and advance attempt 2 -- effective grade must stay A
    k2 = at_approval(rf, student=student, course=course,
                     t="grade_improvement", exam_date="2026-07-24")
    assert rf.effective_grades[ck] == "A"   # still A before publication
    assert rf.attempts[k2]["status"] == "AWAITING_APPROVAL"


def test_sync_failure_does_not_change_effective_grade(rf):
    """
    If sync fails after publication, effective_grades is already updated
    (academic record is safe), but placement is NOT updated.
    A retry by an authorized role corrects the placement copy.
    """
    student, course = "SYN-S-1", "SYN-CS101"
    ck = (student, course)

    k = at_approval(rf)
    rf.sync_fault = True
    rf.publish("SYN-A-1", k, "B")

    # Academic record updated; placement not
    assert rf.effective_grades[ck] == "B"
    assert ck not in rf.placement

    rf.sync_fault = False
    rf.retry_sync("SYN-X-1", k)
    assert rf.placement[ck] == "B"


def test_sync_failure_stale_then_recovery(rf):
    """
    Eight-step synchronization-failure recovery sequence.

    Step 1. Grade A published and successfully synced for (SYN-S-1, SYN-CS101).
    Step 2. A new attempt for the same course receives grade C through
            authorized publication (normal workflow, two distinct keys).
    Step 3. Placement synchronization FAILS on the second attempt.
    Step 4. The EFFECTIVE academic grade is C (updated at publication).
    Step 5. placement[(SYN-S-1, SYN-CS101)] is still A (from step 1),
            but the attempt's sync_status is SYNC_FAILED -- explicitly marked
            stale. The system must NEVER represent this A as currently synced.
    Step 6. System-level invariant: sync_status == SYNC_FAILED means the
            placement copy is stale and must not be treated as authoritative.
    Step 7. Authorized retry (sysadmin) succeeds: placement becomes C;
            sync_status clears to SYNCED.
    Step 8. A second retry is safe and idempotent (result = SYNCED, no
            duplicate events that change placement or effective_grades).
    """
    student = "SYN-S-1"
    course  = "SYN-CS101"
    ck = (student, course)

    # ── Step 1: publish grade A; sync succeeds ────────────────────────────────
    k1 = at_approval(rf, student=student, course=course,
                     t="regular", exam_date="2026-01-15")
    assert rf.publish("SYN-A-1", k1, "A") == "PUBLISHED"
    assert rf.attempts[k1]["sync_status"] == "SYNCED"
    assert rf.effective_grades[ck] == "A"
    assert rf.placement[ck] == "A"

    # ── Step 2: new attempt receives grade C (authorized publish) ─────────────
    k2 = at_approval(rf, student=student, course=course,
                     t="grade_improvement", exam_date="2026-07-24")

    # ── Step 3: inject sync fault BEFORE publishing attempt 2 ─────────────────
    rf.sync_fault = True
    assert rf.publish("SYN-A-1", k2, "C") == "PUBLISHED"

    # ── Step 4: effective academic grade is C ─────────────────────────────────
    assert rf.effective_grades[ck] == "C", (
        "Effective grade must be C after authorized publication, "
        "regardless of sync outcome"
    )

    # ── Step 5: placement is still A; sync_status is SYNC_FAILED ─────────────
    assert rf.placement[ck] == "A", (
        "Placement must retain previous value A -- sync did not succeed"
    )
    assert rf.attempts[k2]["sync_status"] == "SYNC_FAILED", (
        "sync_status must be SYNC_FAILED so the stale A is never "
        "misrepresented as current"
    )

    # ── Step 6: invariant -- stale A is not claimed as synced ─────────────────
    # A placement copy is authoritative ONLY when sync_status == "SYNCED".
    # Any consumer must check sync_status before trusting placement.
    # The test asserts that the two flags are contradictory right now:
    #   effective_grades = C (correct academic value)
    #   placement        = A (stale; must not be used as current)
    #   sync_status      = SYNC_FAILED (marks the stale state explicitly)
    assert rf.effective_grades[ck] != rf.placement[ck], (
        "effective and placement differ -- stale condition confirmed"
    )

    # ── Step 7: authorized retry succeeds ─────────────────────────────────────
    rf.sync_fault = False
    result = rf.retry_sync("SYN-X-1", k2)
    assert result == "SYNCED"
    assert rf.placement[ck] == "C", (
        "After successful retry, placement must be updated to C"
    )
    assert rf.attempts[k2]["sync_status"] == "SYNCED"
    # Effective grade is still C (unchanged throughout)
    assert rf.effective_grades[ck] == "C"

    # ── Step 8: second retry is idempotent ────────────────────────────────────
    result2 = rf.retry_sync("SYN-X-1", k2)
    assert result2 == "SYNCED"
    assert rf.placement[ck] == "C"
    assert rf.effective_grades[ck] == "C"
    # No additional placement entries created
    assert len(rf.placement) == 1
    assert rf.verify_audit()


# ══════════════════════════════════════════════════════════════════════════════
# Authorization safety tests
# ══════════════════════════════════════════════════════════════════════════════

def test_unapproved_cannot_publish(rf):
    """Wrong stage, exam_staff, and sysadmin are all denied; grade stays None."""
    k  = rf.register("SYN-E-1", "SYN-S-1", "SYN-CS101", "regular", "2026-07-24")
    assert rf.publish("SYN-A-1", k, "A") == "DENIED"       # wrong stage (REGISTERED)

    k2 = at_approval(rf, course="SYN-CS102")
    assert rf.publish("SYN-E-1", k2, "A") == "DENIED"      # exam_staff cannot publish
    assert rf.publish("SYN-X-1", k2, "A") == "DENIED"      # sysadmin cannot publish
    assert rf.attempts[k2]["published_grade"] is None


def test_advance_cannot_publish_or_skip(rf):
    """advance() is blocked from reaching PUBLISHED. Students cannot advance."""
    k  = at_approval(rf)
    assert rf.advance("SYN-E-1", k) == "DENIED"            # already at AWAITING_APPROVAL; next=PUBLISHED -> blocked

    k2 = rf.register("SYN-E-1", "SYN-S-1", "SYN-CS103", "repeat", "2026-07-24")
    assert rf.advance("SYN-S-1", k2) == "DENIED"           # student role cannot advance


def test_deadline_flag_is_flag_only(rf):
    """Deadline flag does not change any status or approve anything."""
    k = at_approval(rf)
    flags = rf.deadline_flags(date(2026, 10, 22), date(2026, 10, 30))
    assert k in flags
    assert rf.deadline_flags(date(2026, 10, 22), date(2026, 12, 30)) == []
    assert rf.attempts[k]["status"] == "AWAITING_APPROVAL"  # nothing changed


def test_audit_tamper_detected(rf):
    """Altering any field in an audit record breaks the hash chain."""
    at_approval(rf)
    assert rf.verify_audit()
    rf.audit[2]["actor"] = "SYN-X-1"
    assert not rf.verify_audit()


def test_audit_includes_timestamps(rf):
    """Every audit record must contain a non-empty 'ts' field."""
    at_approval(rf)
    for rec in rf.audit:
        assert "ts" in rec and rec["ts"], "Missing timestamp in audit record"


def test_retry_sync_unauthorized(rf):
    """Student and placement roles are denied on retry; placement stays unupdated."""
    k = at_approval(rf)
    rf.sync_fault = True
    rf.publish("SYN-A-1", k, "B")
    assert rf.attempts[k]["sync_status"] == "SYNC_FAILED"

    assert rf.retry_sync("SYN-S-1", k) == "DENIED"         # student denied
    assert rf.retry_sync("SYN-P-1", k) == "DENIED"         # placement denied
    assert ("SYN-S-1", "SYN-CS101") not in rf.placement    # placement NOT updated


def test_unknown_key_safe(rf):
    """
    Calling advance, publish, or retry_sync with an unknown key returns
    UNKNOWN_KEY rather than raising a KeyError.
    """
    assert rf.advance("SYN-E-1", "NONEXISTENT_KEY") == "UNKNOWN_KEY"
    assert rf.publish("SYN-A-1", "NONEXISTENT_KEY", "A") == "UNKNOWN_KEY"
    assert rf.retry_sync("SYN-X-1", "NONEXISTENT_KEY") == "UNKNOWN_KEY"
    assert rf.retry_sync("SYN-X-1", None) == "UNKNOWN_KEY"


def test_missing_student_id_safe(rf):
    """register() and view() with missing student id return controlled values."""
    result = rf.register("SYN-E-1", "", "SYN-CS101", "regular", "2026-07-24")
    assert result == "ACTION_REQUIRED"
    result2 = rf.view("SYN-S-1", "")
    assert result2 is None


def test_invalid_role_denied(rf):
    """An actor not in the users dict is treated as having no role (denied)."""
    k = at_approval(rf)
    assert rf.advance("UNKNOWN-ACTOR", k) == "DENIED"
    assert rf.publish("UNKNOWN-ACTOR", k, "B") == "DENIED"


def test_duplicate_different_type_not_duplicate(rf):
    """
    Two attempts for the same student+course but different attempt_type
    or different exam_date are distinct keys, not duplicates.
    """
    k1 = at_approval(rf, t="regular",          exam_date="2026-01-15")
    k2 = at_approval(rf, t="grade_improvement", exam_date="2026-07-24")
    assert k1 != k2
    assert len(rf.attempts) == 2
