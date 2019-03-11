# Program to perform the same task as the print() statement shown below using a while/for loop
# print("\n\n       ! ! ! No Cheating ! ! !\n" * 10, end="")
# print("If at first you don't succeed, try, try, try again.")

# Version 1, using a while loop:
str = ""
t = 1
while t <= 10:
    str += "\n\n       ! ! ! No Cheating ! ! !\n"
    t += 1
print(str, end="")
print("If at first you don't succeed, try, try, try again.")

# Version 2, using a while loop:
str = ""
t = 0
while t < 10:
    str += "\n\n       ! ! ! No Cheating ! ! !\n"
    t += 1
print(str, end="")
print("If at first you don't succeed, try, try, try again.")

# Version 3, using a for loop:
str = ""
for t in range(10):
    str += "\n\n       ! ! ! No Cheating ! ! !\n"
print(str, end="")
print("If at first you don't succeed, try, try, try again.")

