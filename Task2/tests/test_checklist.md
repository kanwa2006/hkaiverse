# Test Checklist — HKAIVERSE Round 2, Task 2

> This checklist covers all manual and automated tests for Task 2. The browser automation tool was unavailable in this session (Playwright driver CDN error), so tests for the interactive component are documented as reproducible manual instructions.

---

## Section A — Interactive Course Explorer Tests

Open `Task2/course_explorer.html` in any modern browser (Chrome, Firefox, Edge) by double-clicking the file or using `File → Open`.

### Test CE-01: All Courses Load on Startup

| Field | Detail |
|---|---|
| **Test ID** | CE-01 |
| **Input** | Open the file with no filters applied |
| **Expected result** | All 53 course rows are visible in the table |
| **How to check** | Look at the "courses shown" count below the controls — it should read 53 |
| **Status** | ⬜ To verify |

### Test CE-02: Search Filter — Course Code

| Field | Detail |
|---|---|
| **Test ID** | CE-02 |
| **Input** | Type "CS" in the search box |
| **Expected result** | Only rows with "CS" in the code or name are shown; non-CS rows are hidden |
| **How to check** | Verify that CHY101, PH101, MA101 etc. are not visible |
| **Status** | ⬜ To verify |

### Test CE-03: Search Filter — Course Name

| Field | Detail |
|---|---|
| **Test ID** | CE-03 |
| **Input** | Type "database" in the search box |
| **Expected result** | CS206 (Database Management Systems) is shown |
| **How to check** | One row visible: CS206 |
| **Status** | ⬜ To verify |

### Test CE-04: Semester Filter

| Field | Detail |
|---|---|
| **Test ID** | CE-04 |
| **Input** | Select "Semester 5" from the Semester dropdown |
| **Expected result** | 8 courses shown: CR301, CS301, CS302, CS303, CS304, DS303, DS304, HS301 |
| **How to check** | Count rows and check all 8 Semester 5 codes are present |
| **Status** | ⬜ To verify |

### Test CE-05: Action Filter — UPDATE

| Field | Detail |
|---|---|
| **Test ID** | CE-05 |
| **Input** | Select "UPDATE" from the Action dropdown |
| **Expected result** | 9 courses shown (CS101, CS102, CS205, CS206, CS302, CS304, DS304, CS307, CS415) |
| **How to check** | Count rows — should be 9; all action badges should show UPDATE |
| **Status** | ⬜ To verify |

### Test CE-06: Action Filter — REDUCE

| Field | Detail |
|---|---|
| **Test ID** | CE-06 |
| **Input** | Select "REDUCE" from the Action dropdown |
| **Expected result** | 3 courses shown: PH101, MG201, HS201 |
| **How to check** | 3 rows visible; all with REDUCE badge |
| **Status** | ⬜ To verify |

### Test CE-07: Action Filter — ADD

| Field | Detail |
|---|---|
| **Test ID** | CE-07 |
| **Input** | Select "ADD" from the Action dropdown |
| **Expected result** | 1 course shown: CS-NEW (Applied Software Product Engineering Lab) |
| **How to check** | 1 row visible; ADD badge; base=0, proposed=3, change=+3 |
| **Status** | ⬜ To verify |

### Test CE-08: Credit Calculations — All Courses

| Field | Detail |
|---|---|
| **Test ID** | CE-08 |
| **Input** | Reset all filters (click Reset button) |
| **Expected result** | Baseline (filtered) = 167; Proposed (filtered) = 167; Net change = 0 |
| **How to check** | Read the Calculation box at the bottom of the page |
| **Status** | ⬜ To verify |

### Test CE-09: Credit Calculations — REDUCE Filter

| Field | Detail |
|---|---|
| **Test ID** | CE-09 |
| **Input** | Filter by Action = REDUCE |
| **Expected result** | Baseline (filtered) = 5+3+3 = 11; Proposed = 4+2+2 = 8; Net = −3 |
| **How to check** | Read the Calculation box |
| **Status** | ⬜ To verify |

### Test CE-10: Empty State

| Field | Detail |
|---|---|
| **Test ID** | CE-10 |
| **Input** | Type "xyzxyzxyz" in the search box |
| **Expected result** | No rows visible; empty state message appears ("No courses match your filters") |
| **How to check** | Table body is empty; empty state div is visible |
| **Status** | ⬜ To verify |

### Test CE-11: Reset Button

| Field | Detail |
|---|---|
| **Test ID** | CE-11 |
| **Input** | Apply filters (CE-06), then click Reset Filters |
| **Expected result** | All filters cleared; all 53 courses shown again |
| **How to check** | Count goes back to 53; search box is empty; dropdowns show "All" |
| **Status** | ⬜ To verify |

