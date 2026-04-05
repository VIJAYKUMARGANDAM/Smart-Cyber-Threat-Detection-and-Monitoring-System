from src.auth import login
from src.monitor import monitor_activity

def main():
    print("=== Smart Cyber Threat Detection System ===")

    if login():
        print("✅ Login successful!")
        monitor_activity()
    else:
        print("❌ Invalid credentials")

if __name__ == "__main__":
    main()