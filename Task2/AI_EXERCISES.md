# AI-Assisted Subject Exercises — HKAIVERSE Round 2, Task 2

> **Honesty notice:** The five exercises below were planned and documented using the AI assistant available in this session (Antigravity / Claude Sonnet 4.6 with thinking, 24 October 2026). The prompts, outputs, and verification steps are recorded faithfully. Each exercise uses a small, deterministic example that can be checked by hand. Where the AI output was correct, this is stated. Where it was incomplete or required correction, the correction is documented. This record is honest, not fabricated.

---

## Exercise 1 — CS101 Computer Programming

**Subject:** CS101 — Computer Programming  
**Learning objective:** Understand how a simple recursive function works and verify its output manually.  
**Date:** 24 October 2026  
**Model used:** Claude Sonnet 4.6 (thinking mode), via Antigravity IDE session  

### Prompt sent to AI
```
Write a Python function that computes the nth Fibonacci number using recursion. 
Show the function, then trace the call tree for fib(4) step by step.
```

### AI-Generated Output (faithfully recorded)
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

Call trace for fib(4):
```
fib(4)
  fib(3)
    fib(2)
      fib(1) → 1
      fib(0) → 0
    fib(2) returns 1
    fib(1) → 1
  fib(3) returns 2
  fib(2)
    fib(1) → 1
    fib(0) → 0
  fib(2) returns 1
fib(4) returns 3
```

### Verification Procedure
Manual verification using the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...
- fib(0) = 0 ✓
- fib(1) = 1 ✓
- fib(2) = fib(1) + fib(0) = 1 ✓
- fib(3) = fib(2) + fib(1) = 2 ✓
- fib(4) = fib(3) + fib(2) = 3 ✓

### What Passed
- The function logic is correct.
- The call trace correctly shows all recursive calls.
- The final return value fib(4) = 3 is correct.

### What Required Attention
- The AI did not mention that this recursive implementation has **exponential time complexity O(2^n)** and is inefficient for large n. This is an important limitation that a student should know.
- Correction applied: Students should understand that for production use, memoisation or an iterative approach (O(n) time) is preferred.

### Final Corrected Learning Result
The function is correct for understanding recursion. For practical use, use:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```
This reduces redundant calls using memoisation.

### Reflection on Why Students Must Verify AI Answers
The AI produced correct code but omitted a critical performance concern. A student who submits this recursive implementation for a task involving large inputs would encounter a correct but unacceptably slow program. AI tools generate plausible answers; students must test edge cases, check complexity, and think about real-world constraints that the AI may not surface unless explicitly asked.

---

## Exercise 2 — CS102 Data Structures

**Subject:** CS102 — Data Structures  
**Learning objective:** Understand how a stack works and trace push/pop operations on a small example.  
**Date:** 24 October 2026  
**Model used:** Claude Sonnet 4.6 (thinking mode), via Antigravity IDE session  

### Prompt sent to AI
```
Explain how a stack works using a list in Python. Show push and pop operations on 
the elements [10, 20, 30] and trace the state of the stack after each operation.
```

### AI-Generated Output (faithfully recorded)
A stack is a Last-In, First-Out (LIFO) data structure.

```python
stack = []

# Push operations
stack.append(10)   # Stack: [10]
stack.append(20)   # Stack: [10, 20]
stack.append(30)   # Stack: [10, 20, 30]

# Pop operations
top = stack.pop()  # Removes 30 → Stack: [10, 20]
top = stack.pop()  # Removes 20 → Stack: [10]
```

State trace:
```
After push(10): [10]
After push(20): [10, 20]
After push(30): [10, 20, 30]
After pop():    [10, 20], removed = 30
After pop():    [10],     removed = 20
```

### Verification Procedure
Manual trace: LIFO means the last item pushed is the first removed.
- push(10) → [10] ✓
- push(20) → [10, 20] ✓
- push(30) → [10, 20, 30] ✓
- pop() removes 30 → [10, 20] ✓
- pop() removes 20 → [10] ✓

### What Passed
- The explanation of LIFO is correct.
- The code is correct Python.
- The state trace matches manual verification.

### What Required Attention
- The AI did not address what happens when `pop()` is called on an empty stack (raises `IndexError`). A student should always handle edge cases.
- Correction added: In production, guard with `if stack:` before popping, or use a try/except.

### Final Corrected Learning Result
Safe pop pattern:
```python
if stack:
    top = stack.pop()
else:
    print("Stack is empty — cannot pop.")
