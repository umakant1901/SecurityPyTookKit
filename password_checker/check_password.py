import re
import requests
import hashlib

def check_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search("[a-z]", password): score += 1
    if re.search("[A-Z]", password): score += 1
    if re.search("[0-9]", password): score += 1
    if re.search("[^a-zA-Z0-9]", password): score += 1
    return score

def check_breach(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1[:5]
    res = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    return sha1[5:] in res.text

# test it
if __name__ == "__main__":
    pwd = input("Enter password: ")
    print("Strength:", check_strength(pwd))
    print("Breached:", "Yes" if check_breach(pwd) else "No")
