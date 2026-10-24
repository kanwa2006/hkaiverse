# HKAIVERSE Round 2 — Submission Repository

**Participant:** kanwa2006
**Round:** HKAIVERSE Round 2
**Submission deadline:** 24 October 2026, 11:59 PM IST

---

## Repository Structure

| Folder | Task | Status |
|---|---|---|
| [`Task1/`](Task1/) | Investigate a college workflow — ResultFlow | Complete |
| [`Task2/`](Task2/) | Curriculum audit and redesign — B.Tech CSE, IFHE, Batch 2023–2027 | Complete |

---

## Task 1 — ResultFlow

**Topic:** Investigating the result-publication delay for Summer Term grade-improvement attempts at IFHE Hyderabad and proposing a structured, transparent workflow (ResultFlow) to reduce student uncertainty during placement processing.

**Problem in one line:** A student waited 90 days for a grade-improvement result. During that time, the placement form treated the pending subject as a backlog — making a student with passing grades appear blocked.

**How ResultFlow improves this:**

```mermaid
flowchart LR
    A([Student submits\nimprovement attempt]) --> B[REGISTERED]
    B --> C[EXAM_COMPLETED]
    C --> D[RESULT_PROCESSING]
    D --> E[UNDER_VERIFICATION]
    E --> F[AWAITING_APPROVAL]
    F --> G{Approver\ndecision}
    G -->|Approve| H([PUBLISHED\nGrade synced to placement])
    G -->|Reject| I([Attempt closed\nno grade change])
    style H fill:#22c55e,color:#fff
    style I fill:#ef4444,color:#fff
    style G fill:#f59e0b,color:#fff
```

**Key documents:**
- [`Task1/README.md`](Task1/README.md) — full project overview, evidence log, workflow design, and test summary
- [`Task1/TASK1_REPORT.md`](Task1/TASK1_REPORT.md) — detailed investigation report
- [`Task1/prototype/`](Task1/prototype/) — Python prototype (resultflow.py), test suite (test_resultflow.py), and ROI script
- [`Task1/evidence/`](Task1/evidence/) — screenshot evidence, pytest output, case results, and ROI output

**Test status:** 20/20 tests pass (pytest, Python 3.12, 23 Oct 2026).

---

## Task 2 — Curriculum Audit and Redesign

**Topic:** Auditing the B.Tech CSE curriculum at IFHE Hyderabad (batch 2023–2027) and proposing a balanced redesign that retains strong theoretical foundations while adding more practical, project-based learning aligned with entry-level industry requirements.

**Problem in one line:** Students can complete every subject individually without ever building a frontend, backend, API, and database into one working application — yet every graduate job description requires exactly this.

**How the audit was structured:**

```mermaid
flowchart TD
    A([Course portal\nscreenshots\nSems I–VII]) --> B[53-course baseline\nCOURSE_MAP.csv]
    B --> C[Audit 12 redesign\nreasons — CURRICULUM_AUDIT.md]
    C --> D{Decision per course}
    D -->|KEEP| E[31 courses unchanged]
    D -->|UPDATE| F[9 courses improved]
    D -->|REDUCE| G[3 courses reduced\n-3 credits]
    D -->|ADD| H[1 new lab added\n+3 credits]
    E & F & G & H --> I([Proposed total\n167 credits\nnet = 0])
    J([3 job descriptions\nACHNET · JPMorgan\nJoveo]) --> K[Gap analysis\nJOB_DESCRIPTION_COMPARISON.md]
    K --> F & H
    style I fill:#22c55e,color:#fff
    style J fill:#3b82f6,color:#fff
```

**Key documents:**
- [`Task2/README.md`](Task2/README.md) — main entry point: problem statement, proposed changes, evidence summary, and all links
- [`Task2/CURRICULUM_AUDIT.md`](Task2/CURRICULUM_AUDIT.md) — full course map, 12 redesign reasons, KEEP/UPDATE/REDUCE/ADD decisions
- [`Task2/CREDIT_CALCULATIONS.md`](Task2/CREDIT_CALCULATIONS.md) — transparent credit calculations (baseline 167 cr → proposed 167 cr, ~20% affected)
- [`Task2/JOB_DESCRIPTION_COMPARISON.md`](Task2/JOB_DESCRIPTION_COMPARISON.md) — three job description PDFs (ACHNET, JPMorgan, Joveo) compared to existing courses
- [`Task2/AI_EXERCISES.md`](Task2/AI_EXERCISES.md) — five AI-assisted exercises with verification and reflections
- [`Task2/LAB_CAPSTONE_PROPOSAL.md`](Task2/LAB_CAPSTONE_PROPOSAL.md) — Applied Software Product Engineering Lab proposal
- [`Task2/course_explorer.html`](Task2/course_explorer.html) — interactive course explorer (open locally in any browser)
- [`Task2/CURRICULUM_SCREENSHOTS.md`](Task2/CURRICULUM_SCREENSHOTS.md) — index and reconciliation of semester-wise course portal screenshots
- [`Task2/SOURCES.md`](Task2/SOURCES.md) — all sources, access dates, evidence categories
- [`Task2/FEEDBACK_AND_LIMITATIONS.md`](Task2/FEEDBACK_AND_LIMITATIONS.md) — feedback, personal contribution, limitations, validation status
- [`Task2/tests/test_course_explorer.py`](Task2/tests/test_course_explorer.py) — automated test suite (15/15 tests pass)

**Evidence files:**
- [`Task2/assets/`](Task2/assets/) — 7 semester-wise course portal screenshots (Sems I–VII)
- [`Task2/job_descriptions/`](Task2/job_descriptions/) — 3 job description PDFs: ACHNET SDE, JPMorgan Data Analyst, Joveo Full-Stack Intern

**Test status:** 15/15 course explorer tests pass (Python 3.11, 24 Oct 2026). 20/20 Task 1 tests continue to pass.

**Status:** Complete. Proposal only — not an approved IFHE policy document.

---

## Release and Commit

**Final commit (HEAD):** [`7249481`](https://github.com/kanwa2006/hkaiverse/commit/7249481f39343adc6e7db9fd9bb82076564e2cbd)
Full SHA: `7249481f39343adc6e7db9fd9bb82076564e2cbd`

**GitHub release:** Go to [github.com/kanwa2006/hkaiverse/releases/new](https://github.com/kanwa2006/hkaiverse/releases/new) → tag `v2.0-task2-final` → target `main` → title *"HKAIVERSE Round 2 — Final Submission"* → publish.

---

*All prototype data is synthetic. No real student names, IDs, marks, fees, credentials, or private messages are included in this repository.*
