import datetime
import os

LOG_FILE = "../data/logs.txt"

def log_event(activity):
    # Ensure data folder exists
    os.makedirs("../data", exist_ok=True)

    timestamp = datetime.datetime.now()
    log_entry = f"{timestamp} - {activity}\n"

    with open(LOG_FILE, "a") as file:
        file.write(log_entry)

    print(f"[LOGGED]: {activity}")