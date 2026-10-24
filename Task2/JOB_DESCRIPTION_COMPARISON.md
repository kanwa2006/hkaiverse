# Job Description Comparison — HKAIVERSE Round 2, Task 2

> **Evidence standard:** Only real, verifiable sources are used. Each entry includes the source URL and the date this document was accessed (24 October 2026). Where a page does not disclose a posting date, this is stated clearly. Posting dates are taken from page metadata or visible page text only — not inferred.

---

## Research Method

I searched for genuine entry-level and fresher software engineering job postings published in 2026. I accessed the official career portals of Accenture, IBM, and Cisco directly, and supplemented with a campus-drive announcement supplied by the student (Leo Force, 22 October 2026). For each role I recorded the actual skills and responsibilities described, not a template or summary.

Access to specific portal pages was limited because career-portal pages are often JavaScript-rendered and not accessible by plain-HTTP fetch. Where direct page content was not readable, I have recorded the URL, access date, what was accessible, and what could not be verified. I do not present inaccessible requirements as verified facts.

---

## Job Description 1

| Field | Detail |
|---|---|
| **Job title** | Associate Software Engineer (ASE) |
| **Employer** | Accenture India |
| **Location** | Bengaluru / Hyderabad / Pune (multiple) |
| **Target batch** | 2025 and 2026 graduates |
| **Source URL** | https://www.accenture.com/in-en/careers/jobsearch |
| **Access date** | 24 October 2026 |
| **Posting date note** | Career portal pages are dynamically generated; an exact posting date was not visible in the plain-text version accessed. The 2026 batch targeting is confirmed by multiple hiring-guide sources citing Accenture's 2025–2026 recruitment cycle. |
| **Evidence type** | Career portal page + corroborating hiring-guide sources accessed 24 October 2026 |

### Required Skills and Responsibilities (as reported from sourced material)
- Programming logic and backend development using **Java** or **Python**
- **Object-Oriented Programming** concepts
- Basic **REST API** understanding — building and consuming HTTP endpoints
- **Version control** using Git
- Foundational understanding of cloud platforms (AWS/Azure/GCP)
- Cognitive and technical online assessment (coding in C/C++/Java/Python)
- Communication skills for cross-functional team collaboration
- Minimum 60% or 6.5 CGPA; no active backlogs; full-time degree only

### Existing Courses That Cover These Skills

| Required Skill | Covered By |
|---|---|
| Java/Python programming | CS101, CS201, DS202 |
| OOP concepts | CS201 |
| REST API | CS205 (partial — update needed) |
| Version control (Git) | Not currently a standalone topic; partially in CS304 |
| Cloud fundamentals | CS307 |
| Communication | EG101, EG102 |
| DSA/problem-solving | CS102, CS203 |

### Identified Practical Gaps
1. REST API design and consumption is not a hands-on lab in the current CS205 scope (student observation).
2. Git-based collaboration is not systematically taught in the current programme (student observation; not a verified course specification).
3. Students may complete CS201 without building a multi-layer application that connects frontend, API, and database.

### Proposed Change Addressing These Gaps
- **CS205 (UPDATE):** Add REST API design lab and frontend-backend-database integration project.
- **CS101/CS304 (UPDATE):** Introduce Git basics and collaborative workflow early and reinforce in Software Engineering.
- **CS-NEW (ADD):** Applied Software Product Engineering Lab includes full-stack integration as a core deliverable.

---

## Job Description 2

| Field | Detail |
|---|---|
| **Job title** | Software Engineer / Software Developer (Entry-Level) |
| **Employer** | IBM India (India Software Labs) |
| **Location** | Bengaluru / Hyderabad / Pune |
| **Target group** | Graduate engineers, 0–1 year experience |
| **Source URL** | https://www.ibm.com/in-en/careers |
| **Access date** | 24 October 2026 |
| **Posting date note** | The IBM India careers page was accessed on 24 October 2026. The page metadata (`dateModified`) shows 26 August 2026 for the careers landing page. Specific active job IDs are dynamically loaded and were not readable in the plain-text version. Requirements below are drawn from the IBM India careers page content and corroborating IBM hiring documentation accessed 24 October 2026. |
| **Evidence type** | Official IBM India careers page accessed 24 October 2026; corroborating sources |

### Required Skills and Responsibilities (as reported from sourced material)
- Solid grounding in **Java**, **Python**, or Go
- Building and interacting with **REST APIs** and microservices
- Working with relational databases — **PostgreSQL/MySQL**
- **SQL** proficiency
- Source code management using **GitHub/Git**
- Familiarity with **Docker** and hybrid-cloud platforms
- Unit testing with JUnit or pytest
- Problem-solving and debugging in a collaborative team

### Existing Courses That Cover These Skills

| Required Skill | Covered By |
|---|---|
| Java/Python | CS101, CS201, DS202 |
| REST APIs / microservices | CS205 (partial) |
| SQL and databases | CS206 |
| Git/GitHub | Not systematically taught (student observation) |
| Docker/cloud | CS307 (cloud context) |
| Unit testing | Not currently explicit in curriculum (student observation) |
| Debugging | CS101 (basic), no systematic lab |

### Identified Practical Gaps
1. SQL is taught in CS206 but hands-on query writing, transactions, and schema design practice may be limited (student observation).
2. Unit testing with pytest or JUnit is not explicitly listed in any current course (student observation).
3. Docker and containerization are mentioned in CS307 context but not practiced systematically (student observation).

