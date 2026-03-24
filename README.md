# SMARTCOACH (Job Interview Sim)

**Project By:** [DHEEMAN ACHARJEE]
**Academic Submission:** 1st Year / 2nd Semester Project

---

## 1. Project Overview

SMARTCOACH is an interactive, terminal-based application designed to simulate a job interview environment for college students. It presents common interview questions, requests that users simulate their verbal and physical responses, and then allows users to self-report performance metrics (scale of 1.0 - 5.0) for critical presentation areas: **Eye Contact, Posture, and Verbal Clarity.**

The system uses rule-based placeholder logic (simulating eventual AI behavior) to analyze the provided scores and generate informative, formative feedback to help users improve their performance. A summary of each session is saved to a persistent local text file (`data/session_logs.txt`) for tracking progress.

This project focuses on implementing fundamental programming concepts (procedural logic, control flow, functions, and File I/O) in Python, adhering to a modular structure suitable for a first-year college evaluation.

---

## 2. System Requirements Specification

This section defines the mandatory operational behavior (Functional) and constraints (Non-Functional) that the SMARTCOACH system must satisfy.

### 2.1 Functional Requirements (FR)
*These requirements specify what the system must do:*

- **FR-01 Question Loading:** The system shall load interview questions from a dedicated external text file (`data/questions.txt`).
- **FR-02 Session Initialization:** The user must be able to input their name to initialize a session.
- **FR-03 Interactive Flow:** The system must sequentially present questions and pause for the user to simulate their response before advancing.
- **FR-04 Simulation Metrics Capture:** After each simulated response, the system shall prompt the user to self-report scores (1.0 Poor - 5.0 Perfect) for Eye Contact, Posture, and Verbal Clarity.
- **FR-05 Feedback Generation:** The system shall calculate session averages and generate distinct text-based coaching feedback based on predefined logical thresholds for each metric.
- **FR-06 Session Logging:** The system must save the finalized session results (timestamp, averages, and user name) to a persistent local text file (`data/session_logs.txt`).
- **FR-07 Log Retrieval:** The main menu must provide an option to view the history of logged sessions stored in the log file.

### 2.2 Non-Functional Requirements (NFR)
*These requirements specify operational quality and constraints:*

- **NFR-01 Usability:** The application must utilize a clear, menu-driven Command-Line Interface (CLI). All data input prompts must explicitly state the required input type and logical range (e.g., 1.0 - 5.0 scale).
- **NFR-02 Reliability (Input Validation):** The system must handle incorrect inputs (e.g., entering "good" instead of a number, or entering a score of 10) using robust exception handling (`try-except`) and input loops, without crashing.
- **NFR-03 Performance:** Since all complex AI processing is simplified, feedback generation and file logging must execute near-instantly (<100ms) on standard consumer hardware.
- **NFR-04 Portability:** The software must execute on any operating system with a standard Python 3.x interpreter, utilizing only built-in standard libraries (`time`, `os`, `sys`).
- **NFR-05 Maintainability:** The source code must be modular, separating application flow (`main.py`) from procedural logic and data handling (`interview_logic.py`).

---

## 3. Technologies Used
- **Programming Language:** Python 3.x
- **Modules:** `time` (for timestamps), `os` (for file checking and directory creation), `sys` (for application control).
- **Data Persistence:** Persistent Text File I/O for input (`questions.txt`) and output (`session_logs.txt`).

---

## 4. How to Run

### 4.1 Prerequisites
- Ensure Python 3.x is installed on your computer.

### 4.2 Preparation (Crucial Step)
1.  Navigate to the `data/` folder in your project directory.
2.  If it does not exist, create a file named `questions.txt`.
3.  Add 3-5 sample interview questions to this file (one per line).

### 4.3 Execution
1.  Open your Terminal (or Command Prompt).
2.  Navigate into the project’s `src/` folder.
3.  Run the main application file:
    ```bash
    python main.py
    ```

## 5. Usage Flow Preview

This is the simplified output of a SMARTCOACH session:

```text
========================================
      SMARTCOACH: JOB INTERVIEW SIM
========================================
1. Start Mock Interview Session
2. View Session Logs
3. Exit
----------------------------------------
Enter choice (1-3): 1

Enter your name to begin: Sarah

Loading interview questions...

QUESTION 1: Technical: Describe the CRUD operations in a database.
Press ENTER when ready to answer...
(Simulating answer capture...)

>> Input Performance Indicators <<
Self-Report Eye Contact score (1.0 Poor - 5.0 Perfect): 2.5
Self-Report Posture score (1.0 Poor - 5.0 Perfect): 4.5
Self-Report Verbal Clarity (Minimal Fillers) score (1.0 Poor - 5.0 Perfect): 3.0

[...] <-- (Workflow repeats for remaining questions)

--- SMARTCOACH FINAL REPORT (Sarah) ---
Performance: Eye=3.0, Post=4.2, Clarity=3.3
-----------------------------------
GOOD: Good, but remember to look at the screen/camera consistently.
GOOD POSTURE: Professional and upright.
INFO: Moderate filler words. Practice using pauses deliberately.
===================================

Session summary logged to data/session_logs.txt.
