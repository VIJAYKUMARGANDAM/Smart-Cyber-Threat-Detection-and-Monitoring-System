import datetime
import os

THREAT_FILE = "../data/threats.txt"

def send_alert(message):
    print(f"\n🚨 ALERT: {message}\n")

    # Ensure data folder exists
    os.makedirs("../data", exist_ok=True)

    timestamp = datetime.datetime.now()
    threat_entry = f"{timestamp} - {message}\n"

    with open(THREAT_FILE, "a") as file:
        file.write(threat_entry)