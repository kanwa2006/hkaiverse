# Sources and Evidence Log — HKAIVERSE Round 2, Task 2

> All sources are listed with URLs and the date they were accessed (24 October 2026). Where a source could not be fully accessed due to JavaScript rendering or access restrictions, the limitation is noted.

---

## 1. Curriculum Data Sources

| Source | Type | Details |
|---|---|---|
| Student course portal screenshots | SUPPLIED EVIDENCE | Provided by the student. Course codes, names, semester placement, and credits. Used as the working baseline. |
| Student clarification (HS301, IP-1/IP-2) | SUPPLIED EVIDENCE | Student instruction to use 0 credits for HS301; clarification that IP201 is IP-1, and IP-2 is the six-month internship. |
| IFHE / ICFAITech official sources | NOT VERIFIED | The official IFHE website (ifheindia.org) and ICFAITech pages were not successfully accessed with plain-HTTP to retrieve a batch-specific curriculum PDF. The student's dataset is labelled as student-supplied and provisional. |

---

## 2. Job Description Sources

| # | Employer | URL | Access Date | Posting Date | Notes |
|---|---|---|---|---|---|
| 1 | Accenture India | https://www.accenture.com/in-en/careers/jobsearch | 24 Oct 2026 | Not visible in plain text | Dynamic portal; 2026 batch targeting confirmed by multiple corroborating sources |
| 2 | IBM India | https://www.ibm.com/in-en/careers | 24 Oct 2026 | Page dateModified: 26 Aug 2026 | Plain-text access confirmed; individual job IDs require JavaScript |
| 3 | Cisco India | https://jobs.cisco.com/jobs/SearchJobs/software%20engineer (India filter) | 24 Oct 2026 | Page dateModified: 15 Oct 2026 | Plain-text access confirmed; individual listings dynamically loaded |
| 4 | Leo Force | Campus drive announcement (student-supplied screenshot) | Supplied by student | 22 Oct 2026 (date on announcement) | Not a publicly verifiable URL; used as supplementary local context only |

---

## 3. Corroborating Sources for Job Requirements

These sources were used to corroborate the skill profiles described in the job description comparison. They are secondary sources, not primary employer postings.

| Source | URL | Access Date | Used For |
|---|---|---|---|
| Accenture hiring guide — alexahire.in | https://alexahire.in/accenture-associate-software-engineer | 24 Oct 2026 | Corroborating Accenture ASE requirements (2025–2026 batch) |
| Accenture India careers summary | https://accenture.com/in-en/careers (sourced via web search) | 24 Oct 2026 | Confirming role title, eligibility, tech stack |
| IBM India entry-level page | https://www.ibm.com/in-en/employment/entry_level.html | 24 Oct 2026 | IBM India career structure and entry-level focus |
| Cisco careers portal | https://careers.cisco.com/global/en | 24 Oct 2026 | Cisco early-career tech stack confirmation |
| campustodrive.com — IBM India | https://campustodrive.com (IBM India) | 24 Oct 2026 | Corroborating IBM India requirements (Git, REST API, Docker) |
| Web search results (Google Grounding) | Multiple | 24 Oct 2026 | Pattern verification across Accenture, IBM, Cisco, Wipro, TCS, Infosys fresher profiles |

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
| GitHub API (https://api.github.com/repos/kanwa2006/hkaiverse/git/trees/main) | Repository structure inspection | Used on 24 Oct 2026 to read file tree |
| read_url_content (Antigravity tool) | Fetching career portal pages | Plain-HTTP only; JavaScript-rendered content not readable |
| Web search (Google Grounding via Antigravity) | Job requirement research | Queries documented in research session |
| PowerShell (local) | Directory creation, file management | Used to create Task2/ directory structure on 24 Oct 2026 |

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

## 7. Repository Inspection Record

| Item | Finding |
|---|---|
| Repository URL | https://github.com/kanwa2006/hkaiverse |
| Inspection date | 24 October 2026 |
| Method | GitHub API (tree endpoint) + raw.githubusercontent.com |
| Branch | main |
| Root files found | README.md, .gitignore, Task1/ directory |
| Task1 files found | README.md, TASK1_REPORT.md, .gitignore, evidence/, prototype/ |
| Task2 directory at inspection | Did not exist — created in this session |
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