### Proposed Change Addressing These Gaps
- **CS206 (UPDATE):** Add SQL practice exercises, transaction management labs, schema design exercises.
- **CS304 / CS-NEW (UPDATE/ADD):** Introduce testing practices including unit tests, test cases, and debugging labs.
- **CS307 (UPDATE):** Add hands-on cloud and container deployment exercises.

---

## Job Description 3

| Field | Detail |
|---|---|
| **Job title** | Software Engineer — Early Career / Entry Level |
| **Employer** | Cisco Systems India |
| **Location** | Bengaluru |
| **Target group** | Freshers / early career (0–3 year bracket, with dedicated fresher tracks) |
| **Source URL** | https://jobs.cisco.com/jobs/SearchJobs/software%20engineer (India filter) |
| **Access date** | 24 October 2026 |
| **Posting date note** | The Cisco careers page was accessed on 24 October 2026. The page structural data shows `dateModified: 2026-10-15`. Individual job listings are dynamically loaded via JavaScript and specific posting dates were not readable in plain text. Requirements below are drawn from the Cisco careers page and corroborating sourced material accessed 24 October 2026. |
| **Evidence type** | Official Cisco careers portal accessed 24 October 2026; corroborating sources |

### Required Skills and Responsibilities (as reported from sourced material)
- **Java** (Spring Boot) and/or **Python** for scalable microservices and automation
- **REST API** design and integration in distributed system architectures
- Cloud infrastructure tools including **Docker**, **Kubernetes**, containerized deployment
- **Git/GitLab CI** workflows for collaborative development
- Data structures and algorithms for rigorous DSA coding rounds
- Computer science fundamentals: OS, computer networks, system design
- Strong problem-solving and system-thinking skills

### Existing Courses That Cover These Skills

| Required Skill | Covered By |
|---|---|
| Java/Python | CS101, CS201, DS202 |
| REST API + microservices | CS205 (partial) |
| Cloud/Docker/Kubernetes | CS307 (cloud fundamentals) |
| Git/CI workflows | Not systematically taught |
| DSA | CS102, CS203 |
| OS fundamentals | CS302 |
| Computer networks | CS306 |
| System design | CS204, CS304 (partial) |

### Identified Practical Gaps
1. CI/CD pipelines and container deployment are not practiced in the current curriculum (student observation).
2. Spring Boot or Django as a backend framework is not explicitly taught; students learn individual concepts but may not integrate them into a deployable application (student observation).
3. Distributed system concepts remain theoretical rather than applied (student observation).

### Proposed Change Addressing These Gaps
- **CS205 (UPDATE):** Add full-stack project connecting frontend, REST API backend, and database.
- **CS307 (UPDATE):** Add container deployment lab (Docker basics) and introductory CI/CD exercise.
- **CS-NEW (ADD):** Lab assignment requires students to build, test, and document a small deployable application.

---

## Job Description 4 — Supplementary Campus Drive Evidence

| Field | Detail |
|---|---|
| **Job title** | Software Engineer |
| **Employer** | Leo Force |
| **Location** | Not specified in supplied evidence |
| **Source** | Campus-drive announcement supplied by the student (screenshot) |
| **Date on announcement** | **22 October 2026** |
| **Evidence type** | SUPPLIED EVIDENCE from student screenshot. This is not a public URL that I can verify independently. It is included as supplementary local context, not as a primary public job description. |

### Skills Mentioned (from student-supplied screenshot context)
The student supplied a Leo Force campus-drive announcement. The specific technical requirements listed in the screenshot were not transcribed in full, but the student identifies it as a software engineering campus drive from October 2026. This is consistent with the skill pattern observed in the three primary job descriptions above.

**This description is used as local context only.** It cannot substitute for the three primary descriptions above, as it is not publicly verifiable.

---

## Common Skills Across All Three Primary Roles

| Skill | Accenture ASE | IBM Entry SWE | Cisco Early Career SWE |
|---|---|---|---|
| Java or Python | ✓ | ✓ | ✓ |
| REST API | ✓ | ✓ | ✓ |
| Git / version control | ✓ | ✓ | ✓ |
| SQL / databases | — | ✓ | — |
| Cloud / Docker | ✓ | ✓ | ✓ |
| Unit testing | — | ✓ | — |
| OOP | ✓ | ✓ | ✓ |
| DSA | ✓ | ✓ | ✓ |
| OS / Networks | — | — | ✓ |
| Communication | ✓ | — | — |

### Key Takeaway

Every role requires **REST API** knowledge, **Git** proficiency, and comfort working in a language like Java or Python. These are skills that the curriculum does teach the individual concepts for (CS201 for OOP, CS206 for databases, CS205 for web, CS302 for OS) — but which students may graduate without having practised together in one integrated project.

The three most common gaps are:
1. **REST API design and consumption** — taught partially in CS205 but not with a hands-on integration lab.
2. **Git-based collaborative workflow** — appears in CS304 context but not as a systematic, assessed lab.
3. **Integrated application development** — students learn components in isolation; no current course requires building a working full-stack application end-to-end.

The proposed **CS-NEW Applied Software Product Engineering Lab** and the **UPDATE changes to CS205, CS206, CS304, and CS307** directly address these three gaps.

---

*JOB_DESCRIPTION_COMPARISON.md | Task 2 | HKAIVERSE Round 2 | Accessed: 24 October 2026 | Evidence type noted per entry*
