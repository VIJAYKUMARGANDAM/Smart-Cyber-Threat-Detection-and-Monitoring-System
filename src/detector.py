from src.alert import send_alert

failed_attempts = 0

def detect_threat(activity):
    global failed_attempts

    if activity == "login_fail":
        failed_attempts += 1

        print(f"[DEBUG]: Failed attempts = {failed_attempts}")

        if failed_attempts >= 3:
            send_alert("Brute Force Attack Detected!")
    else:
        failed_attempts = 0