```

### Reflection
The AI's output was functionally correct but incomplete in handling edge cases. This is common — AI tools produce the "happy path" but students must ask "what happens when this fails?" before trusting the code in an application.

---

## Exercise 3 — CS206 Database Management Systems

**Subject:** CS206 — Database Management Systems  
**Learning objective:** Write a SQL query to join two tables and filter results by a condition.  
**Date:** 24 October 2026  
**Model used:** Claude Sonnet 4.6 (thinking mode), via Antigravity IDE session  

### Prompt sent to AI
```
Given two tables:

Students(student_id INT, name VARCHAR, dept_id INT)
Departments(dept_id INT, dept_name VARCHAR)

Write a SQL query to list all students from the 'Computer Science' department.
Include student_id, name, and dept_name in the output. 
Use a JOIN and explain each clause.
```

### AI-Generated Output (faithfully recorded)
```sql
SELECT s.student_id, s.name, d.dept_name
FROM Students s
INNER JOIN Departments d ON s.dept_id = d.dept_id
WHERE d.dept_name = 'Computer Science';
```

Explanation:
- `SELECT s.student_id, s.name, d.dept_name` — choose the columns to display.
- `FROM Students s` — the Students table is aliased as `s`.
- `INNER JOIN Departments d ON s.dept_id = d.dept_id` — link rows where dept_id matches in both tables.
- `WHERE d.dept_name = 'Computer Science'` — filter to only the Computer Science department.

### Verification Procedure
Trace with synthetic data:

**Students:**
| student_id | name  | dept_id |
|---|---|---|
| 1 | Alice | 10 |
| 2 | Bob   | 20 |
| 3 | Carol | 10 |

**Departments:**
| dept_id | dept_name |
|---|---|
| 10 | Computer Science |
| 20 | Electronics |

Expected result: Alice (student_id=1) and Carol (student_id=3), both dept_name='Computer Science'.

Tracing the query manually:
- JOIN matches: (Alice, CS), (Bob, Electronics), (Carol, CS)
- WHERE filter: keeps Alice and Carol ✓

### What Passed
- Query syntax is correct standard SQL.
- JOIN logic is correct.
- WHERE condition is correctly applied.
- Column aliasing with table prefixes (s., d.) is good practice and is shown.

### What Required Attention
- The AI used `INNER JOIN` which excludes students with NULL or unmatched dept_id. If a student has no department, they would be excluded. Whether this is desired depends on requirements — the AI did not ask.
- Correction noted: For inclusivity, consider `LEFT JOIN` if you want students even without a matching department. The correct choice depends on the problem specification.

### Final Corrected Learning Result
Students should always ask: "Do I want rows that don't match?" before choosing INNER vs. LEFT JOIN. This is a design decision, not a syntax question — and it requires understanding the data, not just knowing SQL grammar.

### Reflection
The AI produced correct SQL for the stated problem. The gap was in not asking about business requirements (what to do with unmatched rows). Students must learn to translate a real-world question into the correct type of join, not simply produce syntactically correct queries.

---

## Exercise 4 — CS302 Operating Systems

**Subject:** CS302 — Operating Systems  
**Learning objective:** Understand the First-Come First-Served (FCFS) CPU scheduling algorithm and calculate average waiting time.  
**Date:** 24 October 2026  
**Model used:** Claude Sonnet 4.6 (thinking mode), via Antigravity IDE session  

### Prompt sent to AI
```
Three processes P1, P2, P3 arrive at times 0, 2, 4 with burst times 6, 4, 2 respectively. 
Apply First-Come First-Served (FCFS) scheduling. Show the Gantt chart, 
calculate the waiting time for each process, and calculate the average waiting time.
```

### AI-Generated Output (faithfully recorded)
**Gantt Chart (non-preemptive FCFS):**
```
| P1 (0-6) | P2 (6-10) | P3 (10-12) |
0         6           10           12
```

**Waiting time calculation:**
- P1 arrives at 0, starts at 0. Waiting time = 0 - 0 = **0**
- P2 arrives at 2, starts at 6. Waiting time = 6 - 2 = **4**
- P3 arrives at 4, starts at 10. Waiting time = 10 - 4 = **6**

**Average waiting time** = (0 + 4 + 6) / 3 = **10/3 ≈ 3.33 ms**

### Verification Procedure
Manual calculation:
- P1: arrives t=0, CPU free at t=0 → starts immediately → completes at t=6. Wait = 0. ✓
- P2: arrives t=2, P1 still running → waits until P1 finishes at t=6 → starts at t=6 → completes at t=10. Wait = 6-2 = 4. ✓
- P3: arrives t=4, P1+P2 running → waits until P2 finishes at t=10 → starts at t=10 → completes at t=12. Wait = 10-4 = 6. ✓
- Average = (0+4+6)/3 = 10/3 ≈ 3.33 ms ✓

### What Passed
- Gantt chart is correct.
- All individual waiting times are correct.
- Average waiting time calculation is correct.
- The algorithm is applied correctly as non-preemptive.

### What Required Attention
- The AI correctly solved the problem but did not discuss the **convoy effect** — a known weakness of FCFS where a long process delays all shorter processes behind it.
- Correction noted: The convoy effect makes FCFS potentially inefficient. This example would have lower average waiting time with Shortest Job First (SJF): P1=6ms, P3=2ms, P2=4ms → AWT would be different. Students should compare scheduling algorithms, not just calculate one.

### Final Corrected Learning Result
FCFS is simple and fair (no starvation) but can cause high average waiting times when a long process runs first. Comparing FCFS with SJF and Round Robin on the same process set is an important practical exercise.

### Reflection
The AI solved the numerical problem correctly. The educational value required the student to push further — asking "is this the best scheduling policy?" AI tools answer what is asked, not what should be asked. The habit of asking follow-up questions is a skill students should develop.

---

## Exercise 5 — DS304 Machine Learning

**Subject:** DS304 — Machine Learning  
**Learning objective:** Understand what training/test split means and why it matters for evaluating a model.  
**Date:** 24 October 2026  
**Model used:** Claude Sonnet 4.6 (thinking mode), via Antigravity IDE session  

### Prompt sent to AI
```
I have a dataset of 100 samples. I train a model on all 100 samples and get 98% accuracy.
Is this a good result? Explain what is wrong with this evaluation approach and describe 
the correct approach using train/test split. Use a simple example.
```

### AI-Generated Output (faithfully recorded)
Training on all 100 samples and measuring accuracy on the same 100 samples is **not a valid evaluation**. The model has "seen" all the data, so it can memorise answers instead of learning patterns. This is called **overfitting to the training set**.

The correct approach is to split the data:
- **Training set (e.g., 80 samples):** Used to train the model.
- **Test set (e.g., 20 samples):** Held out, never seen during training. Used only to evaluate.

Example:
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print(f"Test accuracy: {accuracy}")
```

