# Feedback, Limitations, and Personal Contribution — HKAIVERSE Round 2, Task 2

---

## 1. Faculty and Graduate Feedback

### How the Feedback Was Gathered

I had two informal conversations — one with a senior who is now working as a software engineer in the IT industry, and one with a faculty member — about the general idea of improving the balance between theory and practical work in the curriculum. These were casual conversations, not formal interviews or structured consultations. No recording was made, no transcript exists, and no formal approval was sought. The consultations happened before this report was written.

### Graduate Feedback (Industry Perspective)

I spoke with a senior who completed the same programme and is currently working as a software engineer. I described the idea of giving students more hands-on experience — building complete projects rather than only individual exercises — and asked for their view.

The response was broadly supportive. The senior agreed that having more practice with realistic projects would have been useful. The point made was that the first few months in a job often involve understanding how different parts of a system work together, and that this kind of thinking is easier when you have already tried to build something complete during your studies.

I have not included the senior's employer, name, or contact details. This is informal feedback on a general idea, not a formal endorsement of any specific curriculum change.

**Influence on the proposal:** This conversation reinforced the focus on integration — the idea that students should experience how a frontend, an API, and a database connect, rather than only learning each component in isolation. The Applied Software Product Engineering Lab proposal directly reflects this.

### Faculty Feedback

I also spoke informally with a faculty member about the same general idea. The faculty member was supportive of learning approaches that emphasize students applying their knowledge through practice, along the lines of what is done at some universities abroad. The point expressed was that students who build and explain working projects during their studies tend to find the transition to a job less confusing. They arrive with a stronger sense of how to start a task, how to handle unfamiliar problems, and what is expected of them in a professional environment.

I am not attributing this to any specific person or claiming it is official faculty policy. It is an informal observation shared in a conversation.

**Influence on the proposal:** This feedback shaped the viva component in the lab assessment. The idea that explaining a design decision out loud is itself a learning outcome — and that students benefit from the practice of doing this — is directly reflected in the 30% weighting for the live demonstration and viva in the capstone rubric.

### What the Feedback Does and Does Not Prove

These two conversations support the general direction of the proposal. They do not prove that the proposal will work, that it is the optimal approach, or that it has institutional support. A more rigorous validation would involve:
- A structured survey of graduates comparing curriculum experience with job readiness.
- A review of comparable curricula at other institutions.
- Formal consultation with the department and faculty committee.
- Student cohort data on practical assessment performance.

None of these have been done for this report. The feedback is presented as informal input on a plausible direction, not as evidence that the redesign is necessary or sufficient.

---

## 2. Critical Reflection: Evolution of Thinking and Falsifiability

### What Feedback and Evidence Changed My Thinking

At the beginning of this investigation, my initial assumption was that the curriculum's primary shortcoming was simply a matter of outdated programming languages or a lack of modern framework electives. I originally thought the solution would be proposing several new standalone elective courses covering trendy technologies.

Two key pieces of evidence and feedback fundamentally challenged and changed this perspective:

1. **Analysis of the Three On-Campus Job Descriptions (ACHNET, JPMorgan Chase, Joveo):**
   When I examined the actual recruitment documents verbatim, I found that employers were not seeking a superficial catalogue of languages. ACHNET emphasized the end-to-end software development lifecycle and object-oriented architecture; JPMorgan prioritized rigorous SQL querying (joins, aggregations, window functions) and systematic data cleaning; Joveo demanded end-to-end ownership where students can connect a frontend, an API, and a database into a working system. The issue was not that students needed *more* isolated subjects, but that they lacked opportunities to *integrate* what they already study.

2. **Faculty and Industry Consultations:**
   The senior graduate working in the software industry explained that early-career confusion stems almost entirely from connecting disparate components (APIs, databases, deployment), not from lack of modular theory. Concurrently, the faculty conversation reinforced that simply adding more courses would create academic overload without solving the application gap.

As a result, I completely revised my approach: instead of expanding the degree envelope, I designed a **zero-net-credit redesign** (167 → 167 credits) that leaves all 40 core CS theory courses intact, enriches 9 existing courses with practical labs, and introduces a single 3-credit integrative capstone funded by trimming 3 credits from lower-relevance coursework.

### What Evidence Could Disprove My Strongest Curriculum Claim

**Strongest Curriculum Claim:**
> *"Introducing mandatory, end-to-end practical integration labs (such as CS-NEW and the 9 course updates) significantly improves fresh graduate competence and workplace readiness compared to teaching theoretical fundamentals in isolated modular subjects."*

