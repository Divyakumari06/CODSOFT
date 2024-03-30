import string
import random

length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
         1. letters
         2. digits
         3. Special characters
         4. Exit''')

characterList = ""

while True:
    try:
        choice = int(input("Pick a number "))
        if choice == 1:
            characterList += string.ascii_letters
        elif choice == 2:
            characterList += string.digits
        elif choice == 3:
            characterList += string.punctuation
        elif choice == 4:
         break
        else:
            print("Please pick a valid option!")
    except ValueError:
        print("Invalid input. Please enter a number.")

password = []

for i in range(length):
    passchar = random.choice(characterList)
    password.append(passchar)

print("The password is:", ''.join(password))