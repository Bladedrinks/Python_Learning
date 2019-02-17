# A UDF to check if a given number is an Armstrong number or not, using the while loop, the modulo operation
# and the floor division (or the integer division).


def armstr_check(num):
    """Return the number itself if it is an Armstrong number."""
    x = len(str(num))
    Σ = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        Σ = Σ + digit ** x
        temp = temp // 10
    if num == Σ:
        return num


# ------ Test UDF ------
# Use numbers from 0 to 10,000 to test to see if there are the same numbers as the below sequence.
# The sequence of base 10 Armstrong numbers (the first multiple terms):
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727,

test_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 154, 156, 370, 371, 372, 373, 407, 408, 409, 1634, 1635, 1636, 8208, 8209,
           9474, 10000, 54748, 55000, 92727, 100000]
armstr_numbers = []
for num in test_ls:
    if armstr_check(num):
        armstr_numbers.append(armstr_check(num))
print(armstr_numbers)

