# ResultFlow — Academic Result Transparency & Placement Readiness

> **Student-proposed workflow improvement and reference prototype — HKAIVERSE Round 2, Task 1.**
> Not an officially deployed IFHE system. Not an official policy revision. Not connected to any live college database.
> Detailed investigation report: [TASK1_REPORT.md](TASK1_REPORT.md)

---

## Overview

- **Process Studied:** Summer Term grade-improvement result processing through to placement checks at IFHE Hyderabad.
- **Problem Identified:** Students waiting for grade-improvement results face extended uncertainty. In one documented case, a student waited **90 days** (24 July to 22 October 2026) with no published result or update. Meanwhile, a placement registration form (`evidence/Screenshort_Evidence.png`) states that pending Summer Term subjects are *"TREATED AS BACKLOGS"* until results release, making students with passing grades look like they have active backlogs.
- **Evidence Base:** Two direct observations (the 90-day wait and the genuine placement-form screenshot), supported by verbal staff and peer accounts. Internal college processing was not observed and remains an assumption.
- **Proposed Solution:** **ResultFlow** introduces visible stage tracking, approver-only publishing, a separate effective-grade record, safe placement synchronization with error handling, and near-deadline review flags.
- **Validation:** Validated by **20 automated tests** (all passing) covering five required synthetic scenarios, grade-replacement downgrades, error recovery, and role boundaries.
- **Limitations:** Based on one documented case; internal handoffs are assumed; policy rules were verbally confirmed without written source documents; ROI figures are illustrative estimates; prototype runs in memory only.

---

## Current-State Process vs. Proposed Workflow

There is an unmistakable difference between what students experience today and what ResultFlow proposes:

### Current Process (Student-Visible View Only)
Students see only the start and end of the timeline; internal college handling is unobserved:
1. **Exam completed:** Student finishes Summer Term exam on 24 July 2026 (OBSERVED).
2. **Silent wait:** No progress tracker or estimated publication date is provided during follow-ups (OBSERVED, E-02, E-04).
3. **Placement form observed:** Placement form states pending subjects are treated as backlogs (approx. Aug 2026, OBSERVED, E-03).
4. **Internal processing:** Grading, verification, and approvals occur internally (ASSUMPTION — unobserved).
5. **Result publication:** Result unpublished after 90 days as of 22 October 2026 in the documented case (OBSERVED, E-05).

### Proposed ResultFlow Workflow
ResultFlow replaces opacity with clear stages, permissions, and safeguards:
1. **Visible Tracking:** Attempts move visibly: `REGISTERED → EXAM_COMPLETED → RESULT_PROCESSING → UNDER_VERIFICATION → AWAITING_APPROVAL → PUBLISHED`.
2. **Approval Gate:** Only an authorized approver can release an official grade.
3. **Protected Effective Grade:** A student's existing passing grade remains active and valid while an improvement attempt is pending.
4. **Safe Placement Sync:** Approved grades sync to placement records automatically. If sync fails, the system logs the error safely and allows authorized retries without creating duplicate or inconsistent updates.

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

| Component | Current Reality | ResultFlow Proposal |
|---|---|---|
| **Result Tracking** | 90 days elapsed with no visible status or ETA (one case) | Step-by-step visible status tracking with update timestamps |
| **Placement Standing** | Form treats pending subjects as backlogs (`Screenshort_Evidence.png`) | Distinguishes pending improvement from an active backlog |
| **Grade Authority** | Verbal staff guidance on grade replacement (REPORTED, E-07) | Separate effective-grade record updated only on authorized publication |
| **Placement Sync** | Manual or unobserved updates | Safe retries that do not create duplicate or inconsistent updates |
| **Validation** | In-memory reference prototype | 20 automated tests passing (5 required scenarios + edge cases) |
| **ROI Model** | Unmeasured handling times | Estimated +7.0 h/mo net saving in base scenario (illustrative assumptions) |

Full report: [TASK1_REPORT.md](TASK1_REPORT.md)

