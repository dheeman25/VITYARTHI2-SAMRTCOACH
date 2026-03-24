# SMARTCOACH SIMULATOR

**Project By:** [DHEEMAN ACHARJEE]
**Academic Submission:** 1st Year / 2nd Semester Project

---

## 1. What is it?
SMARTCOACH is a terminal-based tool that helps users plan, track, and analyze their workouts. It acts like a basic digital coach by taking your session details (exercise, sets, reps) and your self-reported form quality to provide simple, instant feedback.

It focuses on implementing fundamental programming concepts (Objects, Files, and Loops) in Python.

## 2. Key Features

### User Features (What you can do):
- **Start a Workout:** Choose an exercise (e.g., Bicep Curls) and plan your goal (sets/reps).
- **Log Sets:** After each set, input the actual reps you achieved and rate your form quality (1-5).
- **Receive Coaching Feedback:** Get instant text alerts if your form is failing or fatigue is detected.
- **View History:** See a list of all your past logged sessions.

### System Performance (How it works):
- **Simple Interface:** Easy-to-use, text-based menu (no complex GUI or webcam needed).
- **Reliable Input:** Handles typos or invalid numbers gracefully (e.g., won't crash if you enter "ten" instead of 10).
- **Persistent Storage:** Saves your data to a text file so your progress is kept when you restart.
- **Fast:** Executes commands instantly on any computer.

## 3. Technologies Used
- **Python 3.x:** Core programming language.
- **Standard Library:** Uses built-in `time` and `os` modules.

## 4. How to Run

1.  Open your Terminal (or Command Prompt).
2.  Navigate into the project’s `src/` folder.
3.  Run the main application:
    ```bash
    python main.py
    ```

## 5. Usage Preview

When you run the simulator, you will follow this flow:

```text
========================================
       SMARTCOACH SIMULATOR v1.0
========================================

Main Menu:
1. Start New Workout Session
2. View History Logs
3. Exit
Enter choice (1-3): 1

Enter User Name: Alex
Enter Exercise Name: Bicep Curls
How many sets are planned? 3
Enter target reps per set: 10

Starting session for Alex - Bicep Curls...

--- SET 1 ---
Perform Bicep Curls set. Press ENTER when finished...
How many reps did you achieve? (Target: 10): 10
Self-Report Form Quality (1=Poor, 5=Perfect): 5

>> Coach Feedback: GOOD JOB: Form maintained, rep target met.
