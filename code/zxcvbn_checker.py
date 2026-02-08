from zxcvbn import zxcvbn

def zxcvbn_check(password):
    result = zxcvbn(password)
    return result["score"] 
