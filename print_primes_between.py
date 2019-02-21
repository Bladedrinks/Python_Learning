# UDF to find out all prime numbers between a given interval and put them in a list.
import math


def list_primes_between(lower, upper):
    """List all prime numbers between a given interval
    after asking the lower limit and the upper limit of the interval from the user."""
    ls = []
    for num in range(lower, upper + 1):
        if num == 2:
            ls.append(num)
        if num > 1 and num % 2 != 0:
            d = 3
            while d <= int(math.sqrt(num)):
                if num % d == 0:
                    break
                d = d + 1
            else:
                ls.append(num)
    return ls


# ------ Test UDF ------
# The first 25 prime numbers (all the prime numbers less than 100) are:
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

low = int(input("Enter the lower limit of your interval: "))
upp = int(input("Enter the upper limit of your interval: "))
print(f"Prime numbers between {low} and {upp} are: ")
print(list_primes_between(low, upp))