---

## 2. The Problem

The investigation identified two primary issues from direct observation:

1. **Uncertainty During Long Waits (OBSERVED, E-01, E-02, E-05):** In the documented case, exams ended 24 July 2026. After 90 days (22 October 2026), no results had been published and enquiries gave no confirmed release date.
2. **Backlog Label on Placement Forms (OBSERVED, E-03):** The placement form (`evidence/Screenshort_Evidence.png`, approx. Aug 2026, 56 KB, no private data) states: *"SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS."* Students with existing passing grades attempting improvement may appear to have open backlogs during placement shortlisting.

ResultFlow resolves this by showing visible status, keeping passing grades active, and flagging cases approaching placement deadlines.

---

## 3. Who Is Affected

- **Students attempting grade improvement:** Students holding an existing grade of **E, D, F, C, or B** in the subject (verbally confirmed by officials — REPORTED, E-11; written source document not yet committed).
- **Placement coordinators:** Staff verifying student eligibility who need clear, current academic standing.
- **Exam administration staff:** Teams managing grading, approvals, and student enquiries.
- **Scope:** Based on one directly documented student case. Institutional volume requires official college data.

---

## 4. Evidence and Findings

All statements use strict evidence categories: `OBSERVED` (directly seen), `REPORTED` (verbal staff/peer accounts), `COMPUTED` (date arithmetic), `ASSUMPTION` (unverified workflow design), and `SYNTHETIC` (artificial test data).

| ID | Date | Category | Summary | Notes |
|---|---|---|---|---|
| E-01 | 24 Jul 2026 | OBSERVED | Summer Term exams ended | Single documented student case |
| E-02 | 22 Oct 2026 | OBSERVED | No result published as of this date | Follow-up enquiries gave no confirmed date |
| E-03 | Approx. Aug 2026 | OBSERVED | Placement form: *"SUMMER TERM SUBJECTS ALSO TREATED AS BACKLOGS"* | Screenshot present: `evidence/Screenshort_Evidence.png` (56 KB, no private data) |
| E-04 | Approx. Sep–Oct 2026 | OBSERVED | Academic contacts asked for update; no date given | Date approximate; no personal names recorded |
| E-05 | 22 Oct 2026 | COMPUTED | 24 Jul to 22 Oct = 90 elapsed days | Date arithmetic on single case |
| E-06 | Approx. Oct 2026 | REPORTED | Peers described similar long waits with no status | Secondhand accounts from conversations |
| E-07 | Approx. Oct 2026 | REPORTED | Staff stated new grade replaces previous grade even if lower | Verbal guidance; written regulation not reviewed |
| E-08 | Approx. Oct 2026 | REPORTED | Lecturer mentioned branches release results simultaneously | Verbal statement; not verified as formal policy |
| E-09 | 22 Oct 2026 | SYNTHETIC | Test IDs, student references, and grades | Used solely for automated prototype testing |
| E-10 | 22 Oct 2026 | ASSUMPTION | Case volumes and handling times for ROI | Illustrative assumptions for arithmetic model |
| E-11 | Approx. Oct 2026 | REPORTED | Officials verbally confirmed eligibility: grades E, D, F, C, or B | Verbal only; written document not committed |

No official IFHE web pages, regulations, or notices are cited as evidence for any process claim.

**Evidence Gaps and Limitations:**
The following limitations apply to the evidence log and are disclosed here rather than treated as unfinished editing tasks:
- **E-03 (screenshot date):** The genuine placement-form screenshot is included in the project (`evidence/Screenshort_Evidence.png`), but its exact capture date was not recorded. The date field for E-03 records "Approx. Aug 2026."
- **Approximate dates (E-04, E-06, E-07, E-08, E-11):** Some dates associated with conversations or follow-up enquiries are approximate or were not recorded at the time.
- **Verbal confirmations (E-07, E-11):** The Summer Term eligibility condition (E, D, F, C, or B) and the grade-replacement rule were reported verbally by academic officials. The written eligibility document and any written grade-replacement regulation were not obtained or included in the repository.
- **AI model version (§16 of report):** The exact AI model version used during development was not recorded during the session.
- **Internal stages:** The internal college processing stages and handoffs between exam completion and result publication were not directly verified and remain assumptions throughout this project.

