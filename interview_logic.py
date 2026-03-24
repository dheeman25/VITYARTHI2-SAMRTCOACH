import time
import os

def load_questions(filepath="../data/questions.txt"):
    """Reads questions from a text file into a list."""
    if not os.path.exists(filepath):
        print(f"\nWarning: Question database not found at {filepath}.")
        # Fallback questions if the input file is missing
        return ["Fallback Technical Q: Define a Class.", "Fallback HR Q: Describe your greatest weakness."]
    
    with open(filepath, 'r') as f:
        # Load non-empty lines, stripping whitespace
        questions = [line.strip() for line in f if line.strip()]
    return questions

def get_valid_score(metric_name):
    """Robustly requests a 1.0 - 5.0 float from the user, ensuring validation."""
    while True:
        try:
            prompt = f"Self-Report {metric_name} score (1.0 Poor - 5.0 Perfect): "
            val = float(input(prompt))
            if 1.0 <= val <= 5.0:
                return val
            print("Error: Input must be between 1.0 and 5.0.")
        except ValueError:
            print("Error: Invalid numeric input. Use decimals (e.g., 3.5).")

def run_simulation(username, questions):
    """Executes the interview flow and collects simulated data."""
    if not questions:
        print("Error: No questions available. Ending simulation.")
        return None

    # Storage for collected simulation scores
    session_data = {'scores': {'eye': [], 'post': [], 'clarity': []}}
    
    print(f"\n--- SMARTCOACH: Interview Session Starting for {username} ---")
    time.sleep(1)

    for i, q in enumerate(questions):
        print(f"\nQUESTION {i+1}: {q}")
        input("Press ENTER when you are ready to answer...")
        
        # Simulate Answer Time (Simple pause replacing real-time capture)
        print("(Simulating answer capture...)")
        time.sleep(2)
        
        # --- INPUT SIMULATION PHASE (Replacing Real-time AI) ---
        print("\n>> Input Performance Indicators <<")
        session_data['scores']['eye'].append(get_valid_score("Eye Contact"))
        session_data['scores']['post'].append(get_valid_score("Posture"))
        session_data['scores']['clarity'].append(get_valid_score("Verbal Clarity (Minimal Fillers)"))
        
    return session_data

def finalize_and_log_session(username, session_data):
    """Analyzes data using placeholder rules, displays feedback, and logs results."""
    if not session_data: return

    # Calculate basic averages (Our simulated 'analysis')
    num_q = len(session_data['scores']['eye'])
    avg_eye = sum(session_data['scores']['eye']) / num_q
    avg_post = sum(session_data['scores']['post']) / num_q
    avg_clarity = sum(session_data['scores']['clarity']) / num_q

    # --- RULE-BASED FEEDBACK (Placeholder logic for eventual AI metrics) ---
    feedback_report = []
    
    # Eye Contact Logic
    if avg_eye >= 4.0:
        ec_status = "EXCELLENT: Strong eye contact, showing confidence."
    elif avg_eye >= 2.5:
        ec_status = "GOOD: Good, but remember to look at the screen/camera consistently."
    else:
        ec_status = "IMPROVE: Look forward when speaking to engage the interviewer."
        
    # Posture Logic
    if avg_post >= 4.0:
        p_status = "GOOD POSTURE: Professional and upright."
    else:
        p_status = "IMPROVE POSTURE: Sit straight. Slouching can reduce perceived authority."
        
    # Verbal Clarity Logic (1-5 scale: 5=Few Fillers)
    if avg_clarity >= 4.0:
        vc_status = "CLARITY: Minimal filler words detected. Clear articulation."
    elif avg_clarity >= 2.5:
        vc_status = "INFO: Moderate filler words. Practice using pauses deliberately."
    else:
        vc_status = "ALERT: Frequent filler words. Practice slowing down your speech."

    # Compile feedback for display
    feedback_report.append(f"\n--- SMARTCOACH FINAL REPORT ({username}) ---")
    feedback_report.append(f"Performance: Eye={avg_eye:.1f}, Post={avg_post:.1f}, Clarity={avg_clarity:.1f}")
    feedback_report.append("-" * 35)
    feedback_report.append(ec_status)
    feedback_report.append(p_status)
    feedback_report.append(vc_status)
    feedback_report.append("=" * 35)

    # Output to screen
    for line in feedback_report: print(line)

    # --- LOGGING PHASE (Persistent Data Storage) ---
    try:
        if not os.path.exists("../data/"): os.makedirs("../data/")
        
        with open("../data/session_logs.txt", "a") as logfile:
            # Create a timestamp
            timestamp = time.strftime("%Y-%m-%d %H:%M")
            logfile.write(f"SESSION: {timestamp} | User: {username}\n")
            logfile.write(f"Averages: Eye={avg_eye:.1f}, Posture={avg_post:.1f}, Clarity={avg_clarity:.1f}\n")
            logfile.write("--------------------------------\n\n")
        print("\nSession summary logged to data/session_logs.txt.")
    except Exception as e:
        print(f"\nError logging session: {e}")
