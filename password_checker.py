import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short (min 8 characters)": length_error,
        "No digit": digit_error,
        "No uppercase letter": uppercase_error,
        "No lowercase letter": lowercase_error,
        "No special character": symbol_error,
    }

    score = 5 - sum(errors.values())

    print("\nPassword Check Report:")
    for error, occurred in errors.items():
        if occurred:
            print(f"❌ {error}")
        else:
            print(f"✅ {error}")

    if score == 5:
        print("\nStrength: 🔐 Very Strong")
    elif score >= 3:
        print("\nStrength: 🔒 Medium")
    else:
        print("\nStrength: 🔓 Weak")

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()