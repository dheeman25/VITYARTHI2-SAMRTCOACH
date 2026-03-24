import sys
import interview_logic as coach  # Import our procedural logic module

def show_menu():
    print("\n" + "="*40)
    print("      SMARTCOACH: JOB INTERVIEW SIM      ")
    print("       (1st Year / 2nd Sem Project)      ")
    print("="*40)
    print("1. Start Mock Interview Session")
    print("2. View Session Logs")
    print("3. Exit")
    print("-" * 40)

def main():
    # Application State variables
    username = None

    while True:
        show_menu()
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            # Initialize or reuse username
            if not username:
                username = input("Enter your name to begin: ")
                if not username.strip(): username = "Guest"
            
            # --- 1. INPUT PHASE: Load questions ---
            print("\nLoading interview questions...")
            questions = coach.load_questions()
            
            # --- 2. PROCESS PHASE: Run simulation flow ---
            session_data = coach.run_simulation(username, questions)
            
            # --- 3. OUTPUT PHASE: Analyze, display, and log ---
            if session_data:
                coach.finalize_and_log_session(username, session_data)

        elif choice == '2':
            # Simplified log viewer
            if not os.path.exists("../data/session_logs.txt"):
                print("\nNo logs found. Complete a session first!")
            else:
                try:
                    with open("../data/session_logs.txt", 'r') as f:
                        print("\n--- PAST SESSION LOGS ---")
                        print(f.read())
                        print("-" * 25)
                except Exception as e:
                    print(f"Error reading logs: {e}")

        elif choice == '3':
            print("\nExiting SMARTCOACH. Keep practicing!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
