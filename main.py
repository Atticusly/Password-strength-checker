import string
import getpass

def check_pwd():
    password = getpass.getpass("Enter Password: ")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0
    repeating_chars = False
    prev_char = ''

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

        if char == prev_char:  # Check for repeating characters
            repeating_chars = True
        prev_char = char

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    # Additional feedback for weaknesses
    if repeating_chars:
        remarks += "Your password contains multiple characters of the same type consecutively, which reduces its strength. "
    if lower_count < 2:
        remarks += "Your password should have at least two lowercase characters. "
    if upper_count < 2:
        remarks += "Your password should have at least two uppercase characters. "
    if num_count < 2:
        remarks += "Your password should have at least two numeric characters. "
    if wspace_count > 1:
        remarks += "Your password should avoid multiple whitespace characters. "
    if special_count < 2:
        remarks += "You should add more special characters to improve your password strength. "

    if strength == 1:
        remarks += "This is a bad password you should change it as fast as possible."
    elif strength == 2:
        remarks += "This is not a good password you should change it as fast as possible."
    elif strength == 3:
        remarks += "This is a weak password, consider changing."
    elif strength == 4:
        remarks += "This is a hard password, but can be better."
    elif strength == 5:
        remarks += "This is a very strong password."

    print('Your password has:')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")

    print(f"Password Strength: {strength}")
    print(f"Hint: {remarks}")

def ask_pwd(another_pwd=False):
    valid = False
    if another_pwd:
        choice = input('Do you want to enter another password? (y/n): ')
    else:
        choice = input('Do you want to check the strength of your password? (y/n): ')

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid, Try Again')

if __name__ == '__main__':
    print('Welcome to my password checker')
    ask_pw = ask_pwd()
    while ask_pw:
        check_pwd()
        ask_pw = ask_pwd(True)