These are disclosed evidence limitations, not fabricated or silently completed evidence.

---

## 5. Proposed Solution

ResultFlow replaces uncertainty with structured, role-gated rules:

1. **Visible Status Tracking:** Attempts advance through clear stages (`REGISTERED → EXAM_COMPLETED → RESULT_PROCESSING → UNDER_VERIFICATION → AWAITING_APPROVAL → PUBLISHED`).
2. **Approver-Only Publishing:** Only the `exam_approver` role can release a final grade; others are denied.
3. **Independent Effective Grade:** A student's current official grade (`effective_grades`) is stored separately from pending attempts. Existing passing grades are never altered while an attempt is pending.
4. **Permanent Grade History:** Publishing archives earlier grades; nothing is overwritten or lost.
5. **Safe Placement Synchronization:** Approved grades sync to placement records. Sync failures are flagged as `SYNC_FAILED` without corrupting academic records, allowing safe retries that do not create duplicate or inconsistent updates.
6. **Deadline Review Flag:** Flags pending results approaching placement deadlines for staff review without altering grades or skipping verification.
7. **Tamper-Evident Audit Log:** Append-only hash chain with generated UTC timestamps.
8. **Safe Input Handling:** Missing inputs return `ACTION_REQUIRED` and unknown keys return `UNKNOWN_KEY` instead of crashing.

---

## 6. Proposed ResultFlow Workflow

> **This diagram describes the proposed ResultFlow design — not a verified description of the existing IFHE process.** All roles, stage names, and internal handoffs shown here are proposed and require institutional confirmation before any live implementation.

```
REGISTERED
    │
    ▼
EXAM_COMPLETED
    │
    ▼
RESULT_PROCESSING
    │
    ▼
UNDER_VERIFICATION
    │
    ▼
AWAITING_APPROVAL
    │
    └──(exam_approver only)──► PUBLISHED
                                  │
                             effective_grades[(student, course)] updated
                                  │
                             _sync() runs
                                  │
                        ┌─────────┴─────────┐
                        │                   │
                     SYNCED            SYNC_FAILED
                                            │
                                  (sysadmin or exam_approver)
                                      retry_sync()
                                            │
                                          SYNCED

Exceptions handled at any stage:
  ACTION_REQUIRED  ── Missing or invalid input; nothing stored
  DUPLICATE        ── Same attempt key already registered; ignored and logged
  DENIED           ── Unauthorized action; no state changes; event logged
  UNKNOWN_KEY      ── Invalid attempt key reference; controlled return; no crash
```

---

## 7. Grade-Improvement Rule

**Rule (REPORTED — verbal staff guidance, E-07; written regulation not reviewed):**
> When a new grade-improvement result is officially approved and published, that newly published grade becomes the effective grade for the student and course, even if it is lower than the previous published grade.

ResultFlow stores attempt records separately from the active effective grade:
- **Attempts Store:** Keyed by `student|course|type|exam_date`. Preserves every attempt's record.
- **Effective Grades Store:** Keyed by `(student, course)`. Holds the current official grade.

| Step | Effective Grade | Placement Record | What Happens |
|---|---|---|---|
| **1. Attempt 1 published** (Regular exam) | **A** | **A** | Initial passing grade active and synced |
| **2. Attempt 2 pending** (Summer Term) | **A (unchanged)** | **A** | Pending improvement does not affect current grade |
| **3. Attempt 2 published** (Grade C) | **C** | **C** | New grade replaces prior grade upon approval |

Attempt 1's record still retains its original grade A in history. Verified by automated tests `test_grade_replacement_a_to_c_same_course` and `test_grade_replacement_pending_then_publish_sequence`.

---

