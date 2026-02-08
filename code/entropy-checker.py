import math
def entropy_check(password):
	if not password:
		return 0.0
	char_set = 0.0
	if any(c.lower() for c in password):
        	char_set+=26
	if any(c.upper() for c in password):
        	char_set+=26
	if any(c.isdigit() for c in password):
        	char_set+=10
	if any(not c.isalnum() for c in password):
        	char_set+=32
	entropy = len(password) * math.log2(char_set)
	return entropy
