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

These are the five required test scenarios that every student prototype must implement and pass, directly mirroring the core operational scenarios evaluated in ResultFlow. Data is entirely synthetic.

### Test T1 — Normal Workflow (Happy Path)

| Field | Detail |
|---|---|
| **Scenario** | A student submits a complete, valid grade review request; coordinator approves it. |
| **Input** | Student ID: S001, Subject: CS101, Reason: "Re-evaluation of final project component", Semester: 5 |
| **Expected result** | Request accepted in `RECEIVED` status, advances to `UNDER_REVIEW`, and upon coordinator approval transitions to `APPROVED` with timestamp logged. |
| **Verification** | State history shows sequential progression; final state is `APPROVED`; effective record is updated. |
| **Pass condition** | Request successfully completes full lifecycle with authorized sign-off. |

### Test T2 — Missing Information Detection

| Field | Detail |
|---|---|
| **Scenario** | A request is submitted with missing or blank mandatory fields (e.g., empty subject code). |
| **Input** | Student ID: S002, Subject: "", Reason: "Suspected tabulation error", Semester: 4 |
| **Expected result** | Request is rejected at input validation with error code `MISSING_FIELD: subject`. No partial record is stored. |
| **Verification** | Database contains no unvalidated or corrupted records for S002. |
| **Pass condition** | Input rejected cleanly; informative error returned; database state unchanged. |

### Test T3 — Duplicate Request Detection

| Field | Detail |
|---|---|
| **Scenario** | A student submits an active review request, then resubmits the same request while the first is still pending. |
| **Input** | Resubmission of (S001, CS101, Semester 5) while first attempt is active |
| **Expected result** | Second submission is rejected with status `DUPLICATE_DETECTED`. Original request remains active and unmodified. |
| **Verification** | Exactly one active attempt record exists in database for the given student and subject. |
| **Pass condition** | Duplicate blocked; no duplicate records created; idempotency preserved. |

### Test T4 — Unauthorized Request Rejection

| Field | Detail |
|---|---|
| **Scenario** | An unauthorized role (e.g., student or unprivileged user) attempts to approve or publish a review request. |
| **Input** | Actor: "SYN-STUDENT-1", Role: `student`, Action: `APPROVE`, Target: REQ-001 |
| **Expected result** | Action is rejected with error `UNAUTHORIZED_ROLE`. Request status remains `UNDER_REVIEW`. |
| **Verification** | Audit log records unauthorized attempt; request status is unaltered. |
| **Pass condition** | Strict role enforcement; unauthorized state mutation blocked. |

### Test T5 — Failed Step and Recovery

| Field | Detail |
|---|---|
| **Scenario** | A simulated database or service failure occurs during a state transition or external synchronization. |
| **Input** | Coordinator triggers approval write under simulated storage failure |
| **Expected result** | System catches the exception, rolls back partial changes, logs the failure with timestamp, and marks state as retryable without corrupting data. Subsequent authorized retry succeeds. |
| **Verification** | No corrupted state; retry successfully completes the transition once the failure condition clears. |
| **Pass condition** | Exception handled gracefully; no silent failure; recovery verified. |

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

The lab explicitly builds upon the architectural model developed in Task 1 (ResultFlow):

1. **State-Machine Reference:** Students use ResultFlow's six-state progression (`REGISTERED → EXAM_COMPLETED → RESULT_PROCESSING → UNDER_VERIFICATION → AWAITING_APPROVAL → PUBLISHED`) as the standard reference architecture for workflow governance and transition integrity.
2. **Persistence Layer:** Whereas the Task 1 prototype utilized an in-memory dictionary to prove business logic, students in this lab must design and connect a relational database (SQLite or PostgreSQL) with transactions, foreign keys, and status logs.
3. **API & Interface:** Students expose the workflow via a lightweight REST API (FastAPI or Flask) with dedicated endpoints for request submission, status inquiry, and authorized coordinator approval.
4. **Automated Verification:** Students implement automated test suites verifying the five foundational scenarios:
   - *Normal Progression* (happy path lifecycle)
   - *Missing Information* (payload validation)
   - *Duplicate Request* (idempotency enforcement)
   - *Unauthorized Request* (role-based access control)
   - *Failed Step & Recovery* (safe rollback and retry)

> **Important note on status:** This lab curriculum is an academic proposal designed to bridge theoretical software engineering with integrated development practices. It is not an active, deployed, or university-sanctioned production system.

---

*LAB_CAPSTONE_PROPOSAL.md | Task 2 | HKAIVERSE Round 2 | 24 October 2026 | Student proposal — not an approved IFHE course*
