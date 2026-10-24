# Sources and Evidence Log — HKAIVERSE Round 2, Task 2

> All sources are listed with URLs and the date they were accessed (24 October 2026). Where a source could not be fully accessed due to JavaScript rendering or access restrictions, the limitation is noted.

---

## 1. Curriculum Data Sources

| Source | Type | Details |
|---|---|---|
| Student course portal screenshots (`Task2/assets/`) | SUPPLIED EVIDENCE | Seven PNG screenshots of the student's course portal covering Semesters I–VII. Course codes, names, academic year, and credits all match `COURSE_MAP.csv`. Reconciliation documented in `CURRICULUM_SCREENSHOTS.md`. |
| Student clarification (HS301, IP-1/IP-2) | SUPPLIED EVIDENCE | Student instruction: HS301 = 0 credits (confirmed in Semester V screenshot); IP201 is IP-1 (mandatory post-Semester IV internship, 3 credits); IP-2 is the six-month Mandatory Internship-II (15 credits). |
| IFHE Student Portal Registration Records | PRIMARY EVIDENCE | Direct semester-wise course registration portal screenshots (Semesters I–VII) from student records, establishing the actual curriculum baseline for the 2023–2027 batch. |

---

## 2. Job Description Sources

| # | Employer | Role | Evidence File | Access/Read Date | Posting Date | Notes |
|---|---|---|---|---|---|---|
| 1 | ACHNET | Software Engineer (SDE) | `job_descriptions/Detailed Job Description - Tescra.pdf` | 24 Oct 2026 | Not stated in document | On-campus recruitment opportunity. PDF read directly. Full-stack web, OOP, Data Structures, Python, Agile. |
| 2 | JPMorgan Chase & Co. | Data Analyst — Fresher | `job_descriptions/JPMorgan_Chase_Data_Analyst_Fresher.pdf` | 24 Oct 2026 | Not stated in document | On-campus recruitment opportunity. PDF read directly. SQL, Python, Statistics, Excel, Power BI / Tableau, Git. |
| 3 | Joveo | Software Engineering Intern (Full Stack) | `job_descriptions/Joveo_SE_Intern_JD.pdf` | 24 Oct 2026 | 2026 (Forbes badge in document) | On-campus recruitment opportunity. PDF read directly. React, Next.js, Node.js, PostgreSQL, REST API, Git, LLMs. |

---

## 3. Note on Evidence Approach

The three job descriptions used in this submission are genuine on-campus recruitment documents received through college email for campus placement and internship drives (ACHNET, JPMorgan Chase, and Joveo). Skills were extracted directly from the document text using `pypdf` and are not inferred or templated. This ensures practical relevance to actual graduate hiring standards faced by students.

---

## 4. External References Used in Proposal Rationale

| Reference | URL / Citation | Used For |
|---|---|---|
| Fibonacci and memoisation | General CS knowledge; verified against standard recursion theory | AI Exercise 1 verification |
| Stack LIFO definition | Standard data structures textbook knowledge | AI Exercise 2 verification |
| INNER JOIN vs LEFT JOIN | Standard SQL documentation knowledge | AI Exercise 3 verification |
| FCFS scheduling and convoy effect | Standard OS textbook knowledge (e.g., Silberschatz Operating System Concepts) | AI Exercise 4 verification |
| Train/test split and overfitting | Standard ML knowledge (e.g., Mitchell Machine Learning; Goodfellow Deep Learning) | AI Exercise 5 verification |

---

## 5. Tools and Software Used

| Tool | Purpose | Notes |
|---|---|---|
| Claude Sonnet 4.6 (Antigravity IDE) | AI exercises, research assistance, drafting | All use documented in AI_EXERCISES.md |
| pypdf 6.21.2 (Python library) | Extract text from job description PDFs | Used to read all three PDF JDs on 24 Oct 2026 |
| Python 3.11 (local) | Test runner, PDF extraction, data validation | Task2/tests/test_course_explorer.py; 15/15 tests pass |
| GitHub API (https://api.github.com/repos/kanwa2006/hkaiverse/git/trees/main) | Repository structure inspection | Used on 24 Oct 2026 to read file tree |
| PowerShell (local) | Directory creation, file management, git commands | Used to create Task2/ directory structure and commit history |

---

## 6. Credit Calculations

Calculations are documented in full in `CREDIT_CALCULATIONS.md`. Key figures:

| Item | Value |
|---|---|
| Baseline total | 167 credits (student-supplied) |
| Proposed total | 167 credits (balanced) |
| Net credit change | 0 |
| Credits affected (Method A, conservative) | 33 |
| Percentage affected (Method A) | 19.8% |
| HS301 credit value used | 0 (student-supplied instruction) |

---

## 7. Baseline Repository Inspection Record (Historical Context — Pre-Task 2 Ingestion)

| Item | Finding |
|---|---|
| Repository URL | https://github.com/kanwa2006/hkaiverse |
| Inspection date | 24 October 2026 |
| Method | GitHub API (tree endpoint) + raw.githubusercontent.com |
| Branch | main |
| Root files found | README.md, .gitignore, Task1/ directory |
| Task1 files found | README.md, TASK1_REPORT.md, .gitignore, evidence/, prototype/ |
| Task2 directory (pre-development baseline) | Did not exist prior to Task 2 development (subsequently authored, tested, and committed) |
| Task1 preserved | ✓ Not modified |

---

## 8. Evidence Category Key

All evidence in this submission is labelled with one of the following categories (consistent with Task 1):

| Category | Meaning |
|---|---|
| OBSERVED | Directly seen or experienced by the student |
| REPORTED | Verbal accounts from staff, peers, or contacts |
| COMPUTED | Result of arithmetic or algorithmic calculation |
| ASSUMPTION | Reasonable inference not directly verified |
| SYNTHETIC | Artificial data used only for testing or illustration |
| SUPPLIED | Information provided by the student for this report |
| SOURCED | External source accessed and cited |

---

*SOURCES.md | Task 2 | HKAIVERSE Round 2 | 24 October 2026*
