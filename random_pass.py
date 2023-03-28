import random
import string
# pass1 = int(input("Enter the length of the password:"))
pass1=8

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = random.choice(lower) + random.choice(upper) + \
               random.choice(digits) + random.choice(symbols)

    password += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length-4))

    password = ''.join(random.sample(password, len(password)))

    return password


print(generate_password(pass1))
