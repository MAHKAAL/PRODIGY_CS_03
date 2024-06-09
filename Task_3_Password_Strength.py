import re

def check_password_strength(password):

    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    strength = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if strength == 5:
        return "Strong password"
    elif strength >= 3:
        return "Moderate password"
    else:
        return "Weak password"

# Example usage
password = input("Enter your Password here:  ")
print(check_password_strength(password))