## 8. Prototype and Architecture

The reference implementation is in [`prototype/resultflow.py`](prototype/resultflow.py) (single file, Python standard library, zero external dependencies).

### Storage Structure
- `attempts`: Stores full attempt records, statuses, and history.
- `effective_grades`: Maps `(student, course)` to the current authorized grade.
- `placement`: The synchronized copy used for placement eligibility checks.

### Key Design Principles
- **Deterministic rules:** Pure Python logic without AI in decision pathways.
- **Role-based permissions:** Strict authorization checks on all operations.
- **Safe error recovery:** Sync failures leave academic records intact and allow safe retries that do not create duplicate or inconsistent updates.
- **Scope clarity:** In-memory prototype for logic validation; not connected to live college databases.

---

## 9. Synthetic Test Results

**Run:** 23 Oct 2026 · Python 3.12.10 · pytest-9.1.1  
**Result: 20 passed, 0 failed.** (Log: [`evidence/pytest_output.txt`](evidence/pytest_output.txt))

### Five Required Scenarios

| # | Scenario | Test Function | Result |
|---|---|---|---|
| 1 | **Normal Request** — Attempt registered, advanced through approvals, published, and synced | `test_case1_normal` | **PASSED** |
| 2 | **Missing Information** — Incomplete or invalid attempt rejected safely | `test_case2_missing_information` | **PASSED** |
| 3 | **Duplicate Request** — Resubmitting existing attempt key is blocked without altering data | `test_case3_duplicate` | **PASSED** |
| 4 | **Unauthorized Access** — Unapproved roles blocked from publishing or viewing private records | `test_case4_unauthorized` | **PASSED** |
| 5 | **Failed Step & Recovery** — Sync failure handled safely; retry restores consistent state | `test_case5_failed_step_and_recovery` | **PASSED** |

### Additional Tests (15 Passed)
Fifteen additional tests verify grade-replacement downgrades (A to C), 8-step sync failure and recovery, role publishing boundaries, audit log hash-tamper detection, and safe error handling for missing fields and unknown keys.

Demonstration output: [`evidence/case_results.md`](evidence/case_results.md)

---

## 10. ROI and Time Savings

> **All inputs are illustrative assumptions (E-10).** No real handling times or case volumes were measured.
> Overhead (180 min/month) covers monthly reviews, staff queries, exception handling, and administration.

| Scenario | Cases/mo | Current min/case | Proposed min/case | Overhead min/mo | Gross min saved | Net min saved | Net h/mo | Break-even |
|---|---|---|---|---|---|---|---|---|
| Conservative | 50 | 8 | 5 | 180 | 150 | −30 | **−0.5** | 60 cases/mo |
| **Base** | **100** | **10** | **4** | **180** | **600** | **420** | **+7.0** | **30 cases/mo** |
| Optimistic | 200 | 12 | 3 | 180 | 1,800 | 1,620 | **+27.0** | 20 cases/mo |

**Worked check (base):** 100 × (10 − 4) = 600 min gross; 600 − 180 = 420 min = **7.0 h/mo**. Break-even = 180 ÷ 6 = **30 cases/mo**.

**Takeaway:** At low volume (50 cases/month), overhead exceeds time saved (−0.5 h/month). At base volume (100 cases/month), the workflow saves an estimated **7.0 hours/month**. Real-world savings cannot be claimed until case volumes and handling times are measured with institutional permission.

Full table: [`evidence/roi_results.md`](evidence/roi_results.md) · Script: [`prototype/roi_calc.py`](prototype/roi_calc.py)

---

## 11. How to Run

Requirements: Python 3 (tested on 3.12.10) and pytest. Standard library only.

```bash
cd prototype

# Run all 20 automated tests
python -m pytest -v

# Run the five-case demonstration
python run_cases.py

# Run the ROI calculation model
python roi_calc.py
```

Outputs are saved in `evidence/` (generated 23 Oct 2026).

---

## 12. Repository Structure

