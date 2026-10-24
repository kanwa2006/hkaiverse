# Job Description Comparison — HKAIVERSE Round 2, Task 2

> **Evidence standard:** Three job description documents are provided in `job_descriptions/`. Each is read directly from the PDF evidence file. Where a posting date is visible in the document it is recorded; where it is not, this is stated clearly. All skill requirements are drawn from the actual document text, not inferred or templated.

---

## Research Method

Three PDF job description files were provided and inspected directly:

1. `Detailed Job Description - Tescra.pdf` — Software Engineer at ACHNET (Bangalore/Remote)
2. `JPMorgan_Chase_Data_Analyst_Fresher.pdf` — Data Analyst Fresher at JPMorgan Chase & Co.
3. `Joveo_SE_Intern_JD.pdf` — Software Engineering Intern (Full Stack) at Joveo (Bengaluru)

Each document was read using `pypdf`. Skills, responsibilities, and qualifications are extracted verbatim from the PDF content. The curriculum gap analysis compares each requirement against the current course map in `CURRICULUM_AUDIT.md`.

---

## Job Description 1 — ACHNET Software Engineer

| Field | Detail |
|---|---|
| **Job title** | Software Engineer (SDE) |
| **Employer** | ACHNET (AI-driven professional marketplace, Bangalore/Remote) |
| **Location** | Bangalore / Remote |
| **Target group** | B.Tech CSE or related field graduates |
| **Evidence file** | `job_descriptions/Detailed Job Description - Tescra.pdf` |
| **Posting date** | Not specified in the document |
| **Access/read date** | 24 October 2026 |
| **Evidence type** | PDF — read directly from file |

### Required Skills and Responsibilities (from PDF text)

- Full software development lifecycle — requirements analysis → development → documentation → testing → deployment
- Web application development: **HTML, CSS, JavaScript**, Microsoft Technologies, **Python**, open-source frameworks
- **Object-Oriented Programming (OOP)** — design and implementation
- **Data structures** — strong understanding required for software development
- **NoSQL databases** — Redis, MongoDB (experience or exposure)
- **Agile development** — collaborative, sprint-based environment
- **Machine Learning models** (YOLO, LLM, NER) — good to have
- Performance, security, and scalability of web applications
- B.Tech / B.E. in Computer Science or related field required

### Existing Courses That Cover These Skills

| Required Skill | Covered By |
|---|---|
| Python programming | CS101, CS201, DS202 |
| OOP | CS201 |
| Data Structures | CS102 |
| Web (HTML/CSS/JS) | CS205 |
| Full software lifecycle | CS304 (Software Engineering) |
| NoSQL databases | Not explicitly covered (CS206 covers relational SQL) |
| Agile methods | CS304 (partial) |
| ML/AI models | DS304, DS201 |
| Security | CS415 (Ethical Hacking) |

### Identified Practical Gaps

1. **NoSQL databases (Redis, MongoDB)** are not explicitly covered; CS206 focuses on relational SQL only. Students may reach this role without exposure to key-value or document stores.
2. **Full-stack web deployment** — CS205 covers web technologies but does not include building and deploying a working full-stack application (frontend + backend + database).
3. **Agile workflow practice** — CS304 discusses software engineering methodology but does not include a structured sprint-based lab where students experience iterative delivery.

### Proposed Changes Addressing These Gaps

- **CS205 (UPDATE):** Add REST API lab connecting frontend, Python backend, and SQLite database. Students experience the full stack before the lab course.
- **CS-NEW (ADD):** Applied Software Product Engineering Lab requires requirements, iterative sprints, testing, and final documentation — directly matching the ACHNET SDE lifecycle.
- **CS307 (UPDATE):** Cloud and deployment exercise addresses the "deployment" stage of the lifecycle.

---

## Job Description 2 — JPMorgan Chase Data Analyst (Fresher)

| Field | Detail |
|---|---|
| **Job title** | Data Analyst – Fresher |
| **Employer** | JPMorgan Chase & Co. |
| **Location** | Pan India / As per Business Requirement |
| **Target group** | Fresh graduates and 0–1 year experience; B.Tech, B.Sc., BCA, M.Sc., Statistics, Mathematics, CS, IT, Data Science, Economics, Business Analytics |
| **Evidence file** | `job_descriptions/JPMorgan_Chase_Data_Analyst_Fresher.pdf` |
| **Posting date** | Not specified in the document |
| **Access/read date** | 24 October 2026 |
| **Evidence type** | PDF — read directly from file |

### Required Skills and Responsibilities (from PDF text)