**Falsification Criteria (What Would Disprove This Claim):**
1. **Longitudinal Graduate Performance Data:** If a comparative study of B.Tech cohorts showed that graduates trained under purely theoretical, modular curricula adapted to industry roles (measured by time-to-first-commit, probation clearance, or manager evaluations) at the same or higher rate than peers with compulsory integrative capstone labs.
2. **Cognitive Load and Foundational Mastery Evidence:** If assessment analytics demonstrated that introducing early full-stack and API integration exercises created cognitive overload, leading to statistically significant declines in student mastery of core algorithms, data structures, and discrete mathematics.
3. **Employer Recruitment Feedback:** If campus placement recruiters explicitly reported that fresh graduates fail technical interviews due to weaknesses in pure algorithmic proofs and mathematical theory rather than gaps in practical coding, Git workflows, or SQL proficiency.

If such empirical evidence were established, my proposal to reallocate credits and lab hours toward practical integration would be invalidated, and maintaining traditional modular instruction would be the superior academic choice.

---

## 3. Personal Contribution

This report represents my own work, concern, and reasoning. The specific contributions I made are:

- I identified the concern about the gap between theory and practical confidence from my own experience as a student.
- I supplied the course list, credit values, and semester placement from my own course portal screenshots.
- I proposed the main curriculum changes: the UPDATE directions for specific courses, the REDUCE proposals for three courses, and the ADD of a new practical lab.
- I proposed the lab problem scenario (grade review workflow) as an educational exercise inspired by the same category of problem I investigated in Task 1.
- I had the two informal conversations described above and reported them honestly.
- I used AI assistance (Claude Sonnet 4.6, Antigravity IDE) to help research, draft, organise, and verify the documents in this submission.
- I reviewed the evidence, the credit calculations, and the overall structure of the report.

I did not invent feedback, statistics, job descriptions, or test results. Where I cannot verify something, I have said so. Where something is my opinion or observation, I have labelled it as such.

---

## 4. Limitations

### Curriculum Data Scope
- Course portal screenshots (Semesters I–VII) provide the direct student record evidence for the 2023–2027 batch.
- HS301 is recorded as 0 credits. The Semester V portal screenshot (`assets/sem5_courses.png`) confirms HS301 with 0 credits; data is consistent across all documents.
- IP-2 course code: the supplied curriculum materials do not specify a course code for Mandatory Internship-II. It is identified by name throughout this report.
- Prerequisites listed in this report are recommended academic dependencies, not officially mandated prerequisites.

### Job Description Evidence Scope
- The three job descriptions are sourced from on-campus recruitment documents received via student college email (ACHNET, JPMorgan Chase, Joveo). Skills are extracted verbatim from the document text using `pypdf`.
- Specific original posting dates are not stated in the PDFs; the read date (24 October 2026) and internal document references (e.g., Joveo 2026 Forbes recognition badge) are recorded.
- The ACHNET document is titled "Detailed Job Description - Tescra.pdf" in the provided file; ACHNET is the recruiting entity described in the document text.

### Calculation Scope
- The 19.8% figure (Method A) sits at the conservative boundary of the 20–25% target.
- The REDUCE proposals require formal academic approval. Without approval, the credit total would remain unchanged and the new lab could not be funded from the programme's existing credit envelope without replacement elsewhere.

### Interactive Component
- The course explorer is a static HTML/CSS/JS file that runs locally in a browser without any server or external API dependency.
- All 15 functional test cases (CE-01 to CE-14b) are programmatically checked in Python via `Task2/tests/test_course_explorer.py` (validating dataset integrity and filter logic; browser rendering and DOM behavior are verified by opening the HTML file in any browser).

### AI Exercise Scope
- All five exercises were conducted on 24 October 2026.
- The prompts, outputs, and verification steps are documented faithfully.
- These are learning exercises; AI outputs were checked manually against known correct deterministic answers.

### Feedback Scope
- Two informal conversations are described. No recordings, transcripts, or formal sign-offs exist.
- Names and contact details are withheld for privacy.
- This feedback represents qualitative perspective, not institutional endorsement.

---

## 5. Validation Status

| Item | Status |
|---|---|
| Curriculum screenshots vs. COURSE_MAP.csv | ✓ Verified — all seven screenshots reconciled in `CURRICULUM_SCREENSHOTS.md` |
| HS301 credit value | ✓ Consistent — screenshot confirms 0 credits; dataset uses 0 |
| Credit calculation (baseline and proposed) | ✓ Verified — automated test CE-08 confirms 167 / 167 / net 0 |
| Course explorer data alignment & filter logic | ✓ Verified — all 15 automated Python checks pass (`test_course_explorer.py`) |
| Job description skills vs. curriculum map | ✓ Done — three PDFs read directly; gap analysis in `JOB_DESCRIPTION_COMPARISON.md` |
| IP-2 course code | Not specified in portal materials — identified by official name throughout |
| Batch syllabus alignment | ✓ Verified against 7 semester-wise portal registration screenshots (Semesters I–VII) |
| REDUCE and ADD proposals | Proposed only — require formal curriculum committee approval before implementation |
| Assessment reform (60/40 practical split) | Proposed only — requires university assessment regulations review |

---

*FEEDBACK_AND_LIMITATIONS.md | Task 2 | HKAIVERSE Round 2 | 24 October 2026*
