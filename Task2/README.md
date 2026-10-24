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

### Credit changes

| Change type | Courses | Credit effect |
|---|---|---|
| REDUCE | PH101, MG201, HS201 | −3 |
| ADD | CS-NEW Applied Lab | +3 |
| **Net** | | **0** |
| **Baseline total** | All 53 courses | **167 credits** |
| **Proposed total** | | **167 credits** |

### Credits affected

The conservative estimate (Method A) counts the three courses whose credit values change and five courses whose practical content is substantially redesigned:

- Credit-allocation changes (3 REDUCE + 1 ADD): 5 + 3 + 3 + 3 = **14 credits**
- Key UPDATE courses with substantial redesign (CS205, CS206, CS304, DS304, CS101): 4 + 4 + 3 + 4 + 4 = **19 credits**
- **Total affected: 33 / 167 = approximately 20%**

Three calculation methods are compared in [CREDIT_CALCULATIONS.md](CREDIT_CALCULATIONS.md). Method A (~20%) is the most conservative and honest figure.

**Note:** HS301 Constitution of India is shown as 0 credits throughout, following a direct student instruction. A discrepancy between this and the portal screenshot is documented in CREDIT_CALCULATIONS.md.

---

## 5. Evidence from 2026 Job Descriptions

I accessed the career portals of three major employers on **24 October 2026** and reviewed their entry-level software engineering requirements:

| Role | Employer | Skills listed |
|---|---|---|
| Associate Software Engineer | Accenture India | Python or Java, REST APIs, Git, OOP, cloud basics, 60%+ CGPA |
| Software Engineer — Entry Level | IBM India | Python or Java, REST APIs, Git, SQL, Docker, unit testing |
| Software Engineer — Early Career | Cisco India | Java or Python, REST APIs, Git, Docker/Kubernetes, OS and networks fundamentals |

All three roles consistently listed **REST API knowledge**, **Git proficiency**, and **practical coding ability** as requirements. The current curriculum covers the underlying concepts in CS205, CS304, and CS201, but without a hands-on lab that combines them, students may graduate without having practised these skills together.

The portal pages use JavaScript rendering, so individual posting dates were not visible in plain text. Access dates, source URLs, and evidence categories are recorded in [SOURCES.md](SOURCES.md). The full skill-gap analysis is in [JOB_DESCRIPTION_COMPARISON.md](JOB_DESCRIPTION_COMPARISON.md).

**Supplementary:** A Leo Force campus drive announcement (student-supplied screenshot, dated 22 October 2026) shows continued local interest in software engineering freshers. Used as local context only — not a primary source.

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

**Testing status:** 14 manual test cases are documented in [tests/test_checklist.md](tests/test_checklist.md). These cover loading, search, filtering, credit calculations, empty states, and sorting. The test cases were written and their expected results are documented, but the tests have not yet been executed using a browser tool (the automated browser tool was unavailable in this session). A reviewer can run the checklist manually by opening the file in a browser and following the steps.

---

## 9. How I Checked the Work

| Item | What was done | Status |
|---|---|---|
| Credit totals | Added up semester by semester and compared with student-supplied total | ✅ Verified: 167 baseline, 167 proposed, net 0 |
| Three calculation methods | Conservative, full-UPDATE, and partial-UPDATE methods compared | ✅ Documented in CREDIT_CALCULATIONS.md |
| Job description sources | Career pages accessed on 24 Oct 2026; URLs and access dates recorded | ✅ Sourced; posting dates not readable (JS pages) |
| AI exercises (5 subjects) | Prompts submitted, outputs recorded, manually verified against known answers | ✅ All 5 verified; corrections documented |
| HS301 credit value | Set to 0 in all files per student instruction | ✅ Consistent across explorer and all documents |
| IP-2 course code | Left as "to be confirmed" | ⚠️ Not confirmed |
| Task 1 files | Checked with `git diff Task1/` — no changes | ✅ Preserved unchanged |
| Course explorer tests | Test cases written and expected results documented | ⚠️ Not yet executed (pending manual run) |
| IFHE official curriculum PDF | Attempted to access IFHE/ICFAITech website | ❌ Not accessible; dataset remains student-supplied |

---

## 10. Limitations

**What could not be verified:**
- Official IFHE curriculum PDF for the 2023–2027 batch — the website was not accessible during this session. The course dataset is student-supplied and provisional.
- HS301 official credit value — a discrepancy exists between the student-supplied instruction (0 credits) and the portal screenshot. Not resolved against official records.
- IP-2 course code — not confirmed from available sources.
- Individual posting dates for Accenture, IBM, Cisco listings — not readable in plain text due to JavaScript rendering.

**What requires institutional approval before any implementation:**
- All three REDUCE proposals need curriculum committee approval and syllabus revision.
- CS-NEW needs a new course code, full syllabus, faculty assignment, timetabling, and academic approval.
- Any change to the assessment weighting (60/40 practical/theory split) requires review under IFHE examination regulations.

**What remains to be done for a complete submission:**
- Execute the 14 manual course explorer tests and update the checklist with actual pass/fail results.
- Obtain the official curriculum PDF and verify the course list against it.
- Create a named GitHub release and update the root README with the release URL.

---

## 11. Project Structure

```
Task2/
├── README.md                        ← This file — entry point
├── CURRICULUM_AUDIT.md              ← Full course map, 12 redesign reasons, all decisions
├── COURSE_MAP.csv                   ← Machine-readable: all 53 courses with proposed actions
├── CREDIT_CALCULATIONS.md           ← Three calculation methods; baseline = proposed = 167 cr
├── JOB_DESCRIPTION_COMPARISON.md   ← Three 2026 job descriptions vs. existing courses
├── AI_EXERCISES.md                  ← Five AI-assisted exercises with prompts, verification
├── LAB_CAPSTONE_PROPOSAL.md        ← Full lab proposal: outcomes, schedule, tests, rubric
├── FEEDBACK_AND_LIMITATIONS.md     ← Feedback, personal contribution, known limitations
├── SOURCES.md                       ← All source URLs, access dates, evidence categories
├── course_explorer.html             ← Interactive course explorer (open in browser)
└── tests/
    └── test_checklist.md            ← 14 manual tests for explorer + consistency checks
```

---

## 12. Final Summary

**Problem:** Students may complete a CS degree understanding individual topics well — programming, databases, web, networks — without having practised building a complete application that connects them. This can make the start of a software engineering job more difficult than it needs to be.

**Proposal:** Retain all core CS fundamentals. Add practical exercises to nine existing courses (no credit change). Reduce three low-CS-relevance courses by one credit each and use those three credits to fund a new Applied Software Product Engineering Lab where students build, test, document, and demonstrate a complete small application.

**Evidence:** Three real 2026 job descriptions from Accenture, IBM, and Cisco all require REST APIs, Git, and practical programming — skills the curriculum teaches individually but does not currently provide an integrated opportunity to practise. Two informal conversations with a graduate and a faculty member both supported the general direction.

**What was completed and verified:** Credit calculations (167 → 167, ~20% affected), all 11 Task 2 documents, five AI-assisted exercises with manual verification, one interactive course explorer, and one detailed lab proposal with five acceptance tests. Task 1 preserved unchanged.

**Key limitations:** The course dataset is student-supplied and not verified against the official IFHE PDF. The explorer test cases are documented but not yet executed. The REDUCE and ADD proposals require formal academic approval before any implementation. This is a student proposal, not an approved or enacted policy change.

---

*Participant: kanwa2006 · HKAIVERSE Round 2, Task 2 · 24 October 2026*
*All prototype data is synthetic. No real student names, IDs, marks, or private records are included.*