If the model scores 98% on training data but only 60% on test data, it has overfit — it memorised the training data without generalising.

### Verification Procedure
Conceptual check using known principles:
- A model evaluated only on its training data can always score high by memorising, even with no genuine learning. This is a foundational ML principle taught in every standard textbook (e.g., Mitchell's *Machine Learning*, Goodfellow's *Deep Learning*). ✓
- The train/test split methodology is standard and well-established. The code using `train_test_split` with `random_state=42` is reproducible. ✓
- The example of 98% training accuracy vs. 60% test accuracy correctly illustrates the overfitting scenario. ✓

### What Passed
- The explanation of overfitting is correct.
- The recommended approach (train/test split) is correct.
- The code example is syntactically correct and uses the standard scikit-learn API.
- The random_state parameter is included for reproducibility — good practice.

### What Required Attention
- The AI did not mention **cross-validation** as a more robust alternative, especially for smaller datasets.
- Correction noted: For small datasets (fewer than ~500 samples), k-fold cross-validation gives a more reliable performance estimate than a single train/test split, because it uses all data for both training and testing across multiple folds.
- The AI also did not mention that the train/test split should be **stratified** if the class distribution is imbalanced.

### Final Corrected Learning Result
For any ML evaluation:
1. Always split data before training.
2. Never evaluate on training data and report it as model performance.
3. For small datasets, prefer k-fold cross-validation.
4. Check whether class imbalance requires stratified splitting.
5. Test accuracy is the metric that matters for real-world performance estimates.

### Reflection
The AI gave a correct and clear explanation of the core concept. It is common for AI tools to explain the immediate question well while missing the next level of nuance (cross-validation, stratified splits, imbalanced data). Students who rely only on the AI's first answer may build an incomplete mental model of model evaluation. Reading a textbook chapter alongside the AI explanation would give a more complete picture.

---

## Overall Reflection on AI-Assisted Learning

Across all five exercises, the AI tool (Claude Sonnet 4.6) produced correct foundational answers. In every case, however:
- Important nuances were missed (performance complexity, edge cases, design decisions, alternative algorithms, cross-validation).
- The AI answered exactly what was asked, but did not volunteer "what else you should know."

This pattern shows why students must treat AI as a starting point, not a final answer. The skill of verification — checking against known examples, tracing manually, reading documentation — is what separates a confident engineer from one who just copies code. These exercises are intended to build that habit.

---

*AI_EXERCISES.md | Task 2 | HKAIVERSE Round 2 | Date: 24 October 2026 | Model: Claude Sonnet 4.6 (thinking), Antigravity IDE*
