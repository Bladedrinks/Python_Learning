# ------ Program Introduction ------
# Program to check if an base-10 integer is an Armstrong/Narcissistic number or not, using while loop.

# ------ Relevant Concepts ------
# Before we code, we need to recall the definition of Armstrong/Narcissistic number.
# An armstrong number (also known as "Narcissistic number") is a number that is the sum of its own digits each raised up
# to the power of the number of digits.
# For example, 153 is an Armstrong number since 153 = 1^3 + 5^3 + 3^3 where 1, 5 and 3 are 153's own digits and the 3
# appearing behind the ^ symbol is the number of digits.
# Any Armstrong number (represented by 'n') can be written as a rule:
# n = d(k)^k + d(k-1)^k + ... + d(3)^k + d(2)^k + d(1)^k
# where k stands for the number of digits and d(k) stands for digits.

# ------ Problem Solution ------
# Step 1. Take the number from the user. For example, the user gives us a number 370.
# Step 2. Take each digit from the given number. In the example above, we take 3, 7 and 0 from 370 one at a time.
# Step 3. Compute the number of digits by counting them. In the same example, the number of digits is three.
# Step 4. Calculate the sum of the known digits each raised up to the power of the number of digits. In the same example
#         , 3^3 + 7^3 + 0^3 gives us a value which we don't know whether it is equal to 370 or not so far.
# Step 5. Check if the value we get in Step 4 is equal to 370.
# Step 6. If they are equal, then we can say that '370' is an Armstrong number; if not, we say that '370' is not an
#         Armstrong number.

# ------ Problem Explanation ------
# Step 1:
# Take the number from the user using the input() function.
# Step 2:
# Take the index of each digit from the given number, using a while loop and the length of the number (in string form).
# Steps 3/4:
# Access each digit of the given number using the [...] index operator, raise each digit up to the power of the length
# of the given number and sum up the powers of the digits using the += assignment operator.
# Step 5:
# Check if the sum we get from steps 3/4 is equal to the original number and print the result,
# using the if..else statement.


# ------ Source Code ------
# Code of Step 1:
num = input("Enter your (decimal) number: ")
# Code of Step 2:
i = 0
Sum = 0
while i < len(num):

    # Code of Steps 3/4:
    Sum += int(num[i]) ** len(num)

    i = i + 1

# Code of Step 5:
if Sum == int(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


# ------ UDF Version ------
def armstr_check(num):
    """Return the given number itself if it is an Armstrong number."""
    num = str(num)
    i = 0
    Sum = 0
    while i < len(num):
        Sum += int(num[i]) ** len(num)
        i = i + 1
    if Sum == int(num):
        num = int(num)
        return num


# ------ Test UDF ------
# Use numbers from 0 to 10,000 to test to see if there are the same numbers as the below sequence.
# The sequence of base 10 Armstrong numbers (the first multiple terms):
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, ...
armstr_ls = []
for num in range(0, 1000000):
    if armstr_check(num):
        armstr_ls.append(armstr_check(num))
print("\nWithin the range of 0 to 10000, the Armstrong numbers are:\n")
print(armstr_ls)

