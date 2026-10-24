# ResultFlow — Task 1 Detailed Report
## Academic Result Transparency & Placement Readiness

> **Status:** Student-proposed workflow and reference prototype — not an official IFHE system or policy.
> **Data:** Prototype uses **synthetic data only.** No real student names, IDs, marks, fees, credentials, or private messages are committed.
> **Prepared:** 23 Oct 2026 (IST)

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Problem — Evidence — Impact — Proposed Solution](#2-problem--evidence--impact--proposed-solution)
3. [Problem, Scope, and Affected Users](#3-problem-scope-and-affected-users)
4. [Summer Term Eligibility](#4-summer-term-eligibility)
5. [Current Workflow](#5-current-workflow)
6. [Dated Evidence Log and Permission Scope](#6-dated-evidence-log-and-permission-scope)
7. [Grade-Improvement and Placement-Status Concern](#7-grade-improvement-and-placement-status-concern)
8. [Proposed Improved Workflow](#8-proposed-improved-workflow)
9. [Grade-Improvement Rule and Effective-Grade Logic](#9-grade-improvement-rule-and-effective-grade-logic)
10. [Final-Year Deadline Review and Simultaneous-Publication Limitation](#10-final-year-deadline-review-and-simultaneous-publication-limitation)
11. [Data Protection and Authorization Boundaries](#11-data-protection-and-authorization-boundaries)
12. [Five Synthetic Cases and Actual Test Results](#12-five-synthetic-cases-and-actual-test-results)
13. [ROI Assumptions, Equations, and Results](#13-roi-assumptions-equations-and-results)
14. [Risks, Limitations, and Validation Plan](#14-risks-limitations-and-validation-plan)
15. [Requirement-to-Evidence Checklist](#15-requirement-to-evidence-checklist)
16. [Personal Contribution and AI-Use Record](#16-personal-contribution-and-ai-use-record)
17. [Final Summary](#17-final-summary)

---

## 1. Executive Summary

This project investigates the process between a Summer Term (grade-improvement) examination and the point where a result reaches the placement eligibility check. The starting point is one documented case: examinations ended 24 July 2026, and by 22 October 2026 — ninety days later — no result had been published and no confirmed update date had been given. That wait is the result-processing gap this project maps and proposes to improve.

The project delivers three things:

- A labelled map of the current process, with each stage marked as observed, reported, or assumed.
- A proposed improved process with role-based access, approver-only publication, a separate effective-grade record per student and course, idempotent placement synchronization, a deadline-aware review flag, fallback handling, and a hash-chained audit log with generated timestamps.
- A Python reference prototype with twenty automated tests covering the five required synthetic scenarios and additional safety, grade-replacement, sync-failure stale-then-recovery, and input-validation checks.

All numeric volumes, time estimates, and ROI figures are illustrative assumptions. No real student data is used. No internal system or staff record was accessed.

---

## 2. Problem — Evidence — Impact — Proposed Solution

| Potential problem | Evidence | Impact | Proposed solution |
|---|---|---|---|
| Pending result with no visible status or ETA | OBSERVED — one documented case, 90 days (E-01, E-02, E-05) | No way to tell whether processing is stalled or simply slow | Centralized status record, one-stage-at-a-time movement, latest-update timestamp |
| Placement form treats pending Summer Term subject as a backlog | OBSERVED — placement-form screenshot (E-03); file present: `evidence/Screenshort_Evidence.png` (56 KB, reviewed) | A student improving a grade may appear less competitive while waiting | Distinguish pending-improvement state from current effective published grade |
| Uncertainty about which grade becomes effective after improvement | REPORTED — verbal staff guidance (E-07) | Student or placement team may assume an incorrect effective grade | Separate effective-grade record updated only after authorized publication; attempt history preserved |
| Repeated manual follow-up with no known escalation route | REPORTED — peer conversations (E-06); one documented case (E-04) | Unnecessary time cost; no guarantee of resolution | Self-service status view, notification on state change, defined escalation to accountable owner |
| Placement deadline approaching while result still pending | ASSUMPTION | Potential eligibility-check difficulty if grade needed before result published | Deadline flag for expedited review; flag is informational only — does not change grades or status |
| Internal handoffs and owner unclear | ASSUMPTION — internal stages not directly observed | Processing accountability gap | Proposed accountable role at each stage; institution must confirm actual ownership |
| Placement copy may not reflect newly published grade | ASSUMPTION — proposed concern, not an observed system defect | Risk of stale data reaching placement checks | Authorized sync after publication; SYNC_FAILED prevents false success; manual fallback |

**Key summary of findings:**
- **What is the problem?** Pending grade-improvement results create uncertainty about the effective grade and how the subject appears on the placement form.
- **Who is affected?** Students awaiting Summer Term grade-improvement results, particularly those approaching placement deadlines.
- **What evidence supports it?** One documented 90-day case as of 22 Oct 2026 (OBSERVED) and a placement-form screenshot (OBSERVED, `evidence/Screenshort_Evidence.png`, present in repository, shows "SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS", no private data).
- **What does ResultFlow change?** Transparent status tracking, approver-only publication, a separate effective-grade record per student and course, grade history, deadline flagging, and controlled sync.
- **What has been tested?** Twenty automated tests: five required scenarios plus grade-replacement (same course, two distinct attempt keys, normal workflow only), sync-failure stale-then-recovery (8-step sequence), effective-grade boundary conditions, input safety, timestamp verification, and audit-tamper detection.

---

## 3. Problem, Scope, and Affected Users

**Core problem:** In the documented case, no result-status information was received following the Summer Term examination, and no confirmed publication date was provided in response to enquiries (OBSERVED, E-01 to E-04). Whether a student-facing status facility exists within the institution that was simply not used in this case is not known. Based on a placement-form observation (screenshot present — `evidence/Screenshort_Evidence.png`, E-03), the form treats a pending Summer Term subject as a backlog until the result is published. A student who chose grade improvement — who already has a passing grade — may appear to have an open backlog during the waiting period.

**Scope:**
- In scope: result-status tracking from registration through publication and placement-record synchronization.
- Out of scope: marking, paper checking, forcing release timelines, grading policy decisions, live college-system integration.

**Who is affected:**
- Students eligible for Summer Term grade-improvement — those with an existing grade of E, D, F, C, or B in the relevant subject (see §4 for source status).
- Placement team members who check academic details for eligibility decisions.
- Academic and exam staff who process and approve results.

**Scale:** One directly documented case (90 days, OBSERVED). General frequency requires an anonymized, authorized count that was not obtained.

---

## 4. Summer Term Eligibility

**What officials confirmed (REPORTED, E-11):** Officials verbally confirmed that the Summer Term grade-improvement option is available to students who wish to improve their grades and who have an existing grade of **E, D, F, C, or B** in the relevant subject.

**Evidence classification:** This information is classified as **REPORTED** — it was verbally confirmed by officials. It is not independently verified from a written institutional source.

**Source status:** The exact source document — title, section number, URL, and access date — is not committed to this repository. The written eligibility document was not obtained during the investigation. This is a disclosed evidence gap; the verbally confirmed eligibility criteria (E, D, F, C, or B) remain as stated and are labelled REPORTED throughout this project.

**Why this matters:** This condition defines the population relevant to the workflow. Not every student is in Summer Term; only those who meet this condition and chose grade improvement.

---

## 5. Current Workflow

> ⚠️ Internal processing stages (steps 3 and 4 below) are **NOT directly observed.** They represent a reasonable interpretation of the process based on the documented waiting experience and general academic administration practice. They are labelled ASSUMPTION.

```
[Student registers Summer Term attempt]
        |
        v
  [Exam written]  -- 24 Jul 2026 (OBSERVED, one documented case)
        |
        +-----> [Placement form: Summer Term subject shown as BACKLOG until result published]
        |         (OBSERVED from screenshot, E-03 -- `evidence/Screenshort_Evidence.png`, 56 KB, present)
        |
        v
[Result processed -- stage and owner not visible externally]  (ASSUMPTION)
        |
        v
[Approval by authorised staff -- approver identity unknown]   (ASSUMPTION)
        |
        v
  [Result published]  -- not yet occurred as of 22 Oct 2026 (OBSERVED, one case)
        |
        v
[Academic details re-checked for placement -- manual, frequency unknown]  (ASSUMPTION)
```

| Step | Category | Gap to validate |
|---|---|---|
| 1. Register for Summer Term | OBSERVED | Is grade-improvement treatment explained to students beforehand? |
| 2. Write exam | OBSERVED (24 Jul 2026, one case) | — |
| 3. Result processing | ASSUMPTION | Who owns this? Is progress trackable internally? |
| 4. Approval | ASSUMPTION | How many approvals required? Is there an escalation path? |
| 5. Publication | Not yet occurred as of 22 Oct 2026 | Notification practice unknown |
| 6. Placement re-check | Form wording OBSERVED (E-03, screenshot present); handling ASSUMED | How and when is the placement record updated? |

---

## 6. Dated Evidence Log and Permission Scope

**Evidence categories used in this report:**
- `OBSERVED` — directly seen or experienced
- `REPORTED` — shared by a peer or staff member in conversation; unverified independently
- `COMPUTED` — arithmetic on dated inputs
- `ASSUMPTION` — unverified process detail used in the workflow design
- `SYNTHETIC` — artificial data created for prototype testing only

| ID | Date (IST) | Category | Statement | Limitation |
|---|---|---|---|---|
| E-01 | 24 Jul 2026 | OBSERVED | Summer Term examinations ended (one documented case) | Single case; not a sample |
| E-02 | 22 Oct 2026 | OBSERVED | No result and no confirmed publication date received as of this date | Does not explain cause or represent an average |
| E-03 | Approx. Aug 2026 *(exact date not recorded)* | OBSERVED | Placement-form screenshot shows the instruction: "SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS". File: `evidence/Screenshort_Evidence.png` (56 KB, **present**, public-facing form instruction page, no private student names, IDs, or marks visible) | Exact date of access not recorded. Screenshot shows the form wording, not internal system data. |
| E-04 | Approx. Sep–Oct 2026 *(exact date not recorded)* | OBSERVED | Academic contacts were asked for an update; no confirmed publication date was given | No names or messages recorded |
| E-05 | 22 Oct 2026 | COMPUTED | 24 Jul to 22 Oct = 7 + 31 + 30 + 22 = **90 days** elapsed | One case; not an average |
| E-06 | Approx. Oct 2026 *(exact date not recorded)* | REPORTED | Peers described similar experiences of waiting for Summer Term results with no status update | Secondhand; small number; not independently verified |
| E-07 | Approx. Oct 2026 *(exact date not recorded)* | REPORTED | An anonymous academic staff member stated verbally that the newly published grade becomes the effective grade even if it is lower than the previous grade | Verbal only; no written regulation reviewed — this is a significant limitation |
| E-08 | Approx. Oct 2026 *(exact date not recorded)* | REPORTED | A lecturer mentioned that all branches release results at the same time | Single verbal statement; not independently verified as official policy |
| E-09 | 22 Oct 2026 | SYNTHETIC | All prototype test identifiers, grades, and dates (SYN-S-1, SYN-CS101, grades A/B/C, etc.) | Artificial data created for testing; not real |
| E-10 | 22 Oct 2026 | ASSUMPTION | Monthly case volumes and handling times used in the ROI calculation | Unmeasured; required for scenario arithmetic only |
| E-11 | Approx. Oct 2026 *(exact date not recorded)* | REPORTED | Officials verbally confirmed Summer Term eligibility: existing grade of E, D, F, C, or B in relevant subject | Verbal only; written eligibility document not obtained (disclosed limitation) |

**Permission scope:** Permission was granted to discuss how results are communicated and to hear experiences shared by peers. Permission did not extend to inspecting staff systems, student records, internal processing tools, or confidential institutional data. The current-state workflow map is based on the documented waiting experience and is labelled accordingly.

**Evidence Gaps and Limitations:**
The following limitations apply to the evidence log and are disclosed here rather than treated as unfinished editing tasks:
- **E-03 (screenshot present; date not recorded):** The genuine placement-form screenshot is included in the repository (`evidence/Screenshort_Evidence.png`, 56 KB, reviewed — shows "SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS", no private data). Its exact capture date was not recorded; the date field records "Approx. Aug 2026."
- **Approximate dates (E-04, E-06, E-07, E-08, E-11):** Some dates associated with conversations or follow-up enquiries are approximate or were not recorded at the time.
- **Verbal confirmations (E-07, E-11):** The Summer Term eligibility condition (E, D, F, C, or B) and the grade-replacement rule were reported verbally by academic officials. The written eligibility document and any written grade-replacement regulation were not obtained or included in the repository.
- **AI model version (§16):** The exact AI model version used during development was not recorded during the session.
- **Internal stages:** The internal college processing stages and handoffs between exam completion and result publication were not directly verified and remain assumptions throughout this project.

These are disclosed evidence limitations, not fabricated or silently completed evidence.

---

## 7. Grade-Improvement and Placement-Status Concern

**Placement-form behavior (OBSERVED, E-03):** The placement-form screenshot (`evidence/Screenshort_Evidence.png`) shows the instruction: *"SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS."* The form is the 2027 Passing Out Batch Online Placement Application Form for ICFAI-Tech students, last date 3rd August 2026. This means a student who chose grade improvement — who already holds a passing grade in the subject — may appear to have an open backlog during the waiting period.

**The form does not appear to distinguish between:**
1. A subject that was previously failed and is being repeated (a true backlog in the conventional sense).
2. A subject in which the student already has a passing grade and chose to attempt improvement.

**What ResultFlow proposes:** Label the state explicitly. The student's current effective grade — the most recently authorized published grade — remains unchanged until a new result is officially published. A pending improvement attempt is shown as pending, not as an unresolved failure.

**What ResultFlow does not claim:** That the placement form contains a system defect. The observed behavior may reflect the intended design. The proposal is that clearer labeling would reduce ambiguity for students and placement reviewers.

---

## 8. Proposed Improved Workflow

> This is a proposed design, not a confirmed replacement for any existing IFHE process. Every proposed role and handoff requires institutional confirmation before any implementation.

### Storage Design

The prototype maintains three separate stores:

| Store | Key | Value | Updated when |
|---|---|---|---|
| `attempts` | `student\|course\|type\|exam_date` | Full attempt record including status | On register, advance, or publish |
| `effective_grades` | `(student, course)` | Most recently authorized published grade | Only on authorized publication |
| `placement` | `(student, course)` | Synced copy for placement system | Only after successful sync post-publication |

This separation means a sync failure never corrupts the effective grade, and a pending second attempt never changes the effective grade before publication.

### Inputs

| Field | Required at |
|---|---|
| Student reference (synthetic or anonymized) | Registration |
| Course reference | Registration |
| Attempt type (`regular`, `repeat`, `grade_improvement`) | Registration |
| Exam date | Registration |
| Approved grade | Publication only |
| Approval event and timestamp | Publication (logged automatically) |
| Placement deadline | When authorized and applicable |

### Status Model

```
REGISTERED -> EXAM_COMPLETED -> RESULT_PROCESSING -> UNDER_VERIFICATION -> AWAITING_APPROVAL -> PUBLISHED
                                                                                     |
      ACTION_REQUIRED <-- missing or invalid input at registration                   |
      DUPLICATE       <-- same attempt key already registered                        |
                                                                                     +--> SYNC_FAILED (placement sync failed; effective grade unchanged)
                                                                                          SYNCED
```

### Roles

| Role | Permitted | Not permitted |
|---|---|---|
| Exam/academic owner *(institution confirms who this is)* | Owns processing accountability | — |
| Exam staff | Register attempts; advance stages one step at a time | Publish a grade |
| **Exam approver** | **Publish the approved grade (from AWAITING_APPROVAL only)** | Advance stages via `advance()` |
| Placement team | View student records; `attempt_history` hidden | Change grades |
| System admin | Retry failed syncs | Approve grades |
| Student | View own records only | View other students |
| Employer | View with explicit per-student consent only | Unrestricted access |

### Approval Boundaries

Only `exam_approver` may call `publish()`. The `advance()` method cannot reach `PUBLISHED` — this boundary is enforced in code and tested (`test_advance_cannot_publish_or_skip`). Exam staff, sysadmin, and actors with unknown roles cannot publish (`test_unapproved_cannot_publish`, `test_invalid_role_denied`). Unknown attempt keys return `UNKNOWN_KEY` rather than raising an exception (`test_unknown_key_safe`).

### Fallback Handling

| Failure mode | Response |
|---|---|
| Missing required field | `ACTION_REQUIRED`; nothing stored; staff corrects and resubmits |
| Same request submitted twice | `DUPLICATE`; original record unchanged; logged |
| Unauthorized action | `DENIED`; event logged; no state changes |
| Unknown attempt key | `UNKNOWN_KEY`; logged; no crash |
| Sync failure | `SYNC_FAILED` on attempt record; effective grade unchanged; owner alerted; retry available to authorized roles |
| Authorized owner unavailable | Existing manual process continues; no silent discard |

### Audit Log

Every register, stage change, publication, sync, denial, and duplicate is appended to the hash-chained audit log. Each record includes a real generated UTC timestamp (`ts` field, ISO-8601). The timestamp is included in the hash, so it cannot be silently altered within a single run. This is an in-memory demonstration of tamper-evidence — it is not durable persistent storage.

---

## 9. Grade-Improvement Rule and Effective-Grade Logic

**Rule as implemented in the prototype:**

> When a new grade-improvement result has been officially approved and published, that newly published grade becomes the effective grade for the student and course, even if it is lower than the previously published grade.

**Evidence basis:** REPORTED — anonymous verbal staff guidance (E-07). A written regulation has not been reviewed. This is a significant open limitation.

### How the prototype implements this

The `effective_grades` dictionary is keyed by `(student, course)`. Individual attempt records are keyed by `student|course|type|exam_date` and are stored separately in `attempts`.

When `publish()` is called:
1. If the attempt key already has a `published_grade` (same key published twice), the old value is moved to `attempt_history` on that record.
2. The attempt's `published_grade` is set to the new grade and status becomes `PUBLISHED`.
3. `effective_grades[(student, course)]` is updated to the new grade — regardless of whether it is higher or lower than the previous value.
4. `_sync()` runs. If it fails, `effective_grades` already holds the new grade; `placement` is not updated.

A pending attempt — one that has not yet reached `PUBLISHED` — never touches `effective_grades`.

### A-to-C test sequence (synthetic grades, same course)

| Step | State of `effective_grades[(SYN-S-1, SYN-CS101)]` | State of `placement` |
|---|---|---|
| Attempt 1 (regular, Jan 2026) published grade A | A | A |
| Attempt 2 (grade_improvement, Jul 2026) registered and advanced to AWAITING_APPROVAL | **A (unchanged)** | A |
| Attempt 2 published grade C (lower than A) | **C** | C (after sync) |

- Attempt 1's own record still shows `published_grade = A` — not touched.
- `attempt_history` on Attempt 2 is empty (Attempt 2 was never previously published under its own key).
- Test: `test_grade_replacement_a_to_c_same_course` — **PASSED**
- Test: `test_effective_grade_unchanged_while_pending` — **PASSED**

---

## 10. Final-Year Deadline Review and Simultaneous-Publication Limitation

**Deadline flag:** `deadline_flags(today, deadline, window_days=14)` returns attempt keys not yet `PUBLISHED` where the placement deadline is within `window_days`. This is an informational flag only.

**What the flag does NOT do:**
- Does not approve grades.
- Does not change any status.
- Does not grant placement eligibility.
- Does not bypass any mandatory verification or publication step.

Tested in `test_deadline_flag_is_flag_only`.

**Simultaneous-publication limitation (REPORTED, E-08):** A lecturer mentioned that all branches release results at the same time. If this is policy — which has not been independently verified — then a single student's result cannot be expedited in isolation. In that scenario, the deadline flag would trigger review and escalation to confirm the timeline, not a bypass of the policy. This constraint is respected in the proposed design.

---

## 11. Data Protection and Authorization Boundaries

- Students may view only their own records — enforced by role and identity check in `view()`.
- `attempt_history` is stripped from records returned to placement and employer roles (minimal disclosure).
- Employers require explicit consent registered in `employer_consent` before any record is returned.
- `get_effective_grade()` follows the same authorization rules as `view()`.
- No real student names, IDs, marks, fees, credentials, or private messages are committed to this repository.
- All prototype data is synthetic and labelled (E-09).
- The screenshot file (`evidence/Screenshort_Evidence.png`) is **present** in the repository (56 KB, reviewed, public-facing form instruction, no private student information). Shows the wording: "SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS."

---

## 12. Five Synthetic Cases and Actual Test Results

> All student IDs, course codes, and grades are **SYNTHETIC** (E-09).
> Run: Python 3.12.10, pytest-9.1.1, **20 passed**, 23 Oct 2026.
> Commands: `cd prototype && python -m pytest -v && python run_cases.py && python roi_calc.py`
> Output files: [`evidence/pytest_output.txt`](evidence/pytest_output.txt) | [`evidence/case_results.md`](evidence/case_results.md)

### Case 1 — Normal Request

| Field | Detail |
|---|---|
| Scenario | Valid grade-improvement attempt registered, advanced through all five stages, published by approver |
| Inputs | SYN-S-1, SYN-CS101, grade_improvement, 2026-07-24, grade B |
| Expected | `PUBLISHED`; `effective_grades[(SYN-S-1, SYN-CS101)] = B`; `placement[(SYN-S-1, SYN-CS101)] = B`; audit valid |
| Actual | `status=PUBLISHED, sync_status=SYNCED, effective_grade=B, placement=B` |
| Recovery | N/A (success path) |
| Test | `test_case1_normal` — **PASSED** |

### Case 2 — Missing Information

| Field | Detail |
|---|---|
| Scenario | (a) Empty course reference; (b) invalid attempt type |
| Expected | `ACTION_REQUIRED` both times; zero attempts stored |
| Actual | `ACTION_REQUIRED/ACTION_REQUIRED; attempts stored=0` |
| Recovery | Staff corrects the invalid field and resubmits |
| Test | `test_case2_missing_information` — **PASSED** |

### Case 3 — Duplicate Request

| Field | Detail |
|---|---|
| Scenario | Same attempt key submitted after original already published |
| Expected | `DUPLICATE`; one record in system; grade unchanged |
| Actual | `DUPLICATE; attempts stored=1; grade unchanged=B` |
| Recovery | Original published record unaffected; duplicate logged for review |
| Test | `test_case3_duplicate` — **PASSED** |

### Case 4 — Unauthorized Request

| Field | Detail |
|---|---|
| Scenario | (a) Another student views SYN-S-1's record; (b) employer without consent; (c) SYN-S-1 views own |
| Expected | (a) None, denial logged; (b) None, denial logged; (c) record returned |
| Actual | `other=None employer=None own returned=True; denials logged=2` |
| Recovery | Legitimate access routed through consent or authorized role |
| Test | `test_case4_unauthorized` — **PASSED** |

### Case 5 — Failed Step (Sync Failure and Recovery)

| Field | Detail |
|---|---|
| Scenario | Placement sync fails after approved publication; sysadmin retries; second retry is idempotent |
| Expected | `PUBLISHED` status retained; `SYNC_FAILED`; `effective_grades` updated; `placement` NOT updated; after retry `SYNCED` |
| Actual | `status=PUBLISHED sync_status=SYNC_FAILED effective_grade=B in_placement=False; after retry sync_status=SYNCED placement=B audit_valid=True` |
| Recovery | Sysadmin or exam_approver retries via `retry_sync()`; idempotent (second call = same result) |
| Test | `test_case5_failed_step_and_recovery` — **PASSED** |

### Additional Tests (all PASSED)

| Test | What it verifies |
|---|---|
| `test_grade_replacement_a_to_c_same_course` | Two distinct attempts on same course; A published first; C published second; C becomes effective; A in attempt 1's record unchanged |
| `test_grade_replacement_pending_then_publish_sequence` | Normal-workflow only: A pending; C authorized by approver via publish(); C effective; A in attempt 1; empty attempt_history on attempt 2; placement updated to C; audit intact |
| `test_effective_grade_unchanged_while_pending` | Effective grade stays A while second attempt is at AWAITING_APPROVAL |
| `test_sync_failure_does_not_change_effective_grade` | Sync failure leaves `effective_grades` correct; `placement` not updated; retry fixes placement |
| `test_sync_failure_stale_then_recovery` | 8-step: A synced → C published → sync fails → stale A explicitly marked SYNC_FAILED → retry by authorized role → placement updated to C → idempotent second retry |
| `test_unapproved_cannot_publish` | Wrong stage, exam_staff, sysadmin all denied |
| `test_advance_cannot_publish_or_skip` | `advance()` blocked from PUBLISHED; student cannot advance |
| `test_deadline_flag_is_flag_only` | Flag returned for near-deadline; no status changed |
| `test_audit_tamper_detected` | Modified audit field breaks hash chain |
| `test_audit_includes_timestamps` | Every audit record contains a non-empty `ts` field |
| `test_retry_sync_unauthorized` | Student and placement roles get DENIED on retry |
| `test_unknown_key_safe` | Unknown and None keys return UNKNOWN_KEY without raising exceptions |
| `test_missing_student_id_safe` | Empty student ID returns ACTION_REQUIRED or None safely |
| `test_invalid_role_denied` | Unrecognized actor is denied without exception |
| `test_duplicate_different_type_not_duplicate` | Same course but different type/date = distinct keys, not duplicates |

---

## 13. ROI Assumptions, Equations, and Results

> **All inputs are illustrative assumptions** (E-10). No real handling times or case volumes were measured.

### Formulas

```
Gross saving (min/mo) = cases_per_month × (current_min_per_case − proposed_min_per_case)
Net saving (min/mo)   = gross_saving − monthly_overhead_min
Break-even (cases/mo) = monthly_overhead_min ÷ (current_min_per_case − proposed_min_per_case)
```

**Overhead includes:** review time, staff support queries, exception handling, SYNC_FAILED reconciliation, and system administration. Estimated at 180 min/month in all three scenarios.

### Results (from `prototype/roi_calc.py`, run 23 Oct 2026)

| Scenario | Cases/mo | Current min/case | Proposed min/case | Overhead min/mo | Gross (min) | Net (min) | Net h/mo | Break-even |
|---|---|---|---|---|---|---|---|---|
| Conservative | 50 | 8 | 5 | 180 | 150 | **−30** | **−0.5** | 60 |
| **Base** | **100** | **10** | **4** | **180** | **600** | **420** | **7.0** | **30** |
| Optimistic | 200 | 12 | 3 | 180 | 1,800 | 1,620 | **27.0** | 20 |

**Worked check (base):** 100 × (10 − 4) = 600 min gross; 600 − 180 = 420 min = 7.0 h. Break-even = 180 ÷ (10 − 4) = 30. ✓

**Reading:** At low case volumes (conservative scenario), overhead exceeds the saving — net is negative. Real-world savings cannot be established until representative case volumes and handling times are measured with institutional permission. One-time build and training effort is not estimated; payback = that effort ÷ net hours per month once measured.

Full table: [`evidence/roi_results.md`](evidence/roi_results.md) | Script: [`prototype/roi_calc.py`](prototype/roi_calc.py)

---

## 14. Risks, Limitations, and Validation Plan

### Risks and Safeguards

| Risk | Safeguard |
|---|---|
| Wrong or premature grade | Approver-only publish; tested |
| Wrong effective grade used for eligibility | Separate `effective_grades` record updated only after authorized publication |
| Privacy breach | Role-based access; `attempt_history` hidden from placement/employer; consent required for employers |
| Sync failure hiding approved grade | Separate `SYNC_FAILED` flag; `effective_grades` unchanged; retry by authorized role only |
| Unfair prioritization via deadline flag | Flag is informational only; no status changes; tested |
| Process ownership unclear | All proposed roles explicitly require institutional confirmation |
| Unsupported savings claims | All figures labelled assumptions; formulas shown; measurement plan stated |
| Audit log not production-grade | Clearly labelled as in-memory tamper-evident demonstration with real generated timestamps; not a durable store |
| Unknown keys causing crashes | `_require_key()` returns controlled `UNKNOWN_KEY` rather than raising `KeyError`; tested |

### Limitations

1. Evidence is one directly documented 90-day case. General frequency and impact are unknown.
2. Internal handoffs, actual processing stages, and staff responsibilities are assumed — not verified through a staff walkthrough or system access.
3. No written regulation for the grade-replacement rule has been reviewed. The prototype implements verbal guidance (REPORTED, E-07).
4. The Summer Term eligibility source document was not obtained — this is a disclosed evidence limitation.
5. The placement-form screenshot (E-03) is **present in the repository** (`evidence/Screenshort_Evidence.png`, 56 KB, reviewed, shows "SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS", no private data).
6. ROI figures are illustrative; no real handling times or volumes were measured.
7. The prototype is in-memory only; not connected to any IFHE system; no persistent storage; state is lost on restart.
8. CGPA recalculation is not implemented — the official credit-hour and grade-point formula were not confirmed; documented as a policy-dependent component.
9. Audit timestamps are real generated values but are not cryptographically secured across restarts.

### Abandon or Change Triggers

- Fewer than ~30 pending cases/month → net saving is zero or negative at base overhead; not worth the overhead cost.
- Per-case saving under ~3 minutes at 100 cases/month → same conclusion.
- Policy forbids showing interim status to students → change scope to a staff-only exception queue.
- Results are already visible to students in an existing system → the gap is smaller than claimed; validate first.

### Validation Plan

- Seek permission for an anonymized count of Summer Term pending cases per month.
- Seek permission for a brief staff walkthrough to confirm actual handoffs and owner roles.
- Measure current handling time with permission before claiming any net saving.
- Confirm the written grade-replacement regulation from an official IFHE source.
- Confirm whether the placement form can distinguish improvement attempts from failed-subject repeats.
- Seek voluntary faculty or graduate feedback on the proposed workflow design.

---

## 15. Requirement-to-Evidence Checklist

| Task 1 requirement | Where satisfied | Status |
|---|---|---|
| Investigate a small college workflow with permission | §3, §5, §6 | Included; permission limited to discussions and documented experience |
| Map steps, handoffs, approvals, exceptions, roles | §5 | Included; internal steps labelled ASSUMPTION |
| Dated evidence log with category labels | §6 (E-01 to E-11) | Included; some dates approximate; screenshot **present** (`evidence/Screenshort_Evidence.png`) |
| Explain the problem and estimate scale | §1, §3 | Included; scale: one documented case; general frequency unknown |
| Summer Term eligibility (E, D, F, C, or B) | §4 | Documented; verbally confirmed by officials; written source document not obtained (disclosed limitation) |
| Proposed workflow: inputs, statuses, owner, boundary, fallback | §8 | Included; all roles require institutional confirmation |
| Five synthetic cases: expected, actual, recovery | §12 | Complete — 20 tests pass, including all 5 required scenarios |
| Net time saved after overhead | §13 | Included; all inputs labelled assumptions; arithmetic verified |
| Grade-improvement rule documented and implemented | §9 | Included; verbal guidance only; written regulation missing |
| Effective-grade separate from attempt records | §9, code | Complete — `effective_grades[(student, course)]` keyed separately |
| Sync-failure stale-marking and recovery (8-step) | §9, §12, code | Complete — `test_sync_failure_stale_then_recovery` PASSED; SYNC_FAILED state prevents stale A from being treated as current |
| Simultaneous-publication limitation noted | §10 | Included |
| Authorization boundaries defined and tested | §8, §11, §12 | Complete — tested including unknown keys and invalid roles |
| ROI arithmetic verifiable | §13 | Verified; worked check shown |
| Risks and limitations | §14 | Included |
| Personal contribution and AI-use record | §16 | Included; AI model version was not recorded during the session |
| No private data committed | Throughout | Verified; all prototype data is SYNTHETIC |
| Placement-form screenshot evidence (E-03) | §6, §7 | Screenshot **present** (`evidence/Screenshort_Evidence.png`, 56 KB, reviewed — no private data; shows "SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS") |
| Summer Term eligibility includes E, D, F, C, or B | §4, §3 | Documented (verbally confirmed by officials); written source document not yet committed |

---

## 16. Personal Contribution and AI-Use Record

**Personal contribution:**
- Identified and scoped the problem based on one directly documented waiting experience.
- Supplied all dated observations (E-01 to E-04), the computed elapsed time (E-05), and the placement-form screenshot (E-03, present as `evidence/Screenshort_Evidence.png`).
- Defined the workflow scope and the decision to label unverified internal stages as assumptions rather than assert them as facts.
- Reviewed and approved all prototype logic, test cases, and report content.
- Responsible for this document and prepared to defend every section and finding.

**AI assistance:**
- An AI coding assistant was used to help structure this report, implement the prototype code, write the test suite, and draft the ROI script.
- **Model:** An AI coding assistant (Google Gemini via Antigravity IDE) was used. The exact model version was not recorded during the session.
- **Dates of use:** 21–22 Oct 2026.
- **Verification:** All scripts were executed locally; outputs are saved in `evidence/`. The 90-day elapsed-time count and ROI arithmetic were checked manually. No model output was used as evidence of any IFHE process or policy.

**CGPA recalculation:** Not implemented. The official credit-hour and grade-point rules were not confirmed; this is documented as a policy-dependent component.

---

## 17. Final Summary

**Problem:** A pending grade-improvement result leaves students uncertain about their effective grade and how that subject appears on the placement form. One documented case recorded a 90-day gap between the Summer Term exam and 22 October 2026 with no published result.

**Proposed solution:** ResultFlow proposes transparent result-status tracking, approver-only grade publication, a separate `effective_grades` record keyed by student and course (updated only on authorized publication, even if the new grade is lower), a deadline-based review flag, and idempotent sync to the placement record with explicit failure handling and authorized retry.

**Evidence and validation:** Evidence base is one directly documented 90-day case (OBSERVED, as of 22 Oct 2026), a placement-form screenshot (OBSERVED, `evidence/Screenshort_Evidence.png`, present in repository, shows "SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS", no private data), and conversations with peers and a staff member (REPORTED). Twenty synthetic tests pass. ROI figures are illustrative assumptions.

**Limitations:** Internal processing stages were not directly observed. No written grade-replacement regulation was reviewed. The Summer Term eligibility source document is not yet committed (eligibility verbally confirmed: grades E, D, F, C, or B in the relevant subject). Volumes and handling times are estimated. The prototype is in-memory only and is not connected to any IFHE system.
