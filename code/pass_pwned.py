from collections import Counter
import hashlib
import requests
from getpass import getpass

def has_repeated_letters(password):
    password = password.lower()
    seq_len = 4
    freq = Counter(password)
    for char, count in freq.items():
        if char.isalpha() and count > 3:
            return True
        
    for i in range(len(password) - seq_len + 1):
        chunk = password[i:i+seq_len]

        if all(ord(chunk[j]) + 1 == ord(chunk[j+1]) for j in range(len(chunk)-1)):
            return True

        if all(ord(chunk[j]) - 1 == ord(chunk[j+1]) for j in range(len(chunk)-1)):
            return True

        if chunk.isdigit() and all(int(chunk[j]) + 1 == int(chunk[j+1]) for j in range(len(chunk)-1)):
            return True

        if chunk.isdigit() and all(int(chunk[j]) - 1 == int(chunk[j+1]) for j in range(len(chunk)-1)):
            return True
    return False   
   
def password_strength(password):

    if len(password) < 8:
        return "Length too short"
    
    elif password.islower() or password.isupper():
        return "Password must contain both uppercase and lowercase letters"
    
    elif not any(char.isdigit() for char in password):
        return "Password must contain at least one digit"

    elif not any(char in "!@#$%^&*()_+-={}[]?<>,./:;'" for char in password):
        return "Password must contain at least one special character."
    return "Strong"	

def pass_pwned_check(password):
    return {
        "breached": False,
	"repeating_letters" : has_repeated_letters(password),
        "reason": password_strength(password)
    }
