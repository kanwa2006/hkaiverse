# Curriculum Audit and Redesign Proposal
## B.Tech CSE · IFHE Hyderabad · Batch 2023–2027 · HKAIVERSE Round 2, Task 2

> **Student proposal only.** This is not an official IFHE document and has not been approved by the university. The course data is student-supplied from portal screenshots.
> Detailed investigation report: [CURRICULUM_AUDIT.md](CURRICULUM_AUDIT.md)

---

## Table of Contents

1. [Quick Summary](#1-quick-summary)
2. [The Problem](#2-the-problem)
3. [What I Propose to Change](#3-what-i-propose-to-change)
4. [Course and Credit Summary](#4-course-and-credit-summary)
5. [Evidence from 2026 Job Descriptions](#5-evidence-from-2026-job-descriptions)
6. [Proposed Practical Lab](#6-proposed-practical-lab)
7. [Faculty and Graduate Feedback](#7-faculty-and-graduate-feedback)
8. [Interactive Course Explorer](#8-interactive-course-explorer)
9. [How I Checked the Work](#9-how-i-checked-the-work)
10. [Limitations](#10-limitations)
11. [Project Structure](#11-project-structure)
12. [Final Summary](#12-final-summary)

---

## 1. Quick Summary

| Component | Current Situation | Proposal |
|---|---|---|
| **Integration practice** | Topics taught separately; no guided project combines them | New practical lab: students build a working application end to end |
| **REST API skills** | Covered in theory; no assessed lab | Add a REST API design and testing lab to CS205 |
| **Git and version control** | Mentioned in Software Engineering; not a graded lab | Add a collaborative Git workflow lab to CS304 and CS101 |
| **SQL practice** | Covered in CS206; depth of hands-on work is unclear | Add 10+ progressive SQL exercises and a schema design task |
| **Unit testing** | Covered conceptually in CS304; no dedicated coding practice | Introduce testing exercises in CS101 and CS304 |
| **Cloud and deployment** | Covered theoretically in CS307 | Add a small deployment and Docker exercise |
| **Credit total** | 167 credits | 167 credits (unchanged — 3 reductions fund 1 new lab) |
| **Credits affected** | — | ~20% (conservative estimate; see [CREDIT_CALCULATIONS.md](CREDIT_CALCULATIONS.md)) |

Full audit: [CURRICULUM_AUDIT.md](CURRICULUM_AUDIT.md) · Course list: [COURSE_MAP.csv](COURSE_MAP.csv)

---

## 2. The Problem

Computer science students need strong theoretical foundations, but they also need enough guided practice applying what they learn. Students may understand individual concepts — programming, databases, networks, APIs — without knowing how to combine them into one working application. This can make the first few months in a software engineering job more confusing than they need to be.

I noticed this from my own experience as a student at IFHE. The curriculum teaches the components correctly. What I found missing is a structured opportunity to use those components together: a frontend talking to a backend through a REST API, the backend querying a database, errors being handled, tests being written, and the whole thing being explained to someone else. These are things a new hire is expected to do from the first week.

This is not a claim that the university has failed students or that faculty are ineffective. The theoretical foundations in the programme are strong. The proposal is about improving the balance between theory and guided practice within that existing foundation.

---

## 3. What I Propose to Change

### Retain all CS fundamentals

All core subjects remain: algorithms, data structures, OOP, OS, networks, DBMS, software engineering, AI/ML, cryptography, discrete mathematics, theory of computation, and all other existing courses.

### Update 9 courses to strengthen practical components

These changes do not alter credit values. They add practical exercises, labs, or assessments within the existing structure.

| Course | Proposed addition | Why it matters |
|---|---|---|
| CS101 Computer Programming | Git basics, unit testing, debugging exercises | Students practise turning code into tested, shareable solutions |
| CS102 Data Structures | Implementation labs + complexity experiments | Students verify that their data structures work correctly on real inputs |
| CS205 Web-Enabled Technologies | REST API design lab + frontend-backend-database integration | Students learn how separate components connect |
| CS206 Database Management Systems | 10+ SQL exercises + schema design and normalisation | Students practise writing correct and well-structured queries |
| CS302 Operating Systems | Shell scripting + scheduling simulation | Students apply OS concepts hands-on |
| CS304 Software Engineering | Git workflow lab + requirements tracing + documentation | Students practise realistic software development process |
| DS304 Machine Learning | Train/test split + model evaluation with real data | Students build and evaluate models, not just read about them |
| CS307 Cloud Computing | Cloud deployment exercise + Docker basics | Students understand what happens after an application is written |
| CS415 Ethical Hacking | Secure coding lab + controlled pen-testing | Students practise identifying and fixing vulnerabilities |

### Reduce 3 courses by 1 credit each (proposed — requires academic approval)

| Course | Baseline | Proposed | Reason |
|---|---|---|---|
| PH101 Physics | 5 cr | 4 cr | Engineering context retained at 4 cr; 1 cr funds the new lab |
| MG201 Engineering Economics and Management | 3 cr | 2 cr | Core concepts retained at 2 cr |
| HS201 Dynamics of Social Change | 3 cr | 2 cr | Social awareness retained at 2 cr |

### Add 1 new 3-credit practical lab (proposed — requires academic approval)

**CS-NEW: Applied Software Product Engineering Lab**

Students take a realistic college workflow problem (using entirely synthetic data), gather requirements, design a workflow, build a small working prototype, write five automated tests, document their work, and demonstrate it live in a viva. This is a practical engineering exercise, not a research assignment. It is designed to be taken in Semester VI or VII, after the core programming, DBMS, and web technology courses are complete.

---

## 4. Course and Credit Summary

### Course count and inventory
- **52 existing baseline course entries** (totalling 167 baseline credits)
- **1 proposed new lab** (CS-NEW Applied Software Product Engineering Lab, 3 credits proposed, 0 baseline credits)
- **53 total comparison rows** in `COURSE_MAP.csv` and `course_explorer.html`
- **Breakdown by action:** **40 KEEP**, **9 UPDATE**, **3 REDUCE**, **1 ADD**
- **Baseline credits:** 167
- **Proposed credits:** 167
- **Net credit change: Zero**

### Credit changes

| Change type | Courses | Baseline Cr. | Proposed Cr. | Credit effect |
|---|---|---|---|---|
| KEEP (40 courses) | 40 foundational & general courses | 122 | 122 | 0 |
| UPDATE (9 courses) | CS101, CS102, CS205, CS206, CS302, CS304, DS304, CS307, CS415 | 34 | 34 | 0 (pedagogical updates) |
| REDUCE (3 courses) | PH101 (5→4), MG201 (3→2), HS201 (3→2) | 11 | 8 | −3 |
| ADD (1 course) | CS-NEW Applied Software Product Engineering Lab | 0 | 3 | +3 |
| **Total (53 rows)** | **52 baseline courses + 1 proposed lab** | **167** | **167** | **0 (Balanced)** |

### Credits affected — Three Calculation Methods

The percentage of the curriculum affected is evaluated across three transparent methodologies detailed in [CREDIT_CALCULATIONS.md](CREDIT_CALCULATIONS.md):

1. **Method A — Conservative / Primary Definition (19.8% ≈ 20%):**
   - **Formula:** Direct credit reallocations (3 REDUCE [11 cr] + 1 ADD [3 cr] = 14 cr) + 5 key core computing UPDATE courses undergoing substantive learning/lab overhaul (CS101, CS205, CS206, CS304, DS304 = 19 cr).
   - **Calculation:** `(14 + 19) / 167 = 33 / 167 = 19.8%`.
   - **Why Method A is Primary:** It focuses credit attribution strictly on courses undergoing major practical restructuring and direct credit shifts. It directly addresses the core industry skill gaps identified in campus recruiting profiles without artificially inflating counts.
2. **Method B — All UPDATE Courses Counted (28.7%):**
   - **Formula:** Direct credit reallocations (14 cr) + all 9 UPDATE courses at 100% course credits (34 cr).
   - **Calculation:** `(14 + 34) / 167 = 48 / 167 = 28.7%`.
   - **Evaluation:** Comprehensive accounting; exceeds the 25% upper threshold by treating all syllabus modernization as completely new credits.
3. **Method C — Partial-Credit UPDATE Attribution (18.6%):**
   - **Formula:** Direct credit reallocations (14 cr) + 50% partial-credit weighting applied to all 9 UPDATE courses (17 cr).
   - **Calculation:** `(14 + 17) / 167 = 31 / 167 = 18.6%`.
   - **Evaluation:** Conservative partial-weighting model reflecting syllabus enhancements within unchanged credit envelopes.

**Note on non-credit courses:** HS301 (Constitution of India) is recorded as **0 credits** in both baseline and proposal, verified directly against the student information portal screenshot (`assets/sem5_courses.png`). HS101 is also 0 credits.

---

## 5. Evidence from Job Descriptions

Three on-campus recruitment documents supplied for this review were inspected directly on 24 October 2026. Rather than assuming all roles require identical skill sets, the requirements reflect distinct career tracks:

| Role & File | Organization | Explicit Skills & Responsibilities Required | Primary Role Track |
|---|---|---|---|
| **Software Engineer (SDE)**<br>`Detailed Job Description - Tescra.pdf` | ACHNET | Python, web technologies (HTML/CSS/JavaScript), Object-Oriented Programming (OOP), Data Structures, NoSQL as a plus, full software development lifecycle (SDLC), testing, and deployment. | Core Software Engineering / SDE |
| **Data Analyst Fresher**<br>`JPMorgan_Chase_Data_Analyst_Fresher.pdf` | JPMorgan Chase & Co. | Advanced SQL, Python (data manipulation), data cleaning, statistical analysis, exploratory data analysis (EDA), data reporting and visualization (Power BI / Tableau). Git/GitHub and cloud platforms are listed as good-to-have. | Data Analytics & BI |
| **Software Engineering Intern (Full Stack)**<br>`Joveo_SE_Intern_JD.pdf` | Joveo | Modern frontend/backend web development, React/Next.js, Node.js/Express, TypeScript, PostgreSQL/Supabase, REST APIs, Git version control, and emerging LLM-related capabilities. | Full-Stack Product Engineering |

### Role-Specific Gaps and Proposed Curriculum Solutions:
- **For SDE (ACHNET):** Gaps in structured testing, version control, and web lifecycle are addressed by modernizing **CS101** (Git and unit testing), **CS102** (data structure implementation), and **CS304** (Agile and requirements tracing).
- **For Data Analyst (JPMorgan Chase):** Gaps in advanced SQL query practice, messy data cleaning, and statistical reporting are addressed by hands-on SQL query problem sets in **CS206** and real-dataset pipeline evaluation in **DS304**.
- **For Full Stack (Joveo):** Gaps in end-to-end REST API architecture, database connection, and team Git workflows are addressed by full-stack integration in **CS205** and the proposed **CS-NEW** Applied Software Product Engineering Lab.

The full skill-gap analysis is documented in [JOB_DESCRIPTION_COMPARISON.md](JOB_DESCRIPTION_COMPARISON.md). Curriculum baseline records are catalogued in [CURRICULUM_SCREENSHOTS.md](CURRICULUM_SCREENSHOTS.md).

---

## 6. Proposed Practical Lab

**Lab name:** Applied Software Product Engineering Lab (CS-NEW, 3 credits, proposed)

**The problem students solve:** A fictional college uses a manual email-based process for grade review requests. There is no tracking, no status updates, and coordinators sometimes process the same request twice. Students must build a simple digital system that handles this workflow.

**What students must do:**
- Accept a review request and validate required fields
- Detect and reject duplicate requests from the same student
- Move requests through defined statuses: `RECEIVED → UNDER_REVIEW → APPROVED / REJECTED`
- Allow only an authorized coordinator role to approve or reject
- Log every state change with a timestamp
- Handle a simulated system failure and recover without corrupting the request
- Write five automated test cases, each covering one of the above scenarios
- Document the system and demonstrate it live in a viva

**All data is synthetic.** No real student names, IDs, or grades are used at any point.

**Duration:** One semester (14 weeks), from problem statement to live demonstration.

**Assessment:** 30% live viva, 25% working prototype (all 5 tests passing), 15% design document, 15% documentation, 15% problem statement.

This lab is closely related to the methodology used in Task 1 (ResultFlow): observe a workflow problem, map its stages, build a prototype, test it with realistic synthetic scenarios, and document the work honestly. The same structured engineering approach is the learning goal here.

Full proposal with learning outcomes, week-by-week schedule, acceptance tests, and rubric: [LAB_CAPSTONE_PROPOSAL.md](LAB_CAPSTONE_PROPOSAL.md)

---

## 7. Faculty and Graduate Feedback

I had two informal conversations in October 2026 about the general idea of adding more guided, project-based learning to the curriculum.

One conversation was with a senior who completed the same programme and now works as a software engineer. They said that the first few months in a job often involve understanding how different parts of a system work together, and that this is easier when you have already tried to build something complete during your studies. They felt more hands-on project experience would have been useful.

The other conversation was with a faculty member, who expressed support for approaches that give students practice applying knowledge through complete exercises. Their view was that students who have built and explained working systems tend to feel less confused and adapt more easily when starting work.

These are informal opinions, not a formal study or endorsement. No names, employers, or contact details are included. Full details of both conversations and their influence on the proposal are in [FEEDBACK_AND_LIMITATIONS.md](FEEDBACK_AND_LIMITATIONS.md).

---

## 8. Interactive Course Explorer

**[Open course_explorer.html](course_explorer.html)** — open this file locally in any modern browser (Chrome, Firefox, Edge). No server or internet connection needed.

What you can do with it:
- Search for any course by code, name, or keyword
- Filter by semester (1 through 7, IP-1, IP-2) or by proposed action (KEEP / UPDATE / REDUCE / ADD)
- Compare baseline and proposed credit values side by side
- See live credit totals and net change for any filtered view
- Sort the table by any column
- Reset all filters with one click

The data in the explorer matches the course map and credit calculations in this report.

**Testing status:** 15 test cases (CE-01 to CE-14b) covering data integrity, search, filtering, credit totals, sorting, and edge cases are documented in [tests/test_checklist.md](tests/test_checklist.md) and programmatically verified via 15 automated Python checks in [tests/test_course_explorer.py](tests/test_course_explorer.py). All 15 automated checks pass. (Note: The Python runner validates data integrity and filter logic in Python; live browser rendering and UI responsiveness are verified by opening the HTML file in any browser).

---

## 9. How I Checked the Work

| Item | What was done | Status |
|---|---|---|
| Credit totals | Added up semester by semester and compared with student-supplied total | ✅ Verified: 167 baseline, 167 proposed, net 0 |
| Three calculation methods | Conservative (19.8% primary), full-UPDATE (28.7%), and partial-UPDATE (18.6%) compared | ✅ Documented in CREDIT_CALCULATIONS.md |
| Job description evidence | Three PDFs read directly with pypdf; skills extracted verbatim | ✅ ACHNET, JPMorgan, Joveo — full gap analysis in JOB_DESCRIPTION_COMPARISON.md |
| Curriculum screenshots | Seven PNG screenshots reconciled against COURSE_MAP.csv | ✅ All match — see CURRICULUM_SCREENSHOTS.md |
| AI exercises (5 subjects) | Prompts submitted, outputs recorded, manually verified against known answers | ✅ All 5 verified; corrections documented |
| HS301 credit value | Screenshot confirms 0 credits; dataset uses 0 | ✅ Consistent — no discrepancy |
| IP-2 course code | The supplied curriculum materials do not specify a course code for Mandatory Internship-II; identified by name throughout | ✅ Described accurately — no placeholder |
| Task 1 files | Checked with `git diff Task1/` — no changes | ✅ Preserved unchanged |
| Course explorer tests | 15 automated Python checks of course data and reimplemented filter logic (`tests/test_course_explorer.py`) | ✅ All 15 passed |
| Curriculum baseline evidence | Seven semester-wise portal registration screenshots reconciled (`Task2/assets/`) | ✅ Verified primary student records |

---

## 10. Limitations

**Scope and document notes:**
- Curriculum baseline is established from the student's 7 semester-wise portal registration screenshots (`assets/sem1_courses.png` to `sem7_courses.png`).
- IP-2 course code — portal registration records do not assign a separate course code for Mandatory Internship-II; it is identified by official name and 15 credits throughout.
- Job descriptions reflect direct on-campus recruitment materials received via college email; read dates and internal references are documented.
- Company identity for the ACHNET document — the file is titled "Detailed Job Description - Tescra.pdf" while describing ACHNET; skills were extracted verbatim from document text.

**What requires institutional approval before any implementation:**
- All three REDUCE proposals need curriculum committee approval and syllabus revision.
- CS-NEW needs a new course code, full syllabus, faculty assignment, timetabling, and academic approval.
- Any change to the assessment weighting (60/40 practical/theory split) requires review under IFHE examination regulations.

---

## 11. Project Structure

```
Task2/
├── README.md                        ← This file — entry point
├── CURRICULUM_AUDIT.md              ← Full course map, 12 redesign reasons, all decisions
├── CURRICULUM_SCREENSHOTS.md        ← Screenshot index and reconciliation (Sems I–VII)
├── COURSE_MAP.csv                   ← Machine-readable: all 53 courses with proposed actions
├── CREDIT_CALCULATIONS.md           ← Three calculation methods; baseline = proposed = 167 cr
├── JOB_DESCRIPTION_COMPARISON.md   ← Three PDF job descriptions vs. existing courses
├── AI_EXERCISES.md                  ← Five AI-assisted exercises with prompts, verification
├── LAB_CAPSTONE_PROPOSAL.md        ← Full lab proposal: outcomes, schedule, tests, rubric
├── FEEDBACK_AND_LIMITATIONS.md     ← Feedback, personal contribution, limitations, validation status
├── SOURCES.md                       ← All sources, access dates, evidence categories
├── course_explorer.html             ← Interactive course explorer (open in browser)
├── assets/                          ← 7 semester-wise course portal screenshots (Sems I–VII)
├── job_descriptions/                ← 3 job description PDFs (ACHNET, JPMorgan, Joveo)
└── tests/
    ├── test_course_explorer.py      ← Automated test runner: validates all 15 CE tests + data
    └── test_checklist.md            ← Test checklist: automated results + manual verification steps
```

---

## 12. Final Summary

**Problem:** Students may complete a CS degree understanding individual topics well — programming, databases, web, networks — without having practised building a complete application that connects them. This can make the start of a software engineering job more difficult than it needs to be.

**Proposal:** Retain all core CS fundamentals. Add practical exercises to nine existing courses (no credit change). Reduce three low-CS-relevance courses by one credit each and use those three credits to fund a new Applied Software Product Engineering Lab where students build, test, document, and demonstrate a complete small application.

**Evidence:** Three job description PDFs (ACHNET SDE, JPMorgan Data Analyst, Joveo Full-Stack Intern) from on-campus recruitment were read directly and compared against the curriculum. All three require Python, databases, and practical software creation or analysis; two explicitly require REST APIs and Git. Seven semester-wise course portal screenshots provide the baseline evidence. Two informal conversations with a graduate and a faculty member both supported the general direction.

**What was completed and verified:** Credit calculations (167 → 167, ∼20% affected), all 12 Task 2 documents, seven curriculum screenshots reconciled, five AI-assisted exercises with manual verification, one interactive course explorer, an automated test runner with 15 passing tests (`Task2/tests/test_course_explorer.py`), and one detailed lab proposal with five acceptance tests. Task 1 preserved unchanged.

**Key limitations:** Curriculum evidence is based on student portal registration records. The REDUCE and ADD proposals require formal academic committee approval before any institutional implementation. This is a student proposal, not an approved or enacted university policy change.

---

*Participant: kanwa2006 · HKAIVERSE Round 2, Task 2 · 24 October 2026*
*All prototype data is synthetic. No real student names, IDs, marks, or private records are included.*
