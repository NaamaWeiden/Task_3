import string

def is_coorect_password(password):
    if len(password) < 8:
        return False

    if not any(ch.islower() for ch in password):
        return False

    if not any(c.isupper() for c in password):
        return False

    if not any(c.isdigit() for c in password):
        return False

    special_characters = string.punctuation  
    if not any(c in special_characters for c in password):
        return False

    for c in set(password):
        if password.count(c) > 2:
            return False


    for i in range(len(password) - 2):
        seq = password[i:i+3]
        if seq.isalpha() or seq.isdigit():
            seq_lower = seq.lower()
            if ord(seq_lower[0])+1 == ord(seq_lower[1]) and ord(seq_lower[1])+1 == ord(seq_lower[2]):
                return False
            if seq.isdigit() and int(seq[0])+1 == int(seq[1]) and int(seq[1])+1 == int(seq[2]):
                return False

    return True

user_password = input("  enter password to check: ")
if is_coorect_password(user_password):
    print("✅ the password is correct!")
else:
    print("❌ the password is not correct")
