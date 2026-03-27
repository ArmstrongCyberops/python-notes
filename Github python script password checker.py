import re

def check_password_strength(password):
    strength = "Weak"

    if len(password) >= 8:
        if (re.search("[a-z]", password) and
            re.search("[A-Z]", password) and
            re.search("[!@#$%^&*(),.?\":{}|<>]", password)):
            strength = "Strong"
        else:
            strength = "Moderate"

    return strength


password = input("Enter a password to check:  ")

result = check_password_strength(password)

print(f"Password strength: {result}")
