import random
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    if length < 4:
        print("Your password is very weak, use atleast 8 Characters!")
    else:
        for i in range(length):
            password += random.choice(characters)

    return password 



length = int(input("Password ki length batao: "))
password = password_generator(length)
print(f"Your Password: {password}")