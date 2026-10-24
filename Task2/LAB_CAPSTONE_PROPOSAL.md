# Lab / Capstone Proposal: Applied Software Product Engineering Lab
## Based on the ResultFlow Project Context — HKAIVERSE Round 2, Task 2

> **Important distinction:** Task 1 (ResultFlow) is a completed project and is preserved unchanged. This document proposes a new practical lab activity *inspired by* the ResultFlow context — it is a curriculum recommendation, not a repeat of Task 1. The Task 1 files are not modified by this document.
>
> This lab has not been approved by IFHE. It is a student proposal only.

---

## 1. Proposed Lab Name

**Applied Software Product Engineering Lab (CS-NEW)**  
Proposed credit value: **3 credits**  
Proposed semester placement: Semester VI or VII (after CS304 Software Engineering and CS206 DBMS)

---

## 2. Problem Statement

Computer science students often graduate having studied software engineering principles — requirements, design, testing, deployment — as separate, sequential topics in separate courses. In a first job, they are expected to combine these skills on a single real problem.

This lab asks students to do exactly that. Starting from an unstructured, real-sounding college workflow problem — similar to the result-publication delay investigated in Task 1 — students will gather requirements, design a workflow, build a small working prototype, test it with realistic scenarios, and document their work as a complete product deliverable.

The lab is not a research project. It is an engineering exercise. Students are expected to produce a working piece of software, explain its design decisions, and show that it handles errors, missing inputs, and edge cases.

---

## 3. Learning Outcomes

By the end of this lab, a student should be able to:

1. **Identify and document a problem** — distinguish what is observed from what is assumed; write a clear problem statement.
2. **Map a workflow** — define steps, ownership, statuses, and decision points in a process.
3. **Write requirements** — translate a problem into functional requirements that can be tested.
4. **Design a system** — choose appropriate data structures, database schema, and API contracts for a small application.
5. **Build a working prototype** — implement a backend with at least one REST endpoint, a database interaction, and a user-facing output (CLI or simple web UI).
6. **Test the system** — write at least five automated test cases covering normal flow, edge cases, duplicate inputs, and error recovery.
7. **Document the work** — produce a README, an evidence log (distinguishing observations from assumptions), and a brief impact estimate.
8. **Demonstrate individual understanding** — explain design decisions and trade-offs in a live review or viva.

---

## 4. Problem Domain: Workflow Transparency in a College Process

The scenario is drawn from the same general context as Task 1 but uses entirely synthetic data.

**Scenario:** A fictional college uses a manual, email-based process for students to request grade reviews after an exam. The process has no tracking, no status updates, and no way for a student to know whether their request was received, is being processed, or has been rejected. Coordinators sometimes process the same request twice.

Students must propose and build a simple digital workflow system that:
- Accepts a request (with required fields: student ID, subject, reason, semester).
- Validates the input and identifies missing or duplicate requests.
- Moves the request through defined statuses: `RECEIVED → UNDER_REVIEW → APPROVED / REJECTED`.
- Allows only an authorized role to approve or reject.
- Logs each state change with a timestamp.
- Provides a query endpoint to check request status.
- Handles failure gracefully (e.g., what happens if the approval step fails?).

All data is synthetic. No real student IDs, names, grades, or personal information are used at any point.

---

## 5. Duration

**Proposed duration:** One academic semester (12–14 weeks), run alongside other Semester VI or VII courses.

| Week | Activity |
|---|---|
| 1–2 | Problem framing, evidence types, requirement writing |
| 3–4 | Workflow mapping, status definitions, data schema design |
| 5–6 | Backend implementation (API endpoints, database) |
| 7–8 | Test case design and implementation |
| 9–10 | Error handling, duplicate detection, authorization checks |
| 11–12 | Documentation, README, impact estimate |
| 13 | Peer review and code critique |
| 14 | Live demonstration and viva |

---

## 6. Milestones and Deliverables

| Milestone | Week | Deliverable |
|---|---|---|
| M1 — Problem Statement | 2 | 1–2 page document: observed problem, assumptions, scope |
| M2 — Design Document | 4 | Workflow diagram + data schema + API contract sketch |
| M3 — Working Prototype v1 | 8 | Code + test suite (minimum 5 automated tests passing) |
| M4 — Complete Submission | 12 | Full code, documentation, evidence log, impact estimate |
| M5 — Demonstration | 14 | Live demo + viva (individual) |

---

## 7. Capstone Acceptance Tests (Synthetic Data)

These are the required test scenarios that every submission must pass. Data is entirely synthetic.

### Test T1 — Duplicate Request Detection

| Field | Detail |
|---|---|
| **Scenario** | A student submits a grade review request. The same student submits the same request again. |
| **Input** | Student ID: S001, Subject: CS101, Semester: 5 — submitted twice |
| **Expected result** | First request accepted and assigned ID REQ-001. Second request rejected with status `DUPLICATE_DETECTED`. REQ-001 is processed only once. |
| **Verification** | Check that only one record with (S001, CS101, Sem5) exists in the database after both submissions. |
| **Pass condition** | Zero duplicate records; second submission returns an appropriate error message. |

### Test T2 — Missing Information Detection

| Field | Detail |
|---|---|
| **Scenario** | A request is submitted without a required field (subject code is blank). |
| **Input** | Student ID: S002, Subject: "", Reason: "I believe my answer was misread", Semester: 4 |
| **Expected result** | Request is rejected at input stage with status `MISSING_FIELD: subject`. Request is not stored. |
| **Verification** | Database has no entry for S002 from this submission. The response includes a clear error identifying the missing field. |
| **Pass condition** | No partial record stored; error correctly identifies the missing field. |

