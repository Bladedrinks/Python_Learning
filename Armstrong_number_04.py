# Program to check if a given number is an Armstrong number or not, using the while loop, the modulo operation
# and the floor division (or the integer division).

# Take the number from the user.
num = input("Enter your number: ")
# Change the data type of 'num'.
num = int(num)
# Work out the number of digits which will be used as the power to which each digit is raised up,
# using the len() function.
x = len(str(num))
# Initialize 'Σ' (the sum of the given number's digits each raised up to the power of the number of digits.
Σ = 0
# For the final comparison of 'num' and 'Σ', the value of 'num' should be immutable.
# To keep the value of 'num' immutable, we can just assign the value of 'num'
# to a temporary variable (let's call it 'temp') while the value of 'num' doesn't have to be changed. And then we can
# use 'temp' in the following while loop, instead of using 'num' itself.
# The = (single equal) symbol is the simplest assignment operator which assigns values to variables.
temp = num
# Take the digits of the given number one at a time, using a while loop, the modulo operation and the floor division.
while temp > 0:
    # A very beautiful theorem of the modulo operation: The remainder which the division of any positive integer by 10
    # leaves is the digit in the ones(1s) place of the integer. We can use this theorem to take the digits of the given
    # number in each iteration while using the while loop.
    # For example, 12340 % 10 == 0 since 12340 / 10 == 1234 R 0;
    # 1234 % 10 == 4 since 1234 / 10 == 123 R 4;
    # 123 % 10 == 12 since 123 / 10 == 12 R 3;
    # 12 % 10 == 2 since 12 / 10 == 1 R 2;
    # 1 % 10 == 1 since 1 / 10 == 0 R 1 (the division of 1 by 10 leaves us a quotient of 0 and a remainder of 1)
    digit = temp % 10
    # Now that we have got the digit, the following step is to raise it up to the power of the number of digits and add
    # the results all together to get the sum.
    Σ = Σ + digit ** x

    # For the individual digits, we must change the value of 'num' because next time the digit in the ones position we want
    # to take is from a 'num' that should only consists of the digits right before the one in the ones position. Then, the
    # question is how to change the value of 'num' to get all the digits to the left side of the digit in the ones position.
    # To divide any positive integer by 10 and take the integer part of the result gets us what we want. The floor division
    # works on this issue.
    temp = temp // 10
    # For example, 12340 // 10 == 1234 since 12340 / 10 == 1234.0 of which the integer part is 1234
    # 1234 // 10 == 123 since 1234 / 10 == 123.4 of which the integer part is 123
    # 123 // 10 == 12 since 123 / 10 == 12.3 of which the integer part is 12
    # 12 // 10 == 1 since 12 / 10 == 1.2 of which the integer part is 1
    # 1 // 10 == 0 since 1 / 10 == 0.1 of which the integer part is 0

# If a number is an Armstrong number, the value of itself is equal to the sum of its own digits each raised up to the
# power of the number of digits.
if num == Σ:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")

# ------ Test UDF ------
# Use numbers from 0 to 10,000 to test to see if there are the same numbers as the below sequence.
# The sequence of base 10 Armstrong numbers (the first multiple terms):
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727,