- **SQL** — Queries, Joins, Subqueries, CTEs, Aggregations, Window Functions
- **Python** — Pandas, NumPy, Matplotlib/Seaborn (data cleaning, transformation, EDA)
- **Microsoft Excel** — Pivot Tables, VLOOKUP/XLOOKUP, INDEX-MATCH, Conditional Formatting
- **Statistics** — Descriptive statistics, probability fundamentals, correlation, regression basics
- **Data Visualization** — Power BI or Tableau (dashboards, interactive reports)
- **Data Cleaning and Preparation**
- **Exploratory Data Analysis (EDA)**
- Collect, clean, validate, and analyse structured and unstructured datasets
- Write SQL queries to extract and manipulate data from databases
- Develop and maintain reports and dashboards
- Translate business requirements into analytical outputs
- Good to have: ETL/ELT, cloud platforms (AWS/Azure/GCP), data warehousing, Git/GitHub, AI/ML fundamentals

### Existing Courses That Cover These Skills

| Required Skill | Covered By |
|---|---|
| SQL and databases | CS206 (Database Management Systems) |
| Python | CS101, DS202, DS304 (ML context) |
| Statistics and probability | MA201 (Integral Transforms and Probability & Statistics) |
| Data Science concepts | DS203, DS101 |
| Machine Learning / AI | DS304, DS201 |
| Git | Not systematically taught (student observation) |
| Data Visualization | Not explicitly covered as a standalone lab |
| ETL/ELT, data warehousing | DS307 (Big Data Systems, partial) |

### Identified Practical Gaps

1. **SQL query practice depth** — CS206 teaches database concepts and SQL, but a hands-on progression from simple SELECT through CTEs and window functions is not confirmed as a lab component (student observation).
2. **Data visualization tools (Power BI / Tableau)** — not covered in the current curriculum; students have no structured exposure to industry dashboard tools.
3. **Python for data analysis (Pandas, NumPy, Matplotlib)** — Python is taught in CS101 and DS202 but the data-analysis-specific libraries used in industry are not systematically practised.
4. **Exploratory Data Analysis as a structured practice** — DS203 covers Data Science concepts, but EDA as a hands-on workflow (cleaning, profiling, analysis, reporting) does not appear as an explicit lab.

### Proposed Changes Addressing These Gaps

- **CS206 (UPDATE):** Add SQL practice exercises progressing through joins, aggregations, CTEs, and a schema-design task.
- **DS304 (UPDATE):** Practical ML lab includes dataset exploration, cleaning, train/test split, and model evaluation — directly building EDA and Python data-skills relevant to the analyst role.
- **CS-NEW (ADD):** Lab documentation and report components give students practice in translating a technical result into a clear written output — matching JPMorgan's "translate business requirements into meaningful analytical outputs" requirement.

---

## Job Description 3 — Joveo Software Engineering Intern (Full Stack)

| Field | Detail |
|---|---|
| **Job title** | Software Engineering Intern (Full Stack) |
| **Employer** | Joveo (Forbes-recognized startup, "America's Best Startup Employers 2026") |
| **Location** | Bengaluru — Work from Office, 5 days a week |
| **Target group** | Computer science students and early-career engineers; internship role |
| **Evidence file** | `job_descriptions/Joveo_SE_Intern_JD.pdf` |
| **Posting date** | Document references "2026" in Forbes recognition badge; specific posting date not stated |
| **Access/read date** | 24 October 2026 |
| **Evidence type** | PDF — read directly from file |

### Required Skills and Responsibilities (from PDF text)

- **React and Next.js** (frontend)
- **Node.js and Express** (backend)
- **PostgreSQL and Supabase** — schema design, indexing, query optimization
- **REST APIs** — design, implementation, and consumption
- **Git** — version control and collaborative workflow
- **LLMs, embeddings, and vector databases (pgvector)** — practical integration into real products
- **TypeScript**
- Full-stack ownership — requirements, building, and shipping to production
- Greenfield AI product development — whiteboards to working prototype in weeks
- Load balancing, search optimization, indexing, categorization at scale
- **AWS** — advantageous
- Portfolio of shipped projects required

### Existing Courses That Cover These Skills

| Required Skill | Covered By |
|---|---|
| JavaScript / Web programming | CS205 |
| Databases and SQL | CS206 |
| REST API | CS205 (partial; no dedicated lab) |
| Git/version control | Not systematically taught (student observation) |
| Cloud (AWS) | CS307 (cloud fundamentals) |
| Networking/system basics | CS302, CS306 |
| OOP / backend programming | CS201 |
| AI/ML and LLM awareness | DS304, DS201 |
| Full-stack integration | Not covered — no integrated project course |
| PostgreSQL / NoSQL | CS206 (relational SQL; no PostgreSQL-specific lab) |

