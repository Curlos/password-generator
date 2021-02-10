from random import choice, randint
import string
from pprint import pprint

passwords_and_sites = {}


def validate_password(password):
    special_char = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    if len(password) < 16:
        print('length should be at least 6')
        return False

    if len(password) > 127:
        print('length should be not be greater than 8')
        return False

    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        return False

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        return False

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        return False

    if not any(char in special_char for char in password):
        print('Password should have at least one of the symbols $@#')
        return False

    return True


def generate_password():
    ''' Generates a password that meets the following requirements:
    - Has at least one lowercase letter
    - Has at least one uppercase letter
    - Has at least one digit
    - Has at least one symbol 
    - Has at least one special character, e.g., ! @ # ? $
    - Has at least 16 characters but at most 120 characters '''

    all_char = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + \
        string.ascii_lowercase + string.ascii_uppercase + '0123456789'
    all_char_list = [char for char in all_char]
    password_length = randint(16, 127)
    password_use = input(
        'What website or app will this password be used for?\n')

    while True:
        password = ''
        for i in range(password_length):
            password += choice(all_char_list)

        if(validate_password(password)):
            passwords_and_sites[password_use] = password
            print(f"New password created for '{password_use}': {password}")
            break

    return password


# generate password for 3 different websites
for i in range(3):
    generate_password()

print('Saved passwords for all your sites/apps')

for site, password in passwords_and_sites.items():
    print(f"'{site}': '{password}'")