### Test T3 — Unauthorized Approval Rejection

| Field | Detail |
|---|---|
| **Scenario** | A user without the coordinator role attempts to approve a pending request. |
| **Input** | Role: STUDENT, Action: APPROVE, Request ID: REQ-003 |
| **Expected result** | Action is rejected with status `UNAUTHORIZED`. Request remains in `UNDER_REVIEW` status. |
| **Verification** | REQ-003 status is still `UNDER_REVIEW` after the unauthorized attempt. |
| **Pass condition** | Status unchanged; error logged; no approval applied. |

### Test T4 — Failed Step Recovery

| Field | Detail |
|---|---|
| **Scenario** | A coordinator attempts to approve REQ-004 but a simulated database error occurs during the write. |
| **Input** | Role: COORDINATOR, Action: APPROVE, Request ID: REQ-004 (simulate DB failure with a mock) |
| **Expected result** | System catches the error, logs it with a timestamp, and leaves REQ-004 in `UNDER_REVIEW` (unchanged). The error is retrievable from a log query. |
| **Verification** | REQ-004 status unchanged; error record visible in log; system remains operational. |
| **Pass condition** | No data corruption; REQ-004 still processable; log entry present. |

### Test T5 — Before-and-After Process Measure

| Field | Detail |
|---|---|
| **Scenario** | Illustrative estimate of time saving using synthetic assumptions. |
| **Synthetic assumptions** | Before: each duplicate check is manual, estimated 10 minutes per request; 20 requests per week → 200 minutes/week on duplicate checking. After: automated duplicate detection handles this in <1 second. Saving: approximately 200 minutes/week (SYNTHETIC ESTIMATE — not a measured result). |
| **Input** | Synthetic: 20 requests/week × 10 min/request manual duplicate check |
| **Expected result** | Prototype eliminates manual duplicate checking, estimated saving: 200 min/week = ~3.3 hours/week |
| **Honest label** | This is an illustrative synthetic estimate. Actual saving depends on real volume, which is not available. Students must label this as an estimate, not a fact. |
| **Pass condition** | Student presents a clearly labelled estimate with stated assumptions. Claim is not presented as a measured result. |

---

## 8. Assessment Rubric

| Component | Weight | Assessment Criteria |
|---|---|---|
| Problem statement and requirements (M1) | 15% | Clear, honest, distinguishes observed from assumed |
| Design document (M2) | 15% | Workflow diagram is correct; schema and API make sense for the requirements |
| Working prototype (M3) | 25% | Code runs; all 5 test scenarios pass; no crashes on edge cases |
| Documentation (M4) | 15% | README is clear; evidence log is honest; impact estimate is labelled |
| Live demonstration and viva (M5) | 30% | Student can explain design choices, handle unexpected questions, demonstrate the system |

**Practical assessment principles:** The viva tests whether the student genuinely understands what they built, not whether they can reproduce memorised answers. Questions include: "Why did you choose this data structure?", "What happens if a user submits with an empty subject?", "How would you deploy this?", "What would you change if you had more time?"

---

## 9. Connection to Existing Courses

| Lab Activity | Connected Course |
|---|---|
| Problem statement, evidence types | CS304 Software Engineering |
| SQL schema design, transactions | CS206 DBMS |
| REST API design and implementation | CS205 Web-Enabled Technologies |
| Automated test cases | CS304, CS101 |
| Workflow and state machine design | CS202 Theory of Computation (state transitions) |
| Authorization and role checking | CS301 Cryptography, CS415 Ethical Hacking |
| Error logging and recovery | CS302 Operating Systems |
| Documentation | EG101, EG102 |

This lab is designed to be taken after Semester V, when most foundational courses are complete. Students should have the component skills — they are now asked to assemble them.

---

## 10. Prerequisites

| Prerequisite | Recommended course |
|---|---|
| Programming in Python or Java | CS101, CS201 |
| Database fundamentals and SQL | CS206 |
| Web technologies | CS205 |
| Software engineering process | CS304 |
| Data structures | CS102 |

These are **recommended academic prerequisites** based on the logical dependency of skills. They are not verified as officially mandated prerequisites in the IFHE programme.

---

## 11. Safety, Privacy, and Permission Boundaries

- **No real student data.** All scenarios use synthetic student IDs (e.g., S001, S002), synthetic grades, and fictional subjects. Submitting any real student name, ID, marks, or personal information would invalidate the submission.
- **No real college systems.** Students connect to a local SQLite database or a test PostgreSQL instance, not any actual college database or portal.
- **No real approval authority.** The approval role in the prototype is simulated with a test user. It does not represent or interact with any real academic authority.
- **Transparency about limitations.** Students must include a Limitations section in their documentation acknowledging what the prototype does not do and what assumptions it relies on.

---

## 12. How This Connects to Task 1 (ResultFlow)

Task 1 investigated a real workflow problem (result-publication delays at IFHE) and proposed a structured workflow (ResultFlow) with a Python prototype and 20 automated tests.

This lab proposes that students learn the same *kind of thinking* — but by doing it themselves on a fresh scenario. The connection is methodological, not technical. Students are not required to build ResultFlow again. They are asked to apply the same approach:
1. Observe a real-looking problem.
2. Distinguish facts from assumptions.
3. Design a workflow with clear statuses and roles.
4. Build a prototype with tested error handling.
5. Document honestly.

Task 1 is the existence proof that this kind of work is possible at the undergraduate level.

---

*LAB_CAPSTONE_PROPOSAL.md | Task 2 | HKAIVERSE Round 2 | 24 October 2026 | Student proposal — not an approved IFHE course*