```
ResultFlow/
├── README.md                      <- Project summary and quick recruiter guide (this file)
├── TASK1_REPORT.md                <- Comprehensive 17-section investigation report
├── prototype/
│   ├── resultflow.py              <- Workflow rules engine (standard library only)
│   ├── test_resultflow.py         <- 20 automated pytest test cases
│   ├── run_cases.py               <- Five-case demonstration runner
│   └── roi_calc.py                <- ROI arithmetic script
└── evidence/
    ├── Screenshort_Evidence.png   <- Placement-form screenshot (OBSERVED, E-03, 56 KB)
    ├── pytest_output.txt          <- Real test run output, 23 Oct 2026 (20 passed)
    ├── case_results.md            <- Five-case demonstration output
    └── roi_results.md             <- ROI calculation output
```

---

## 13. Limitations and Risks

- **Single Documented Case:** The 90-day waiting period reflects one documented student experience. Institutional averages were not measured.
- **Unverified Internal Handoffs:** Internal processing stages, roles, and handoffs are assumed, not directly observed.
- **Verbal Policy Guidance:** Summer Term eligibility (grades E, D, F, C, or B) and the grade-replacement rule were verbally reported by staff; written institutional regulations were not obtained.
- **Illustrative ROI:** Time estimates and volume numbers are modeling assumptions, not measured institutional statistics.
- **In-Memory Prototype:** Demonstrates business logic in memory; not integrated with live college infrastructure.
- **Scope Boundary:** ResultFlow does not alter grading standards, expedite paper correction, or calculate CGPA.

---

## 14. Interview Talking Points

**1. What specific problem does ResultFlow address?**  
The lack of visibility between Summer Term exams and result publication, and the ambiguity caused when placement forms label pending subjects as backlogs. In one documented case, a student waited 90 days with no status updates.

**2. What direct evidence supports the project?**  
Two primary observations: the 90-day wait (24 July to 22 October 2026) and a genuine placement-form screenshot (`evidence/Screenshort_Evidence.png`) stating pending Summer Term subjects are treated as backlogs. Eligibility criteria and grade-replacement rules were verbally reported.

**3. What does ResultFlow propose?**  
A role-governed workflow that gives students status visibility, restricts grade publishing to authorized approvers, separates current effective grades from pending attempts, and synchronizes with placement records safely.

**4. What did the prototype prove?**  
All 20 automated tests passed, confirming that pending attempts do not alter existing grades before approval, approved downgrades replace prior grades while preserving history, sync failures allow safe retries without creating duplicate or inconsistent updates, and unauthorized roles are blocked safely.

**5. What are the key limitations?**  
The investigation is based on one documented case, internal college stages are assumed, policy details were verbally confirmed without written source documents, and ROI savings are estimates rather than measured data.

---

## 15. Final Summary

**Problem:** A pending grade-improvement result creates uncertainty about which grade is currently effective and how the pending subject appears in placement processing. One documented case recorded 90 elapsed days between the Summer Term exam and the evidence cutoff with no published result.

**Solution:** ResultFlow proposes transparent status tracking, approver-only publication, a separate `effective_grades` record per student and course (updated only on authorized publication, even if the new grade is lower), a deadline-based review flag, and safe placement synchronization with explicit failure handling and authorized retry.

**Evidence and Validation:** One directly observed 90-day case; a placement-form screenshot (OBSERVED, present as `evidence/Screenshort_Evidence.png`); peer-reported experiences (REPORTED); verbal staff guidance on grade replacement (REPORTED). Twenty synthetic tests pass. ROI is hypothetical.

**Limitations:** Internal processing stages were not directly observed. No written grade-replacement regulation was reviewed. Summer Term eligibility verbally confirmed (E, D, F, C, or B) — written source not yet committed. Volumes and handling times are estimated assumptions. The prototype is in-memory only and is not connected to any IFHE system.

*This is a student proposal demonstrating what a structured, accountable process could look like. It uses no real student data and makes no claims about any specific IFHE system.*
