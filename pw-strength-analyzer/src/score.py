import math
import re

COMMON_PASSWORDS = ["123456","password","qwerty","abc123","letmein"]

def analyze(pw: str):
    if not pw:
        return {"label": "Invalid", "bits": 0}

    length = len(pw)
    lower = any(c.islower() for c in pw)
    upper = any(c.isupper() for c in pw)
    digit = any(c.isdigit() for c in pw)
    symbol = any(not c.isalnum() for c in pw)

    charset = (26 if lower else 0) + (26 if upper else 0) + (10 if digit else 0) + (33 if symbol else 0)
    bits = length * math.log2(charset) if charset else 0

    if pw in COMMON_PASSWORDS:
        return {"label": "Very weak", "bits": bits}

    if bits < 28:
        label = "Very weak"
    elif bits < 36:
        label = "Weak"
    elif bits < 60:
        label = "Okay"
    elif bits < 80:
        label = "Strong"
    else:
        label = "Very strong"

    return {"label": label}

if __name__ == "__main__":
    while True:
        pw = input("Enter a password (or q to quit): ")
        if pw.lower() == "q":
            break
        print(analyze(pw))
