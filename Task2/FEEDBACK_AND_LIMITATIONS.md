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

## 2. Personal Contribution

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

## 3. Limitations

### Curriculum Data Limitations
- The course dataset is student-supplied. I do not have access to the official printed or PDF syllabus for the 2023–2027 batch.
- HS301 is recorded as 0 credits. The Semester V portal screenshot (`assets/sem5_courses.png`) also shows HS301 with 0 credits, so the data is consistent with the source.
- IP-2 course code: the supplied curriculum materials do not specify a course code for Mandatory Internship-II. It is identified by name throughout this report.
- Prerequisites listed in this report are recommended academic dependencies, not officially mandated prerequisites.

### Job Description Limitations
- The three job descriptions are sourced from PDF files read directly with `pypdf`. Skills are extracted verbatim from the document text.
- Posting dates are not stated in any of the three PDFs; the document read date (24 October 2026) is recorded instead.
- The ACHNET document is named "Tescra" in the file name but describes the ACHNET organisation; both names appear to refer to the same company or a related entity. This ambiguity is noted but does not affect the skills extracted from the document.
- The JPMorgan and Joveo documents do not carry official company letterheads or unique job IDs that could be independently verified online.

### Calculation Limitations
- The 19.8% figure (Method A) sits at the lower boundary of the 20–25% target. A fully defensible result within the target range would require either more credit-allocation changes or confirmation that UPDATE redesigns genuinely meet the threshold.
- The REDUCE proposals require formal academic approval. Without approval, the credit total would remain unchanged and the new lab could not be funded from the programme's existing credit envelope without replacement elsewhere.

### Interactive Component Limitations
- The course explorer is a static HTML/CSS/JS file that runs locally in a browser without any server or API.
- The data in the explorer matches the proposal but is hardcoded. Any change to the proposal requires a corresponding update to the explorer data.
- Automated browser testing was not performed (browser tool unavailable in this session). Manual testing instructions are provided in `tests/test_checklist.md`.

### AI Exercise Limitations
- All five exercises were conducted in the same session (24 October 2026) using Claude Sonnet 4.6 in Antigravity IDE.
- The prompts, outputs, and verification steps are documented faithfully.
- These are learning exercises, not peer-reviewed research. The AI outputs were checked manually against known correct answers, but no formal testing framework was applied.

### Feedback Limitations
- Two informal conversations are described. No recordings, transcripts, or formal sign-offs exist.
- The graduation year and employer of the industry contact are not disclosed.
- Faculty name, department, and date of conversation are not disclosed.
- This feedback cannot be used as evidence of institutional endorsement.

---

## 4. Validation Status

| Item | Status |
|---|---|
| Curriculum screenshots vs. COURSE_MAP.csv | ✓ Verified — all seven screenshots reconciled in `CURRICULUM_SCREENSHOTS.md` |
| HS301 credit value | ✓ Consistent — screenshot shows 0; dataset uses 0 |
| Credit calculation (baseline and proposed) | ✓ Verified — automated test CE-08 confirms 167 / 167 / net 0 |
| Course explorer data alignment | ✓ Verified — all 15 automated test cases pass (`test_course_explorer.py`) |
| Job description skills vs. curriculum map | ✓ Done — three PDFs read directly; gap analysis in `JOB_DESCRIPTION_COMPARISON.md` |
| IP-2 course code | Not confirmed in available materials — identified by name throughout |
| Official IFHE batch syllabus document | Not verified — the official PDF could not be accessed; dataset remains student-supplied |
| REDUCE and ADD proposals | Proposed only — require formal curriculum committee approval before implementation |
| Assessment reform (60/40 practical split) | Proposed only — requires university assessment regulations review |

---

*FEEDBACK_AND_LIMITATIONS.md | Task 2 | HKAIVERSE Round 2 | 24 October 2026*
