# Program to ask user to enter and verify password.

password = input("Please create your password: ")
while len(password) < 6:
    password = input("The password must contain at least 6 characters. Please recreate your password: ")

temp = input("Please verify your password: ")
while temp != password:
    temp = input("Sorry, your verification goes wrong. Please enter the same password as the one you just created: ")
# else:
len_of_password = len(password)
asterisks = "*" * (len_of_password - 4)
print(f"Okay, your password is: {password[:2]}{asterisks}{password[-2:]}. Keep in mind!")


user_input = input("\nWelcome to The National Treasure. Please, enter your password: ")
while user_input != password:
        print("Sorry, the password is wrong.")
        user_input = input("Please, reenter your password: ")
else:
    print("Now you have access to the National Treasure!")
