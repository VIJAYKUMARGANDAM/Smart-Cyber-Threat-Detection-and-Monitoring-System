from src.logger import log_event
from src.detector import detect_threat

def monitor_activity():
    print("\n=== Monitoring Started ===")
    print("Commands: login_fail / normal / view_logs / view_threats / exit\n")

    while True:
        activity = input("Enter activity: ")

        if activity == "exit":
            print("Monitoring stopped.")
            break

        elif activity == "view_logs":
            with open("../data/logs.txt", "r") as f:
                print("\n--- LOGS ---")
                print(f.read())

        elif activity == "view_threats":
            with open("../data/threats.txt", "r") as f:
                print("\n--- THREATS ---")
                print(f.read())

        else:
            log_event(activity)
            detect_threat(activity)