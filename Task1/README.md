# ResultFlow — Academic Result Transparency & Placement Readiness

> **Student-proposed workflow improvement and reference prototype — HKAIVERSE Round 2, Task 1.**
> Not an officially deployed IFHE system. Not an official policy revision. Not connected to any college database or live data.

---

**PROBLEM** — A pending grade-improvement result creates uncertainty about which grade is currently effective and how a pending Summer Term subject is represented in placement processing. One documented case recorded **90 elapsed days** between the Summer Term exam (24 Jul 2026) and the evidence cutoff (22 Oct 2026) with no published result. A placement-form screenshot (`evidence/Screenshort_Evidence.png`) observed around Aug 2026 shows the instruction: *"SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS"* until results are released.

**SOLUTION** — ResultFlow proposes transparent result-status tracking, approver-only grade publication, a separate latest-published-grade record per student and course (updated only on authorized publication), placement-record synchronization with explicit failure handling, and a deadline-based final-year review flag.

**VALIDATION** — **20 automated tests pass** (Python 3.12.10, pytest-9.1.1). Five required synthetic scenarios are covered. Additional tests verify grade-replacement via the normal authorized workflow, 8-step sync-failure stale-then-recovery, effective-grade boundary conditions, input safety, timestamp integrity, and audit-tamper detection.

**STATUS AND LIMITATIONS** — One documented case; internal handoffs not directly observed; Summer Term eligibility verbally confirmed by officials (written source not yet committed); grade-replacement rule from verbal staff guidance only; ROI figures are illustrative assumptions; prototype is in-memory only.

---

## Current-State Process (Student-Visible, Evidence-Limited)

> This is a **student-visible, evidence-limited view** of the process — not a verified map of IFHE’s internal workflow. Internal processing stages, responsible owners, handoffs, approvals, and post-publication placement updates were not directly observed.

1. **Exam completed** — Summer Term grade-improvement examination ended 24 July 2026 (OBSERVED, one documented case).
2. **Waiting period begins** — In the documented case, no result-status information was received and no confirmed publication date was provided in response to follow-up enquiries to academic contacts (OBSERVED, E-02, E-04).
3. **Placement form observed** — A placement-form screenshot (approx. Aug 2026, E-03) shows the instruction: *“SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS”* until results are released. A student with a passing grade may therefore appear to have an open backlog during the wait.
4. **Internal processing — not observed** — What happens between exam completion and result publication (who processes results, who approves them, how many stages exist) is not known from the evidence available. These steps are labelled ASSUMPTION throughout the report.
5. **Result publication — not yet occurred** as of 22 October 2026 in the documented case (90 elapsed days, OBSERVED).

