# Task 2 — Curriculum Audit and Redesign
## HKAIVERSE Round 2 | B.Tech CSE, IFHE Hyderabad | Batch 2023–2027

> **Quick orientation for a reviewer:** This README is the entry point for Task 2. The course explorer, detailed audit, credit calculations, job evidence, and lab proposal are all linked below. Task 1 (ResultFlow) is in the `Task1/` folder and is not changed.

---

## 1. The Problem

Computer science students need strong theoretical foundations, but they also need regular opportunities to apply what they learn. When practical work is limited to individual exercises, students may understand separate concepts without knowing how to combine them into a complete application. This can make the transition from university to a software engineering job more difficult.

I noticed this from my own experience as a student. We learn programming, data structures, databases, networks, and software engineering — but not always in the same project, and not always in a way that shows how they connect. A frontend communicates with a backend through an API; the backend queries a database; errors are handled; the whole thing is tested and deployed. Understanding each piece separately is not the same as being able to build the system.

The curriculum should retain essential fundamentals while providing more guided, project-based learning, current industry tools, practical assessments, and opportunities to build and explain complete software systems.

---

## 2. Why This Matters

When a student starts their first engineering job, they are often asked to:
- Build or extend a feature that spans a frontend, an API, and a database.
- Debug something they have never seen before.
- Write a test for their own code.
- Push their changes to a shared repository and not break the build.
- Explain what they built and why they made certain choices.

These tasks use skills that are technically in the curriculum — but they may never have been practised together in a single assessed project. The result is that students who know the theory well can still feel confused and underprepared at the start of a job.

This is not an accusation that the university or faculty are ineffective. The theoretical foundations in the programme are strong. The proposal is about adding more structured practice using those foundations.

---

## 3. What I Propose to Change

### Keep everything important
All core CS subjects are retained: algorithms, data structures, OOP, OS, networks, DBMS, software engineering, AI/ML, cryptography, discrete mathematics, theory of computation.

### Update 9 courses to add practical components
| Course | What I propose to add |
|---|---|
| CS101 Computer Programming | Git basics, unit testing, debugging exercises |
| CS102 Data Structures | Implementation labs + complexity experiments |
| CS205 Web-Enabled Technologies | REST API design lab + frontend-backend-database integration |
| CS206 Database Management Systems | SQL practice + transactions + schema design |
| CS302 Operating Systems | Shell scripting + process scheduling simulation |
| CS304 Software Engineering | Git workflow lab + requirements tracing + documentation |
| DS304 Machine Learning | Practical model building + train/test evaluation |
| CS307 Cloud Computing | Cloud deployment lab + Docker basics |
| CS415 Ethical Hacking | Secure coding lab + basic pen-testing |

### Reduce 3 courses by 1 credit each (proposed, requires approval)
- PH101 Physics: 5 → 4 credits
- MG201 Engineering Economics and Management: 3 → 2 credits
- HS201 Dynamics of Social Change: 3 → 2 credits

### Add 1 new 3-credit practical lab (proposed, requires approval)
**CS-NEW: Applied Software Product Engineering Lab** — students build a complete small application through the full engineering process: requirements → design → implementation → testing → documentation → live demonstration.

**Net credit change: 0. Total remains 167 credits.**

---

## 4. Examples of Current Subjects and Proposed Improvements

### CS205 — Web-Enabled Technologies (UPDATE)
*Current (student observation):* Covers web concepts and technologies.  
*Proposed addition:* A 3-endpoint REST API lab where students design an API, implement it in Python (Flask or FastAPI), connect it to a SQLite database, and test it with curl. The lab requires students to handle a missing-field error and a duplicate-request scenario.

### CS206 — Database Management Systems (UPDATE)
*Current (student observation):* Covers DBMS concepts and SQL.  
*Proposed addition:* 10+ written SQL queries progressing from simple SELECT to JOIN, aggregation, and transaction management. A schema normalisation exercise where students redesign a flawed table to 3NF.

### CS304 — Software Engineering (UPDATE)
*Current (student observation):* Covers software engineering principles.  
*Proposed addition:* A Git workflow lab (branch, merge conflict, pull request) done in pairs. A requirements-tracing exercise. A one-page design document for a feature with a justification of design choices.

### CS-NEW — Applied Software Product Engineering Lab (ADD)
Students are given a realistic college workflow problem (grade review requests — using entirely synthetic data). They must gather requirements, design a workflow, build a small working prototype, write five automated test cases, document their work, and demonstrate it live. This is not a research project — it is a practical engineering exercise.

---

## 5. Credit-Change Summary

| Change | Courses | Credits |
|---|---|---|
| REDUCE | PH101, MG201, HS201 | −3 |
| ADD | CS-NEW Applied Lab | +3 |
| **Net** | | **0** |
| **Baseline total** | | **167** |
| **Proposed total** | | **167** |

Credits affected (Method A, conservative): **33 / 167 = ~19.8%** (approximately 20%).  
Full calculation with three methods: [`CREDIT_CALCULATIONS.md`](CREDIT_CALCULATIONS.md)

*HS301 Constitution of India is shown as 0 credits per student instruction. The screenshot shows a different value — this discrepancy is documented in CREDIT_CALCULATIONS.md.*

---

## 6. Evidence from 2026 Job Descriptions

I researched entry-level software engineering job postings from three employers with career pages accessed on 24 October 2026:

| Role | Employer | Top Skill Gaps vs. Current Curriculum |
|---|---|---|
| Associate Software Engineer | Accenture India | REST API hands-on lab; Git-based collaboration |
| Software Engineer (Entry) | IBM India | SQL practice; unit testing; Git |
| Software Engineer (Early Career) | Cisco India | REST API; cloud/Docker; full-stack integration |

