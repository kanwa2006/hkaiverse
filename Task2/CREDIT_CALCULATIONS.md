# Credit Calculations — HKAIVERSE Round 2, Task 2

> **Status of this document:** Student-supplied dataset used as working baseline. Calculations are performed independently below. Results are for curriculum redesign analysis only — not an official IFHE document.

---

## 1. Baseline Credit Inventory

### Semester-by-Semester Totals (Student-Supplied Dataset)

| Semester | Courses | Credits |
|---|---|---|
| Semester I | CHY101, CS101, EC101, EG101, HS101, MA101, MT101 | 4+4+4+3+0+3+3 = **21** |
| Semester II | CH102, CS102, DS101, EG102, MA102, MT102, PH101 | 2+4+3+3+3+3+5 = **23** |
| Semester III | CR201, CS201, CS202, CS203, EC201, MA201, MA202, MG201 | 1+4+3+3+3+3+3+3 = **23** |
| Semester IV | CR202, CS204, CS205, CS206, DS202, DS203, EC102, HS201 | 1+3+4+4+3+3+3+3 = **24** |
| **Mandatory IP-1** | IP201 | **3** |
| Semester V | CR301, CS301, CS302, CS303, CS304, DS303, DS304, HS301 | 1+3+4+3+3+3+4+0 = **21** |
| Semester VI | CR302, CS305, CS306, CS307, DS201, DS307, SP301 | 1+3+4+4+3+3+3 = **21** |
| Semester VII | CS415, DS306, DS311, DS401, MG401 | 3+4+3+3+3 = **16** |
| **Mandatory IP-2** | [code to be confirmed] | **15** |
| **TOTAL** | | **167** |

**Working total: 167 credits.** This matches the student-supplied expected total.

### Data Note — HS301 Constitution of India
The student's course screenshot appears to show HS301 with a 3-credit entry. The student has explicitly instructed that HS301 be recorded as **0 credits** in both the baseline and proposed curriculum. This correction is used throughout all calculations. If the official course carries 3 credits, the student should verify this before any formal submission. The supplied corrected value (0 credits) is the working baseline used here.

### Credit Counting Principles
- IP-1 (IP201, 3 credits) is a mandatory post-Semester IV internship, approximately two months. It is listed separately.
- IP-2 (15 credits, approximately 24–26 weeks) is listed as Semester VIII. The official course code is not confirmed; "official code to be confirmed" is used.
- Internship credits are counted once only. No double-counting.
- HS101 (Essence of Indian Traditional Knowledge) is listed as 0 credits in the dataset and is included in the semester count without adding to the credit total.
- HS301 (Constitution of India) is 0 credits as instructed.

---

## 2. Proposed Changes and Their Credit Impact

### 2A. Changes That Affect Credit Allocation

Three eligible courses are proposed for a one-credit reduction each. One new three-credit practical lab is proposed.

| Course | Current Credits | Proposed Credits | Change | Type |
|---|---|---|---|---|
| PH101 — Physics | 5 | 4 | −1 | REDUCE |
| MG201 — Engineering Economics and Management | 3 | 2 | −1 | REDUCE |
| HS201 — Dynamics of Social Change | 3 | 2 | −1 | REDUCE |
| CS-NEW — Applied Software Product Engineering Lab | 0 | 3 | +3 | ADD |
| **Net change** | | | **0** | Balanced |

**Net credit change: 0.** Baseline total (167) equals proposed total (167).

### 2B. Courses Whose Learning Design Changes (No Credit Change)

UPDATE changes improve content, tools, or practical emphasis without changing credit values.

| Course | Proposed UPDATE Focus |
|---|---|
| CS101 — Computer Programming | Add Git, debugging, unit tests, AI-assisted coding with verification |
| CS102 — Data Structures | Add implementation projects, complexity analysis, real test cases |
| CS205 — Web-Enabled Technologies | Add REST API, full-stack integration (frontend + backend + database) |
| CS206 — Database Management Systems | Add SQL query practice, transactions, schema design exercises |
| CS302 — Operating Systems | Add shell scripting, process simulation, scheduling demonstrations |
| CS304 — Software Engineering | Add Agile practices, Git workflows, requirements tracing, documentation |
| DS304 — Machine Learning | Add practical model building, evaluation, data pipeline exercises |
| CS307 — Cloud Computing | Add hands-on deployment to cloud platforms, IaC basics |
| CS415 — Ethical Hacking | Strengthen secure coding and pen-testing lab components |

---

## 3. Percentage-Affected Calculation

### Defining the Terms

- **Numerator:** Credits directly affected by proposed changes.
- **Denominator:** Total programme credits (167).
- A credit is "affected" if its allocation changes (REDUCE or ADD) OR the course undergoes substantial learning redesign (UPDATE).
- Each credit counted once only.

### Method A — Conservative Calculation (Recommended Primary)

Count courses where credit allocation changes OR where redesign is substantive enough to clearly affect student learning.

| Category | Credits | Basis |
|---|---|---|
| Full credit-allocation changes (4 courses: 3 REDUCE + 1 ADD) | 5+3+3+3 = 14 | Credit values change directly |
| Key UPDATE courses (CS205, CS206, CS304, DS304, CS101) | 4+4+3+4+4 = 19 | Substantial practical/assessment redesign |
| **Subtotal** | **33** | |
| **Percentage** | **33 / 167 = 19.8%** | At boundary of 20% lower bound |

### Method B — Including All UPDATE Courses

| Category | Credits |
|---|---|
| REDUCE (PH101, MG201, HS201) | 5+3+3 = 11 |
| ADD (CS-NEW) | 3 |
| UPDATE (9 courses) | 4+4+4+4+4+3+4+4+3 = 34 |
| **Subtotal** | **48** |
| **Percentage** | **48 / 167 = 28.7%** (above 25% upper bound) |

### Method C — Partial-Credit UPDATE (50% per UPDATE course)

| Category | Credits |
|---|---|
| REDUCE + ADD | 14 |
| UPDATE × 50% | 17 |
| **Subtotal** | **31** |
| **Percentage** | **31 / 167 = 18.6%** |

### Summary

| Method | Credits Affected | % | In 20–25%? |
|---|---|---|---|
| A — Conservative | 33 | **19.8%** | At boundary |
| B — All UPDATEs | 48 | 28.7% | Above upper bound |
| C — 50% UPDATEs | 31 | 18.6% | Below lower bound |

**Preferred result: Method A at approximately 20%.** Reaching 25% defensibly would require additional allocation changes beyond what is proposed. The student acknowledges this and presents Method A as the most honest calculation.

---

## 4. Balance Check

| Item | Credits |
|---|---|
| Baseline total | 167 |
| Credits removed (3 × −1) | −3 |
| Credits added (new lab) | +3 |
| **Proposed total** | **167** |

✅ Balance maintained at 167 credits.

---

## 5. Assumptions and Limitations

1. Student-supplied dataset is the working baseline; not independently verified against official IFHE batch regulations.
2. HS301 is 0 credits per student instruction (data note above).
3. REDUCE proposals require formal academic approval. They are student recommendations, not enacted policy.
4. UPDATE changes are subject to faculty discretion and applicable regulations.
5. The 167-credit denominator covers the full programme.
6. No credit counted more than once.

---

*CREDIT_CALCULATIONS.md | Task 2 | HKAIVERSE Round 2 | 24 October 2026 | Student-supplied baseline*
