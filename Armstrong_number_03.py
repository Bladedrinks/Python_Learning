# ------ Code Analysis ------
# Python program to check if the number provided by the user is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))  # Say, 'num' is assigned a value 663, a 3-digit number.

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num  # 'temp' is assigned the value of 'num', 663.
while temp > 0:         # 'temp(663) > 0' returns (evaluates to) True since 663 is greater than 0, then execute the body
    # of the while loop. After the first iteration, 'temp' is reassigned a new value of 66 (the integer part of 66.3)
    # the test_expression of the while loop should be check again. While 'temp(66) > 0' evaluates to True, execute the
    # body of while loop.
    # 'temp' has been reassigned a new value of 6, which is greater than 0, so we can keep executing the body of while.
    # 'temp' has been reassigned a new value of 0, which makes the test_expression 'temp > 0' evaluates to False, so we
    # have to exit the while loop.
    digit = temp % 10   # The modulo operation 'temp(663) % 10' evaluates to 3 because the division of 663 by 10 has a
    # a quotient of 66 and leaves a remainder of 3. And then assign the value of 'temp(663) % 10', 3, to the variable
    # 'digit'. The goal of this 'digit = temp % 10' statement is nothing but to take the digit in the ones(1s) position
    # Why the 'digit = temp % 10' statement works? Because the digits in the tens(10s) and the hundreds(100s) positions
    # are all multiples of 10 and can be divisible by 10 and nothing is left. The digit in the ones position can not be
    # divisible by 10 (in other words, 10 can't go into it since it is less than 10), so the 'temp % 10' can help us
    # individually obtain the digit in the ones position. Can we use other divisors (like 2, 5, 11, 20, etc) in the
    # modulo operation? No, other divisors don't work at all. Other divisors would not make the modulo operation return
    # a value that is equal to the digit in the ones position. For example, we take 7 as the operand to the right-hand
    # side the modulus operator. temp(633) % 7 equals 5. '5' is not the digit in the ones position.
    # 'temp(66) % 10' evaluates to 6 (obviously, 10 goes into 66 exactly six times and leaves a 6 outside there).
    # 'digit' is assigned a new value of 6.
    # 'temp(6) % 10' evaluates to 6, since 6 / 10 equals 0 with a remainder of 6, or you can also say, 0 R 6. Why 0 R 6?
    # The division operation, in essence, is used to tell us how many times the divisor goes into the dividend. If the
    # dividend (say, 50) can be evenly divided by the divisor (say, 10), the divisor(10) goes into the dividend(50) five
    # times. When we want to know how many times 10 can go into 6, we need to use the division operation to
    # divide 6 by 10. '10' can't go into '6', so the quotient(Latin for 'how many times') is 0 and we still hold a 6
    # after 6 - (10 * 0) == 6.
    sum += digit ** 3   # Add the digit raised up to the power of the number of digits (in this case, 3) to the sum.

    temp //= 10  # '//=' in 'temp //= 10' is a compound assignment operator. The 'temp //= 10' operation is equivalent
    # to 'temp = temp // 10'. The 'temp(663) // 10' operation (a floor/integer division) evaluates to 66 since 663 / 10
    # == 66.3 of which the integer part is 66 . The 'temp //= 10' assignment is intended to get us the other digits
    # right before the digit in the ones(1s) position and prepare for the next modulo operation.
    # 'temp(66) // 10' evaluates to 6 since 66 / 10 == 6.6 of which the integer part is '6'. 'temp' is reassigned a new
    # value of 6.
    # 'temp(6) // 10' evaluates to 0 since 6 / 10 == 0.6 of which the integer part is '0'. 'temp' is reassigned a new
    # value of 0.

# display the result
if num == sum:
    # Check if the number is equal to the sum of its own digits each raised up to the power of the number of digits,
    # using the == ('equal to') comparision operator. If the test_expression of if evaluates to True, then we can say
    # the number is an Armstrong number.
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# Uncomment the below block of code to see the core part of the code.
# # Below is a self-contained part of code of the program:
# temp = num  # For keep the original value of 'num' unchanged, assign the value of 'num' to the variable 'temp'.
# while temp > 0:  # The 'temp > 0' condition is designed based off of the below code.
#     digit = temp % 10  # No matter what the digit in the ones(1s) position is, the number made by the digits before the
#     # ones position (in this case, 66) must be divisible by 10, since the digits stands for tens(10s), hundreds(10x10s),
#     # thousands(10x10x10s), ten-thousands(10x10x10x10s), etc. The digit in the ones(1s) place only stands for the number
#     # of 1s (in this case, 3 standing for three 1s). Even the largest digit in the ones place, which is 9, is less than
#     # 10 and can not be divisible by 10, so the remainder of 'temp % 10' must be the value of the digit in the 1s place.
#
#     temp = temp // 10
