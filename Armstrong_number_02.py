# ------ Program Introduction ------
# Program to check if a number of any base is an Armstrong/Narcissistic number or not.


# ------ Source Code ------
# First, ask the user for the base of the numeral system in which their number is, like 2, 8, 10, 16, 60, etc.
b = input("Enter the base: ")
b = int(b)
# Ask the user for the number they want to check.
num = input(f"Enter your base-{b} number: ")
# Work out the decimal value of the given number. For example, the decimal value of base-3 number 122 is 17.
i = 0
Σ = 0
while i < len(num):

    x = len(num) - (1 + i)
    if num[i] == "A" or num[i] == "a":
        Σ += 10 * b ** x
    elif num[i] == "B" or num[i] == "b":
        Σ += 11 * b ** x
    elif num[i] == "C" or num[i] == "c":
        Σ += 12 * b ** x
    elif num[i] == "D" or num[i] == "d":
        Σ += 13 * b ** x
    elif num[i] == "E" or num[i] == "e":
        Σ += 14 * b ** x
    elif num[i] == "F" or num[i] == "f":
        Σ += 15 * b ** x
    else:
        Σ += int(num[i]) * b ** x

    i = i + 1
num_deci = Σ
print(f"The base-{b} number {num} is converted to the decimal number {num_deci}")

# Work out the decimal value of the sum of its own digits each raised up to the power of the number of digits.
i = 0
Sum = 0
while i < len(num):
    if num[i] == "A" or num[i] == "a":
        Sum += 10 ** len(num)
    elif num[i] == "B" or num[i] == "b":
        Sum += 11 ** len(num)
    elif num[i] == "C" or num[i] == "c":
        Sum += 12 ** len(num)
    elif num[i] == "D" or num[i] == "d":
        Sum += 13 ** len(num)
    elif num[i] == "E" or num[i] == "e":
        Sum += 14 ** len(num)
    elif num[i] == "F" or num[i] == "f":
        Sum += 15 ** len(num)
    else:
        Sum += int(num[i]) ** len(num)
    i = i + 1
print(f"The decimal value of the sum of its own digits each raised up to the power of the number of digits is: {Sum}")

# If 'Sum' equals 'num_deci', the given number is an Armstrong number.
if Sum == num_deci:
    print(f"\nThe base-{b} number {num} (whose decimal value is {num_deci}) is an Armstrong number.")
else:
    print(f"\nThe base-{b} number {num} (whose decimal value is {num_deci}) is not an Armstrong number.")


# ------ UDF Version ------
def armstr_check_with_open_base(b, num):
    """Returns the given number itself if it is an Armstrong number."""
    num = str(num)
    # Work out the decimal value of the given number. For example, the decimal value of base-3 number 122 is 17.
    i = 0
    Σ = 0
    while i < len(num):
        x = len(num) - (1 + i)
        if num[i] == "A" or num[i] == "a":
            Σ += 10 * b ** x
        elif num[i] == "B" or num[i] == "b":
            Σ += 11 * b ** x
        elif num[i] == "C" or num[i] == "c":
            Σ += 12 * b ** x
        elif num[i] == "D" or num[i] == "d":
            Σ += 13 * b ** x
        elif num[i] == "E" or num[i] == "e":
            Σ += 14 * b ** x
        elif num[i] == "F" or num[i] == "f":
            Σ += 15 * b ** x
        else:
            Σ += int(num[i]) * b ** x
        i = i + 1
    num_deci = Σ
    # Work out the decimal value of the sum of its own digits each raised up to the power of the number of digits.
    i = 0
    Sum = 0
    while i < len(num):
        if num[i] == "A" or num[i] == "a":
            Sum += 10 ** len(num)
        elif num[i] == "B" or num[i] == "b":
            Sum += 11 ** len(num)
        elif num[i] == "C" or num[i] == "c":
            Sum += 12 ** len(num)
        elif num[i] == "D" or num[i] == "d":
            Sum += 13 ** len(num)
        elif num[i] == "E" or num[i] == "e":
            Sum += 14 ** len(num)
        elif num[i] == "F" or num[i] == "f":
            Sum += 15 ** len(num)
        else:
            Sum += int(num[i]) ** len(num)
        i = i + 1
    # If 'Sum' equals 'num_deci', the given number is an Armstrong number.
    if Sum == num_deci:
        num = int(num)
        return num


# ------ Test UDF ------
# Use numbers from 0 to 10,000 to test to see if there are the same numbers as the below sequence.
# The sequence of base 10 Armstrong numbers (the first multiple terms):
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727,
# 93084, 548834, 1741725, 4210818, 9800817, 9926315, 24678050, 24678051, 88593477,
# 146511208, 472335975, 534494836, 912985153, 4679307774, 32164049650, 32164049651
# The sequence of base 8 narcissistic numbers starts:
# 0, 1, 2, 3, 4, 5, 6, 7, 24, 64, 134, 205, 463, 660, 661, ...
# The sequence of base 16 narcissistic numbers starts:
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, 156, 173, 208, 248, 285, 4A5, 5B0, 5B1, 60B, 64B, ...
# The sequence of base 4 narcissistic numbers starts:
# 0, 1, 2, 3, 130, 131, 203, 223, 313, 332, 1103, 3303

armstr_ls = []
base = int(input("Enter the base of the sequence of Armstrong numbers: "))
lower_limit = int(input("Enter the lower limit of the test range "
                        "within which the sequence of Armstrong numbers appear: "))
upper_limit = int(input("Enter the upper limit of the test range "
                        "within which the sequence of Armstrong numbers appear: "))
for number in range(lower_limit, upper_limit):
    if armstr_check_with_open_base(base, number):
        armstr_ls.append(armstr_check_with_open_base(base, number))
print(f"\nWithin the range of 'base-{base}' {lower_limit} to {upper_limit}, the Armstrong numbers are:\n")
print(armstr_ls, end=f" which are all base-{base} numbers.\n")



