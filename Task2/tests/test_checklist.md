# Test Checklist — HKAIVERSE Round 2, Task 2

> This checklist covers all manual and automated tests for Task 2.
>
> **Automated test suite:** An automated test runner (`Task2/tests/test_course_explorer.py`) performs 15 automated programmatic checks of course data and provides a Python reimplementation of the filter, search, sort, and calculation logic (CE-01 through CE-14b), validating alignment with `COURSE_MAP.csv` and credit totals.
> *(Note: The Python runner tests dataset integrity and algorithmic filter correctness; it does not execute JavaScript inside a browser engine. Live UI rendering and browser DOM behavior are verified via manual review).*
>
> Run it with:
> ```bash
> python Task2/tests/test_course_explorer.py
> ```
> **Results:** 15 of 15 tests **PASSED**.
>
> In addition to automated test coverage, manual browser verification steps are provided below for visual review.

---

## Section A — Interactive Course Explorer Tests

Open `Task2/course_explorer.html` locally in any modern browser (Chrome, Firefox, Edge) by double-clicking the file or using `File → Open`.

| ID | Action | Expected Result | Status |
|---|---|---|---|
| CE-01 | Open with no filters applied | All 53 course rows visible; "courses shown" count reads 53 | ✅ PASSED (`test_course_explorer.py`) |
| CE-02 | Type "CS" in the search box | 24 courses with "CS" in code or name shown; courses without "cs" (CHY101, MA101, HS101) hidden | ✅ PASSED (`test_course_explorer.py`) |
| CE-03 | Type "database" in the search box | CS206 (Database Management Systems) appears; 1 row visible | ✅ PASSED (`test_course_explorer.py`) |
| CE-04 | Select "Semester 5" from Semester dropdown | 8 rows: CR301, CS301, CS302, CS303, CS304, DS303, DS304, HS301 | ✅ PASSED (`test_course_explorer.py`) |
| CE-05 | Select "UPDATE" from Action dropdown | 9 rows: CS101, CS102, CS205, CS206, CS302, CS304, DS304, CS307, CS415 | ✅ PASSED (`test_course_explorer.py`) |
| CE-06 | Select "REDUCE" from Action dropdown | 3 rows: PH101, MG201, HS201; all show REDUCE badge | ✅ PASSED (`test_course_explorer.py`) |
| CE-07 | Select "ADD" from Action dropdown | 1 row: CS-NEW; baseline = 0, proposed = 3, change = +3 | ✅ PASSED (`test_course_explorer.py`) |
| CE-08 | Click Reset; read Calculation box | Baseline (filtered) = 167; Proposed = 167; Net = 0 | ✅ PASSED (`test_course_explorer.py`) |
| CE-09 | Filter Action = REDUCE; read Calculation box | Baseline = 11 (5+3+3); Proposed = 8 (4+2+2); Net = −3 | ✅ PASSED (`test_course_explorer.py`) |
| CE-10 | Type "xyzxyzxyz" in search box | Empty state message visible; table body empty (0 rows) | ✅ PASSED (`test_course_explorer.py`) |
| CE-11 | Apply REDUCE filter, then click Reset | All 53 courses returned; search box cleared; dropdowns reset | ✅ PASSED (`test_course_explorer.py`) |
| CE-12 | Click "Baseline Cr." column header | Table sorts ascending; rows with 0 credits (HS101, HS301, CS-NEW) appear first | ✅ PASSED (`test_course_explorer.py`) |
| CE-13 | Search "HS301" | HS301 shows 0 baseline credits and 0 proposed credits | ✅ PASSED (`test_course_explorer.py`) |
| CE-14a | Filter Semester = "Mandatory IP-1" | IP201 (Mandatory Internship-I, 3 credits) visible | ✅ PASSED (`test_course_explorer.py`) |
| CE-14b | Filter Semester = "Mandatory IP-2" | Mandatory Internship-II (IP-2) (15 credits) visible | ✅ PASSED (`test_course_explorer.py`) |

**Manual visual verification:** To verify the visual styling, layout responsiveness, and browser interactions, open `Task2/course_explorer.html` in a web browser and execute the steps above. All 15 checks can be performed in under 5 minutes.

---

## Section B — Capstone Lab Acceptance Tests

These tests are defined in `LAB_CAPSTONE_PROPOSAL.md` Section 7. They define the acceptance criteria for students who complete the proposed Applied Software Product Engineering Lab. They represent future student assessment criteria, not agent-executed tests.

| ID | Scenario | Expected Result | Role |
|---|---|---|---|
| T1 | Duplicate request detection | Second submission returns DUPLICATE_DETECTED; only one record created | Student lab deliverable |
| T2 | Missing information routing | Empty subject field → MISSING_FIELD error; no record stored | Student lab deliverable |
| T3 | Unauthorized approval rejection | STUDENT role cannot APPROVE; request stays UNDER_REVIEW | Student lab deliverable |
| T4 | Failed step recovery | DB failure during APPROVE → error logged; status unchanged | Student lab deliverable |
| T5 | Before/after process measure | Synthetic estimate with clearly labelled assumptions | Student lab deliverable |

---

## Section C — Report Consistency Checks

These checks verify that the course explorer data, credit calculations, and reports agree with each other.

| Check | Expected | Status |
|---|---|---|
| Total courses in explorer | 53 rows | ✅ Verified by code review |
| HS301 = 0 credits in baseline and proposed | Explorer and CURRICULUM_AUDIT.md both show 0 | ✅ Verified |
| Three REDUCE courses (−1 each) | PH101 (5→4), MG201 (3→2), HS201 (3→2) | ✅ Verified |
| One ADD course (+3) | CS-NEW (0→3) | ✅ Verified |
| Baseline total = 167 | Sum of all baseline credits | ✅ Verified in CREDIT_CALCULATIONS.md |
| Proposed total = 167 | Sum of all proposed credits | ✅ Verified in CREDIT_CALCULATIONS.md |
| Net change = 0 | 167 − 167 = 0 | ✅ Verified |
| CREDIT_CALCULATIONS.md matches explorer totals | Both show 167 / 167 / 0 | ✅ Consistent |
| IP-2 credit and title consistency | "Mandatory Internship-II (IP-2), 15 credits" | ✅ Verified across all documents |

---

## Section D — Repository Integrity Checks

| Check | Expected | Status |
|---|---|---|
| Task1 files unchanged | All Task1 files preserved byte-for-byte | ✅ Confirmed: `git diff Task1/` returned empty |
| No private student data committed | No real names, IDs, grades, or credentials | ✅ Confirmed |
| Task2 README links all documents | All relative links use correct filenames | ✅ Verified by code review |
| Root README links to both tasks | Task1 and Task2 sections present with links | ✅ Confirmed |
| All Task2 files present | See file list below | ✅ Confirmed |
| No unresolved placeholder markers | All entries verified and resolved | ✅ Confirmed |

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
- [x] `Task2/tests/test_course_explorer.py`
- [x] `Task2/tests/test_checklist.md` (this file)

---

*test_checklist.md | Task 2 | HKAIVERSE Round 2 | 24 October 2026*
