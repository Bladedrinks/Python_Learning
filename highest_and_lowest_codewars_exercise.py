# This file contains solutions to an exercise given by codewars.com
# https://www.codewars.com/kata/highest-and-lowest/solutions/python

# In this program, the user is given a string of space-separated numbers (which looks like this: "5 -2 0.9 33 10 3.4"),
# and the program will return the highest and lowest number(s). Since the highest and lowest numbers might be the same
# one (if the space-separated numbers in the string are all the same), the program will return the duplicates of the
# same number.

# Example:
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

# Notes:
# (1) All numbers are valid Int32, no need to validate them.
#     (WARNING: WHAT THE HECK does 'Int32' refer to? AND WHY WE NEED TO LIMIT THE ALL THE NUMBERS TO 'valid Int32'?)
# (2) There will always be at least one number in the input string.
#     (Why "at least one number"? Otherwise you have nothing to compare.)
# (3) Output string (compared to the 'input string') must be two numbers separated by a single whitespace, and the
#     highest comes first.


def high_and_low_v1(str):
    """Return the highest and lowest number(s) in the given string."""
    nums = [int(n) for n in str.split()]
    return f"{max(nums)} {min(nums)}"


def high_and_low_v2(str):
    """Return the highest and lowest number(s) in the given string."""
    nums = list(map(lambda strNum: int(strNum), str.split()))
    return f"{max(nums)} {min(nums)}"


def high_and_low_v3(str):
    """Return the highest and lowest number(s) in the given string."""
    nums = list(map(int, str.split()))
    return f"{max(nums)} {min(nums)}"


def high_and_low_v4(str):
    """Return the highest and lowest number(s) in the given string."""
    nums = list(map(int, str.split()))
    return str(max(nums)) + ' ' + str(min(nums))
    # The version doesn't work and Python throws an error.
    # TypeError: 'str' object is not callable


# ====== UDF TEST ======
print(high_and_low_v4("1 2 3 4 5"))  # return "5 1"
print(high_and_low_v4("1 2 -3 4 5"))  # return "5 -3"
print(high_and_low_v4("1 9 3 4 -5"))  # return "9 -5"