### Test CE-12: Sort by Column

| Field | Detail |
|---|---|
| **Test ID** | CE-12 |
| **Input** | Click the "Baseline Cr." column header |
| **Expected result** | Table sorts ascending by baseline credits; HS101 and HS301 (0 credits) appear first |
| **How to check** | First rows have 0 in baseline credit column |
| **Status** | ⬜ To verify |

### Test CE-13: HS301 Credit Value

| Field | Detail |
|---|---|
| **Test ID** | CE-13 |
| **Input** | Search for "HS301" |
| **Expected result** | HS301 Constitution of India shows 0 baseline credits and 0 proposed credits |
| **How to check** | Both credit columns for HS301 show 0 |
| **Status** | ⬜ To verify |

### Test CE-14: IP-1 and IP-2 Visibility

| Field | Detail |
|---|---|
| **Test ID** | CE-14 |
| **Input** | Filter Semester = "Mandatory IP-1" then separately "Mandatory IP-2" |
| **Expected result** | IP-1: shows IP201 (3 credits). IP-2: shows IP-2 [TBC] (15 credits). |
| **How to check** | Correct rows appear for each filter |
| **Status** | ⬜ To verify |

---

## Section B — Capstone Acceptance Tests (Synthetic Data)

These tests are defined in `LAB_CAPSTONE_PROPOSAL.md` Section 7. They are to be implemented and run by students completing the Applied Software Product Engineering Lab. They are documented here as a cross-reference.

| Test ID | Scenario | Expected Result | Status |
|---|---|---|---|
| T1 | Duplicate request detection | Second submission returns DUPLICATE_DETECTED; only one DB record created | Defined in LAB proposal; not yet executed |
| T2 | Missing information routing | Empty subject field → MISSING_FIELD error; no record stored | Defined in LAB proposal; not yet executed |
| T3 | Unauthorized approval rejection | STUDENT role cannot APPROVE; request stays UNDER_REVIEW | Defined in LAB proposal; not yet executed |
| T4 | Failed step recovery | DB failure during APPROVE → error logged; status unchanged | Defined in LAB proposal; not yet executed |
| T5 | Before/after process measure | Synthetic estimate: ~200 min/week saving with automation (labelled estimate) | Defined in LAB proposal; illustrative only |

---

## Section C — Report Consistency Checks

These are manual checks to ensure the course explorer data matches the report.

| Check | Expected | Status |
|---|---|---|
| Total courses in explorer matches report | 53 rows in explorer | ⬜ To verify |
| HS301 = 0 credits in both baseline and proposed | explorer and CURRICULUM_AUDIT.md both show 0 | ⬜ To verify |
| Three REDUCE courses with −1 each | PH101 (5→4), MG201 (3→2), HS201 (3→2) | ⬜ To verify |
| One ADD course with +3 | CS-NEW (0→3) | ⬜ To verify |
| Total baseline = 167 | Sum of all baseline credits | ⬜ To verify |
| Total proposed = 167 | Sum of all proposed credits | ⬜ To verify |
| Net change = 0 | 167 − 167 = 0 | ⬜ To verify |
| CREDIT_CALCULATIONS.md matches explorer totals | Both show 167/167/0 | ⬜ To verify |

---

## Section D — Repository Integrity Checks

| Check | Expected | Status |
|---|---|---|
| Task1 files unchanged | All Task1 files preserved byte-for-byte | ⬜ Verify with git diff |
| No private student data committed | No real names, IDs, grades, credentials | ⬜ Scan Task2/ |
| Task2 README links all documents | All links resolve | ⬜ Check manually |
| Root README links to Task2 | Task2 section present | ⬜ Check manually |
| All Task2 files present | See file list below | ⬜ Check |

### Required Task 2 Files

- [x] `Task2/README.md`
- [x] `Task2/CURRICULUM_AUDIT.md`
- [x] `Task2/COURSE_MAP.csv`
- [x] `Task2/JOB_DESCRIPTION_COMPARISON.md`
- [x] `Task2/AI_EXERCISES.md`
- [x] `Task2/FEEDBACK_AND_LIMITATIONS.md`
- [x] `Task2/SOURCES.md`
- [x] `Task2/CREDIT_CALCULATIONS.md`
- [x] `Task2/LAB_CAPSTONE_PROPOSAL.md`
- [x] `Task2/course_explorer.html`
- [x] `Task2/tests/test_checklist.md` (this file)

---

*test_checklist.md | Task 2 | HKAIVERSE Round 2 | 24 October 2026*
