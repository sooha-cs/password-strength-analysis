def regex_check(password):
    sequences = [
        "abcdefghijklmnopqrstuvwxyz",
        "0123456789",
        "qwertyuiopasdfghjklzxcvbnm"
    ]

    pw = password.lower()

    for seq in sequences:
        for i in range(len(seq) - 3):
            if seq[i:i+4] in pw:
                return True
    return False