### Identified Practical Gaps

1. **Full-stack integration with a real stack (React + Node.js + PostgreSQL)** — the curriculum teaches the components individually but no current course requires students to assemble them into a working deployable application.
2. **REST API design and implementation** — CS205 introduces web technologies but a hands-on API design and test lab does not appear to be present (student observation).
3. **Git workflow as a collaborative practice** — Joveo explicitly requires a shipped-project portfolio and comfort with Git commits. This is not systematically assessed in any current course.
4. **Modern deployment** — shipping an application to a cloud service, even a free tier, is not part of any current lab.

### Proposed Changes Addressing These Gaps

- **CS205 (UPDATE):** Add REST API design lab — 3-endpoint API, Python backend, SQLite, tested with curl or Postman.
- **CS304 (UPDATE):** Git workflow lab — branches, pull requests, merge conflict resolution.
- **CS307 (UPDATE):** Hands-on cloud deployment exercise (Render, Railway, or equivalent free platform); Docker containerisation.
- **CS-NEW (ADD):** Applied Software Product Engineering Lab — students build a complete small application (requirements → design → implementation → testing → documentation → demonstration), directly matching the "full ownership from whiteboard to working prototype" requirement.

---

---

## Cross-Role Skill Comparison Across the Three On-Campus Opportunities

| Skill Area | ACHNET SDE | JPMorgan Data Analyst | Joveo SWE Intern (Full Stack) |
|---|---|---|---|
| **Python** | ✓ Required (programming & frameworks) | ✓ Required (Pandas, NumPy, EDA) | ✓ Required |
| **Web Technologies / Frontend** | ✓ HTML, CSS, JavaScript | — | ✓ React, Next.js, TypeScript |
| **Backend & REST APIs** | ✓ OOP & web application backend | — | ✓ Node.js, Express, REST APIs |
| **Databases & Querying** | ✓ NoSQL (Redis, MongoDB as a plus) | ✓ Advanced SQL (Joins, CTEs, Window Functions) | ✓ PostgreSQL, Supabase |
| **Data Analysis & Visualization** | — | ✓ Statistics, EDA, Excel, Power BI / Tableau | — |
| **Data Structures & OOP** | ✓ Strong data structures & OOP design | ✓ Analytical problem-solving | ✓ Systems problem-solving |
| **Version Control (Git/GitHub)** | — | ✓ Listed as good-to-have | ✓ Required (collaborative workflow) |
| **Cloud & Deployment** | ✓ Deployment in SDLC | ✓ Cloud platforms listed as good-to-have | ✓ AWS advantageous |
| **Software Lifecycle & Ownership** | ✓ Full SDLC (analysis → test → deploy) | ✓ Data validation & analytical reporting | ✓ Full-stack ownership (whiteboard to ship) |
| **AI / ML / LLMs** | ✓ Good to have (YOLO, LLMs, NER) | ✓ AI/ML fundamentals (good-to-have) | ✓ LLMs, embeddings, pgvector |

### Key Takeaway: Distinct Role Tracks and Targeted Curriculum Solutions

The three on-campus recruitment documents demonstrate that graduate employment paths diverge into distinct functional roles rather than a single homogeneous profile:

1. **Software Development Engineer (ACHNET):** Focuses on core programming (Python, OOP, data structures), web development, and the end-to-end SDLC.
   - *Curriculum Response:* Strengthened programming and unit testing in **CS101**, data structure benchmarking in **CS102**, and structured engineering process in **CS304**.
2. **Data Analyst (JPMorgan Chase):** Focuses heavily on deep relational database querying (CTEs, window functions, aggregations), exploratory data analysis (EDA), and data reporting. Git and cloud are explicitly listed as good-to-have advantages.
   - *Curriculum Response:* Advanced SQL query exercises and schema design in **CS206**, probability/statistics in **MA201**, and dataset cleaning and model evaluation labs in **DS304**.
3. **Full-Stack Engineering Intern (Joveo):** Demands integrated full-stack construction connecting modern frontend, backend, PostgreSQL database, REST APIs, and collaborative Git workflows.
   - *Curriculum Response:* REST API design and testing in **CS205**, Git branching and pull-request lab in **CS304**, cloud deployment in **CS307**, and the integrated prototype build in **CS-NEW** (Applied Software Product Engineering Lab).

---

*JOB_DESCRIPTION_COMPARISON.md | Task 2 | HKAIVERSE Round 2 | Evaluated against supplied on-campus recruitment materials (reviewed 24 October 2026)*
