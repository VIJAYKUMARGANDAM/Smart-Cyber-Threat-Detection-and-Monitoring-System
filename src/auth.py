def login():
    print("\n=== LOGIN ===")
    
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Simple hardcoded auth (can improve later)
    if username == "admin" and password == "admin":
        return True
    else:
        return False