Every role listed REST APIs, Git, and practical language proficiency (Java or Python) as requirements. The current curriculum teaches the individual components; the proposed changes give students practice combining them.

Campus drive supplement: A Leo Force campus drive announcement dated **22 October 2026** (student-supplied screenshot) confirms continued local industry interest in software engineering freshers. Used as supplementary local context only.

Full comparison table: [`JOB_DESCRIPTION_COMPARISON.md`](JOB_DESCRIPTION_COMPARISON.md)

---

## 7. Practical Lab/Capstone Proposal

**Lab name:** Applied Software Product Engineering Lab (CS-NEW, 3 credits)  
**Problem:** Students design and build a small workflow system (grade review request tracker) using synthetic data. They must handle duplicate inputs, missing fields, unauthorized access, and failed steps — and test all five scenarios.

**Learning outcomes:** Requirement writing → workflow design → REST API implementation → database interaction → automated testing → documentation → live demonstration.

**Duration:** One semester (14 weeks).  
**Assessment:** 30% live viva, 25% working prototype, 15% design document, 15% documentation, 15% problem statement.

Full proposal: [`LAB_CAPSTONE_PROPOSAL.md`](LAB_CAPSTONE_PROPOSAL.md)

---

## 8. Faculty and Graduate Feedback

I had two informal conversations about this proposal — one with a senior who works as a software engineer in the IT industry, and one with a faculty member.

Both were supportive of the general direction. The industry contact said that having more experience building complete systems during university would have been useful — the early months of a job involve understanding how different parts of a system work together, and that is easier when you have done it before. The faculty member made a similar point: students who have practised applying their knowledge tend to feel less confused when they start work and adapt more easily to real tasks.

These are informal opinions on a general idea. They are not formal endorsements, and no names or contact details are included. Full details and the influence on the proposal: [`FEEDBACK_AND_LIMITATIONS.md`](FEEDBACK_AND_LIMITATIONS.md)

---

## 9. Interactive Course Explorer

📊 **[Open course_explorer.html](course_explorer.html)** — works locally in any modern browser, no server needed.

Features:
- Search by code, name, or keyword
- Filter by semester or action (KEEP / UPDATE / REDUCE / ADD)
- Live baseline and proposed credit totals
- Net change and percentage-affected display
- Sortable columns
- Empty state for no results
- Reset button

All data in the explorer matches this report exactly.

---

## 10. How the Work Was Checked

- Credit totals independently recalculated and match the student-supplied expected total of 167.
- Three credit-calculation methods compared (conservative, full UPDATE, partial UPDATE).
- Job description sources accessed on 24 October 2026 and their URLs recorded.
- AI exercises conducted on 24 October 2026; outputs verified manually against known correct answers.
- Course explorer tested manually against the checklist in `tests/test_checklist.md`.
- HS301 shown as 0 credits in both the explorer and all documents.
- IP-2 course code left as "to be confirmed."
- Task 1 files preserved unchanged (verified via GitHub API and local directory inspection).

---

## 11. Limitations and Next Steps

**What I could not verify:**
- Official batch-specific curriculum PDF for 2023–2027 (IFHE site not accessible)
- HS301 credit value in official records (discrepancy between screenshot and supplied instruction)
- IP-2 course code
- Individual posting dates for Accenture, IBM, Cisco listings (JavaScript-rendered pages)

**What requires approval before implementation:**
- All three REDUCE proposals need curriculum committee approval
- CS-NEW lab needs full academic approval: course code, syllabus, faculty, timetabling
- Assessment pattern changes need review under IFHE examination regulations

**Possible next steps:**
- Request official curriculum PDF from the academic office
- Run a small structured survey of recent graduates comparing practical confidence vs. curriculum experience
- Pilot the Git workflow lab and REST API lab within existing CS304 and CS205 before proposing formal changes

---

## 12. Links to Detailed Documents

| Document | Description |
|---|---|
| [`CURRICULUM_AUDIT.md`](CURRICULUM_AUDIT.md) | Full course map, 12 reasons for redesign, KEEP/UPDATE/REDUCE/ADD decisions, prerequisite table |
| [`COURSE_MAP.csv`](COURSE_MAP.csv) | Machine-readable course list with all proposed actions |
| [`CREDIT_CALCULATIONS.md`](CREDIT_CALCULATIONS.md) | Transparent credit calculation with three methods |
| [`JOB_DESCRIPTION_COMPARISON.md`](JOB_DESCRIPTION_COMPARISON.md) | Three 2026 job descriptions compared to existing courses |
| [`AI_EXERCISES.md`](AI_EXERCISES.md) | Five AI-assisted exercises with prompts, outputs, verification, and corrections |
| [`LAB_CAPSTONE_PROPOSAL.md`](LAB_CAPSTONE_PROPOSAL.md) | Full lab proposal with milestones, acceptance tests, and rubric |
| [`FEEDBACK_AND_LIMITATIONS.md`](FEEDBACK_AND_LIMITATIONS.md) | Graduate and faculty feedback, personal contribution, limitations |
| [`SOURCES.md`](SOURCES.md) | All sources, access dates, and evidence categories |
| [`course_explorer.html`](course_explorer.html) | Interactive course explorer (open in browser) |
| [`tests/test_checklist.md`](tests/test_checklist.md) | Manual test instructions for course explorer and report consistency |

---

*Task 2 README | HKAIVERSE Round 2 | Participant: kanwa2006 | 24 October 2026*  
*All prototype data is synthetic. No real student names, IDs, marks, fees, credentials, or private messages are included.*