For the proposed ResultFlow workflow design, see [§6 below](#6-proposed-resultflow-workflow). Full evidence log: [§4 Evidence and Findings](#4-evidence-and-findings).

---

## Table of Contents

1. [Quick Summary](#1-quick-summary)
2. [The Problem](#2-the-problem)
3. [Who Is Affected](#3-who-is-affected)
4. [Evidence and Findings](#4-evidence-and-findings)
5. [Proposed Solution](#5-proposed-solution)
6. [Proposed ResultFlow Workflow](#6-proposed-resultflow-workflow)
7. [Grade-Improvement Rule](#7-grade-improvement-rule)
8. [Prototype and Architecture](#8-prototype-and-architecture)
9. [Synthetic Test Results](#9-synthetic-test-results)
10. [ROI and Time Savings](#10-roi-and-time-savings)
11. [How to Run](#11-how-to-run)
12. [Repository Structure](#12-repository-structure)
13. [Limitations and Risks](#13-limitations-and-risks)
14. [Interview Talking Points](#14-interview-talking-points)
15. [Final Summary](#15-final-summary)

---

## 1. Quick Summary

| Item | Detail |
|---|---|
| Process studied | Summer Term (grade-improvement) result processing through to placement eligibility check |
| Core observation | 90 elapsed days between exam (24 Jul 2026) and evidence cutoff (22 Oct 2026) with no published result — one documented case |
| Placement-form observation | `evidence/Screenshort_Evidence.png` (OBSERVED, approx. Aug 2026): *"SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS"* — file present, 56 KB, no private data |
| Grade-replacement rule | Verbally confirmed by an academic staff member (REPORTED, E-07): the newly published grade becomes effective even if lower than the previous grade |
| What ResultFlow proposes | Traceable status record, approver-only publication, separate effective-grade record per student+course, deadline flag, idempotent sync, hash-chained audit log |
| Tests | 20 pass — 5 required scenarios + grade-replacement (normal workflow) + sync-failure stale-then-recovery (8-step) + effective-grade boundaries + input safety + timestamp + audit-tamper |
| ROI | −0.5 / +7.0 / +27.0 h/month (conservative / base / optimistic); **all inputs assumed** |
| Key limitations | One documented case; internal stages not observed; eligibility source document not committed; grade-replacement rule from verbal guidance only; no written regulation reviewed |

Full detailed report: [TASK1_REPORT.md](TASK1_REPORT.md)

---

## 2. The Problem

Two observations form the evidence base:

**Observation 1 — No result status (OBSERVED, E-01, E-02, E-05):**
Examinations ended 24 July 2026. As of 22 October 2026 — **90 elapsed days** later — no result had been published and no confirmed publication date had been provided in response to enquiries. This is one documented case; it is not presented as institution-wide data.

**Observation 2 — Placement-form backlog label (OBSERVED, E-03):**
A placement-form screenshot (`evidence/Screenshort_Evidence.png`, approx. Aug 2026, 56 KB, no private data) shows the instruction: *"SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS."* A student who chose grade improvement — who already holds a passing grade — may appear to have an open backlog during the waiting period.

> The form is the 2027 Passing Out Batch Online Placement Application Form (last date: 3 Aug 2026). Whether the form's treatment of pending Summer Term subjects is intentional institutional design or an area that could benefit from clearer labeling is not determined by this project. ResultFlow proposes that clearer status labeling would reduce ambiguity for students and placement reviewers.

Everything beyond these two observations is either reported by peers or staff (REPORTED), calculated from dated observations (COMPUTED), or is a design assumption (ASSUMPTION) — and is labelled accordingly throughout this project.

**The gap in brief:** In this documented case, students lacked any confirmed result-publication date, while the placement-form wording creates uncertainty about backlog status during the waiting period. This is one case — it does not establish institution-wide frequency or prove that the college’s internal system is defective. ResultFlow proposes addressing the opacity through visible status tracking, authorized grade publication, a clear effective-grade record, deadline-based review, and safe recovery from synchronization failures.

**Problem → Evidence → Impact → Proposed Solution:**

| Concern | Evidence | Potential Impact | Proposed Response |
|---|---|---|---|
| No visible result status or ETA | OBSERVED — 90 days, one case (E-01, E-02, E-05) | No way to distinguish processing-in-progress from stalled | Centralized status record; one-stage-at-a-time progression; latest-update timestamp |
| Placement form labels pending subject as backlog | OBSERVED — screenshot E-03 (file present) | Student with passing grade may appear to have an open backlog during wait | Distinguish pending-improvement state from current effective published grade |
| Uncertainty about which grade becomes effective | REPORTED — verbal staff guidance (E-07) | Student or placement team may assume an incorrect effective grade | Separate effective-grade record updated only after authorized publication; attempt history preserved |
| Manual follow-up with no known escalation path | REPORTED — peer conversations (E-06); documented follow-ups (E-04) | Time cost; no guaranteed resolution | Self-service status view; notification on state change; escalation to accountable owner |
| Placement deadline approaching while result pending | ASSUMPTION | Potential difficulty if grade needed before publication | Informational deadline flag only — does not change grades, status, or eligibility |
| Internal handoffs and owner not externally visible | ASSUMPTION (not observed) | Accountability gap in processing | Proposed accountable role at each stage; institution must confirm actual ownership |
| Placement copy may not reflect a newly published grade | ASSUMPTION (proposed concern, not an observed system defect) | Risk of stale data in placement checks | Authorized sync after publication; SYNC_FAILED prevents false success claim; authorized retry |

---

## 3. Who Is Affected

- **Students in Summer Term grade-improvement:** Students who wish to improve their grades and have an existing grade of **E, D, F, C, or B** in the relevant subject. *(Source: verbally confirmed by officials — REPORTED, E-11. Written eligibility document not yet committed — see §4 of [TASK1_REPORT.md](TASK1_REPORT.md).)*
- **Placement team:** Staff who check academic details for placement-eligibility decisions.
- **Exam and academic staff:** Those who process and authorize grade-improvement results.

**Scale:** One directly documented case. General frequency, volume, and institutional scope require an anonymized, authorized count that was not obtained.

---

## 4. Evidence and Findings

| ID | Date | Category | Statement | Notes |
|---|---|---|---|---|
| E-01 | 24 Jul 2026 | OBSERVED | Summer Term examinations ended (one documented case) | Single case; not a sample |
| E-02 | 22 Oct 2026 | OBSERVED | No result and no confirmed publication date as of this date | Does not represent an average or institution-wide position |
| E-03 | Approx. Aug 2026 | OBSERVED | Placement-form screenshot: *"SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS"* — `evidence/Screenshort_Evidence.png`, 56 KB, present, no private data | Exact date not recorded; shows form wording, not internal system data |
| E-04 | Approx. Sep–Oct 2026 | OBSERVED | Academic contacts asked for update; no confirmed publication date given | No names or messages recorded; date approximate |
| E-05 | 22 Oct 2026 | COMPUTED | 24 Jul → 22 Oct = 7 + 31 + 30 + 22 = **90 days** elapsed | One case; not an average |
| E-06 | Approx. Oct 2026 | REPORTED | Peers described similar waiting experiences with no visible status | Secondhand; small number; not independently verified |
| E-07 | Approx. Oct 2026 | REPORTED | Anonymous academic staff member stated verbally: newly published grade becomes effective even if lower | Verbal only; no written regulation reviewed — significant limitation |
| E-08 | Approx. Oct 2026 | REPORTED | A lecturer mentioned all branches release results simultaneously | Single verbal statement; not independently verified as official policy |
| E-09 | 22 Oct 2026 | SYNTHETIC | All prototype test identifiers, grades, and dates (SYN-S-1, SYN-CS101, etc.) | Artificial data for testing only; not real |
| E-10 | 22 Oct 2026 | ASSUMPTION | Monthly case volumes and handling times in the ROI calculation | Unmeasured; required for scenario arithmetic only |
| E-11 | Approx. Oct 2026 | REPORTED | Officials verbally confirmed Summer Term grade-improvement eligibility: existing grade of E, D, F, C, or B | Verbal only; written eligibility document not committed — action required |

No official IFHE or ICFAI web pages, regulations, or notices are cited as evidence for any process claim.

**Evidence completion checklist — actions you still need to confirm:**
- [ ] **E-03:** Confirm the exact date the screenshot was taken or accessed. Update the date field above.
- [ ] **E-11 / §4 of report:** Locate the written eligibility source. Add its title, section, URL (if available), and access date.
- [ ] **E-04, E-06, E-07, E-08:** Confirm approximate months if recalled.
- [ ] **§16 of report:** Confirm exact AI model name and version used.

---

## 5. Proposed Solution

ResultFlow proposes replacing the opaque waiting period with a traceable, role-gated process:

- **Status tracking:** One record per attempt moves through defined stages: `REGISTERED → EXAM_COMPLETED → RESULT_PROCESSING → UNDER_VERIFICATION → AWAITING_APPROVAL → PUBLISHED`.
- **Approver-only publication:** Only `exam_approver` can publish a grade. Exam staff, sysadmin, students, and unrecognized actors are all denied (tested in `test_unapproved_cannot_publish`, `test_invalid_role_denied`).
- **Separate effective-grade record:** `effective_grades[(student, course)]` is updated only on authorized publication, regardless of whether the new grade is higher or lower. A pending attempt never changes this record.
- **Grade history:** When the *same attempt key* is published a second time, the previous published grade on that record is archived in `attempt_history` — never deleted. When two separate attempts exist for the same course (different keys), the earlier attempt's own record retains its `published_grade` and is preserved in the audit log.
- **Deadline flag:** Cases approaching a placement deadline are flagged for review. The flag does not approve grades, change status, or grant eligibility (tested in `test_deadline_flag_is_flag_only`).
- **Sync with fallback:** After publication, the approved grade is copied to `placement[(student, course)]`. If sync fails, `SYNC_FAILED` is recorded on the attempt record and `effective_grades` is already updated (academic record safe), while `placement` is left unchanged — retaining its prior value — and is not falsely claimed as current. An authorized role retries safely (tested in `test_sync_failure_stale_then_recovery`).
- **Audit log:** Every action is appended to a hash-chained log with real generated UTC timestamps. Tampering breaks the hash chain (tested in `test_audit_tamper_detected`).
- **Input safety:** Unknown attempt keys return `UNKNOWN_KEY`; missing fields return `ACTION_REQUIRED` or `None` — no unhandled exceptions (tested).

---

## 6. Proposed ResultFlow Workflow

> **This diagram describes the proposed ResultFlow design — not a verified description of the existing IFHE process.** All roles, stage names, and internal handoffs shown here are proposed and require institutional confirmation before any live implementation.

```
REGISTERED
    |
    v
EXAM_COMPLETED
    |
    v
RESULT_PROCESSING
    |
    v
UNDER_VERIFICATION
    |
    v
AWAITING_APPROVAL
    |
    +--(exam_approver only)--> PUBLISHED
                                    |
                               effective_grades[(student, course)] updated
                                    |
                               _sync() runs
                                    |
                          +---------+---------+
                          |                   |
                        SYNCED           SYNC_FAILED
                                             |
                                    (sysadmin or exam_approver)
                                        retry_sync()
                                             |
                                           SYNCED

Exceptions handled at any stage:
  ACTION_REQUIRED  -- missing or invalid input; nothing stored
  DUPLICATE        -- same attempt key already registered; ignored and logged
  DENIED           -- unauthorized action; no state changes; event logged
  UNKNOWN_KEY      -- invalid attempt key reference; controlled return; no crash
```

> All proposed roles and stage owners require institutional confirmation before any live implementation.

---

## 7. Grade-Improvement Rule

**Rule (REPORTED — verbal staff guidance, E-07; written regulation not reviewed):**

> When a new grade-improvement result is officially approved and published, that newly published grade becomes the effective grade for the student and course, even if it is lower than the previous published grade.

**Two-key design:** Attempts are keyed by `student|course|type|exam_date`. The effective grade is keyed by `(student, course)`. These are separate stores — a pending second attempt never overwrites the first.

| Step | `effective_grades[(SYN-S-1, SYN-CS101)]` | `placement[(SYN-S-1, SYN-CS101)]` |
|---|---|---|
| Attempt 1 (regular, Jan) published — grade A | A | A |
| Attempt 2 (grade_improvement, Jul) pending at AWAITING_APPROVAL | **A — unchanged** | A |
| Attempt 2 published — grade C (lower than A) | **C** | C (after successful sync) |

- Attempt 1's own record retains `published_grade = A` — not touched.
- `attempt_history` on Attempt 2 is empty (it was not previously published under its own key).
- Source of rule: verbal guidance (REPORTED, E-07). Written regulation is an open evidence gap.
- Tests: `test_grade_replacement_a_to_c_same_course` **PASSED** · `test_grade_replacement_pending_then_publish_sequence` **PASSED**

---

## 8. Prototype and Architecture

**File:** [`prototype/resultflow.py`](prototype/resultflow.py) — single file, standard library only, no external dependencies.

**Three storage dictionaries:**

| Dict | Key | Holds |
|---|---|---|
| `attempts` | `"student\|course\|type\|exam_date"` | Full attempt record (status, published_grade, attempt_history, sync_status) |
| `effective_grades` | `(student, course)` | Most recently authorized published grade |
| `placement` | `(student, course)` | Synced copy for placement system |

**Design principles:**
- Deterministic rules only. No AI in any decision.
- Least-privilege: each role is limited to exactly what is documented and tested.
- Fail-safe: `SYNC_FAILED` never falsely claims placement was updated.
- Idempotent: repeating a valid operation produces the same result without side effects.
- Safe inputs: `_require_key()` guards all key lookups; controlled returns instead of exceptions.
- Audit: hash-chained, append-only, with real generated UTC timestamps included in each hash.

**What the prototype is NOT:**
- Not connected to any IFHE system or database.
- Not persistent (in-memory only; state lost on restart).
- Not a production-grade durable audit store.
- Not an implementation of CGPA recalculation (policy-dependent; official rules not confirmed).

---

## 9. Synthetic Test Results

**Run:** 23 Oct 2026 · Python 3.12.10 · pytest-9.1.1
**Result: 20 passed, 0 failed**
**Saved output:** [`evidence/pytest_output.txt`](evidence/pytest_output.txt)

### Five Required Scenarios

| # | Test | Scenario | Result |
|---|---|---|---|
| 1 | `test_case1_normal` | Valid request registered, advanced, and published; effective grade and placement synced | **PASSED** |
| 2 | `test_case2_missing_information` | Empty course / invalid attempt type; nothing stored | **PASSED** |
| 3 | `test_case3_duplicate` | Same attempt key submitted twice; original record unchanged | **PASSED** |
| 4 | `test_case4_unauthorized` | Other student and unconsented employer denied; own record accessible | **PASSED** |
| 5 | `test_case5_failed_step_and_recovery` | Sync fails; effective grade kept; sysadmin retry succeeds; idempotent | **PASSED** |

### Additional Tests

| Test | What it verifies | Result |
|---|---|---|
| `test_grade_replacement_a_to_c_same_course` | Two distinct attempts on same course; A then C; effective = C; attempt 1 record still shows A | **PASSED** |
| `test_grade_replacement_pending_then_publish_sequence` | Normal workflow only — no manual status reset; A pending → C authorized → C effective; all 8 sub-checks | **PASSED** |
| `test_sync_failure_stale_then_recovery` | 8-step: A synced → C published → sync fails → stale A marked SYNC_FAILED → retry → C synced → idempotent | **PASSED** |
| `test_effective_grade_unchanged_while_pending` | Effective grade stays A while attempt 2 is at AWAITING_APPROVAL | **PASSED** |
| `test_sync_failure_does_not_change_effective_grade` | Sync failure: effective_grades correct; placement not updated; retry fixes placement | **PASSED** |
| `test_unapproved_cannot_publish` | Wrong stage, exam_staff, sysadmin all denied | **PASSED** |
| `test_advance_cannot_publish_or_skip` | `advance()` cannot reach PUBLISHED; student role cannot advance | **PASSED** |
| `test_deadline_flag_is_flag_only` | Deadline flag returned; no status changed | **PASSED** |
| `test_audit_tamper_detected` | Modified audit record field breaks hash chain | **PASSED** |
| `test_audit_includes_timestamps` | Every audit record contains a non-empty `ts` field | **PASSED** |
| `test_retry_sync_unauthorized` | Student and placement roles denied on retry | **PASSED** |
| `test_unknown_key_safe` | Unknown and None keys return UNKNOWN_KEY; no exception raised | **PASSED** |
| `test_missing_student_id_safe` | Empty student ID returns ACTION_REQUIRED or None safely | **PASSED** |
| `test_invalid_role_denied` | Unrecognized actor is denied without exception | **PASSED** |
| `test_duplicate_different_type_not_duplicate` | Same course, different type/date = distinct keys, not duplicates | **PASSED** |

Five-case demonstration output: [`evidence/case_results.md`](evidence/case_results.md)

---

## 10. ROI and Time Savings

> **All inputs are illustrative assumptions (E-10).** No real handling times or case volumes were measured.
>
> Overhead (180 min/month) covers: monthly review, staff support queries, exception handling, SYNC_FAILED reconciliation, and system administration.

| Scenario | Cases/mo | Current min/case | Proposed min/case | Net saving/case | Overhead min/mo | Gross min saved | Net min saved | Net h/mo | Break-even |
|---|---|---|---|---|---|---|---|---|---|
| Conservative | 50 | 8 | 5 | 3 | 180 | 150 | −30 | **−0.5** | 60 cases/mo |
| **Base** | **100** | **10** | **4** | **6** | **180** | **600** | **420** | **+7.0** | **30 cases/mo** |
| Optimistic | 200 | 12 | 3 | 9 | 180 | 1,800 | 1,620 | **+27.0** | 20 cases/mo |

**Worked check (base):** 100 × (10 − 4) = 600 min gross; 600 − 180 = 420 min = **7.0 h**. Break-even = 180 ÷ 6 = **30 cases/mo**. ✓

At low volume (conservative), overhead exceeds the saving — net is negative. Real-world savings cannot be claimed until actual case volumes and handling times are measured with institutional permission.

Full table: [`evidence/roi_results.md`](evidence/roi_results.md) · Script: [`prototype/roi_calc.py`](prototype/roi_calc.py)

---

## 11. How to Run

Requirements: Python 3 (tested on 3.12.10) and pytest. No other dependencies.

```bash
cd prototype

# Run all 20 tests
python -m pytest -v

# Run the five-case demonstration (writes ../evidence/case_results.md)
python run_cases.py

# Run the ROI calculation (writes ../evidence/roi_results.md)
python roi_calc.py
```

Saved outputs in `evidence/` are from a real run on 23 Oct 2026.

---

## 12. Repository Structure

```
ResultFlow_Task1_submission/
├── .gitignore                     <- Excludes __pycache__, .pytest_cache, OS files
├── README.md                      <- This file — fast entry point for interviewers
├── TASK1_REPORT.md                <- Full detailed report (17 sections)
├── prototype/
│   ├── resultflow.py              <- Rules engine (stdlib only; no AI in decisions)
│   ├── test_resultflow.py         <- 20 automated tests (pytest)
│   ├── run_cases.py               <- Five-case demonstration; writes case_results.md
│   └── roi_calc.py                <- ROI arithmetic; writes roi_results.md
└── evidence/
    ├── Screenshort_Evidence.png   <- Placement-form screenshot (OBSERVED, E-03)
    │                                  PRESENT · 56 KB · shows "SUMMER TERM SUBJECTS
    │                                  ALSO TREATED AS BACKLOGS" · no private data
    ├── pytest_output.txt          <- Real test run output, 23 Oct 2026 (20 passed)
    ├── case_results.md            <- Five-case demonstration output
    └── roi_results.md             <- ROI calculation output
```

---

## 13. Limitations and Risks

- Evidence is **one directly documented case** (90 elapsed days). Scale and general frequency are unknown.
- Internal processing stages, handoffs, and role ownership are **assumed, not observed** through a staff walkthrough.
- No written grade-replacement regulation reviewed. Rule implemented from verbal guidance only (REPORTED, E-07).
- Summer Term eligibility verbally confirmed (E, D, F, C, or B). **Written source document not yet committed** — required before final submission.
- ROI figures are illustrative. No real volumes or handling times measured.
- Prototype is in-memory only; not persistent; not production-ready; not connected to any IFHE system.
- CGPA recalculation not implemented — official rules not confirmed; documented as a policy-dependent component.
- Audit timestamps are real generated values but not cryptographically secured across process restarts.
- No claim is made that a specific IFHE system has a defect or that any placement opportunity was lost.

All problems and concerns are clearly labelled OBSERVED, REPORTED, COMPUTED, ASSUMPTION, or SYNTHETIC throughout this project.

---

## 14. Interview Talking Points

**What problem did you study?**
The gap between a Summer Term grade-improvement exam and result publication, and how the placement form represents pending Summer Term subjects while results are unpublished. Based on one documented 90-day waiting case and reported peer experiences. The exact scope of this behavior across the institution was not verified.

**What evidence do you have?**
- Two directly observed facts: exam date (24 Jul 2026) and no result after 90 days (as of 22 Oct 2026).
- A placement-form screenshot (`evidence/Screenshort_Evidence.png`, present, approx. Aug 2026) showing the wording *"SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS."*
- Peer-reported similar experiences (REPORTED, E-06).
- An academic staff member's verbal statement on grade-replacement (REPORTED, E-07).
- Verbal confirmation from officials on Summer Term eligibility criteria (REPORTED, E-11).
Each item is labelled OBSERVED, REPORTED, COMPUTED, or ASSUMPTION.

**Why did you propose this solution?**
The core issue is opacity — no visible status and no escalation path. ResultFlow adds status visibility, a clear approval boundary, a separate effective-grade record, grade history, and a sync-failure fallback. These address the opacity problem without granting unauthorized access or bypassing institutional processes.

**What does the prototype actually prove?**
That the proposed rules work correctly under 20 synthetic test scenarios. Specifically: grade replacement using two distinct attempt keys and the normal authorized workflow (no manual status reset), sync failure leaves effective grades intact and explicitly marks the stale placement copy as SYNC_FAILED, an 8-step stale-then-recovery sequence passes, unauthorized actors are denied, and unknown keys return controlled values instead of raising exceptions.

**What are the biggest limitations?**
One documented case, not a sample. Internal handoffs are assumptions. Grade-replacement rule from verbal guidance only — no written regulation reviewed. Eligibility verbally confirmed but written source not committed. ROI is hypothetical.

**Explain the effective-grade logic.**
`effective_grades` is keyed by `(student, course)` and is updated **only** when `publish()` is called by an authorized approver. A pending attempt — even one at AWAITING_APPROVAL — does not touch it. `placement` is a separate copy, updated only after a successful sync. If sync fails, `SYNC_FAILED` is recorded on the **attempt record** (not on the placement dictionary); `effective_grades` is already correct; and `placement` retains its prior value unchanged — it is not falsely claimed as current. An authorized sysadmin or approver retries via `retry_sync()`, which writes the current effective grade into `placement` and clears the failure state.

**Can you explain the grade-replacement logic?**
Two attempts for the same course have different attempt keys (different type or exam date). When the second is published, `effective_grades[(student, course)]` is overwritten with the new grade regardless of whether it is higher or lower. The first attempt's own record is not modified — it still shows its original published grade. This is tested with two real distinct attempt keys and the normal workflow, not a manual status hack.

---

## 15. Final Summary

**Problem:** A pending grade-improvement result creates uncertainty about which grade is currently effective and how the pending subject appears in placement processing. One documented case recorded 90 elapsed days between the Summer Term exam and the evidence cutoff with no published result.

**Solution:** ResultFlow proposes transparent status tracking, approver-only publication, a separate `effective_grades` record per student and course (updated only on authorized publication, even if the new grade is lower), a deadline-based review flag, and controlled sync with explicit failure handling and authorized retry.

**Evidence and validation:** One directly observed 90-day case; a placement-form screenshot (OBSERVED, present as `evidence/Screenshort_Evidence.png`); peer-reported experiences (REPORTED); verbal staff guidance on grade replacement (REPORTED). Twenty synthetic tests pass. ROI is hypothetical.

**Limitations:** Internal processing stages were not directly observed. No written grade-replacement regulation was reviewed. Summer Term eligibility verbally confirmed (E, D, F, C, or B) — written source not yet committed. Volumes and handling times are estimated assumptions. The prototype is in-memory only and is not connected to any IFHE system.

*This is a student proposal demonstrating what a structured, accountable process could look like. It uses no real student data and makes no claims about any specific IFHE system.*
