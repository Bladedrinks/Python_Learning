# Program to find all the primes less than or equal to an integer 'n',
# using the Sieve of Eratosthenes and the pseudocode based off of it.
# The pseudocode is from:
# (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode)
# TO UNDERSTAND HOW THE SIEVE OF ERATOSTHENES AND ITS PSEUDOCODE

from math import sqrt

# Input: an integer n > 1.
n = int(input("Enter the number which you want to find all the primes less than or equal to: "))

# Let A be an array of Boolean values, indexed by integers 2 to n,
# initially all set to True.
A = []
for i in range(n + 1):
    A.append(True)
# To make sure the last index is equal to 'n',
# we need to set the range() equal to 'range(n + 1)'.
# Let's take 100 as an example by assigning 100 to 'n'. So the list consisting of boolean values are indexed like this:
# [True, True, True, True, True, True, True, True, True, True, True, True, ..., True, True, True, True, True]
#   0     1     2     3     4     5     6     7     8     9     10    11   ...,  96    97    98    99    100
# Why do we need a list of boolean values? Aren't we dealing with a number problem? Yes, we ARE dealing with a number
# problem. But, we are dealing with it on computer. The sieve of Eratosthenes asks us to mark off (cross out) composite
# numbers from 2 up to 100, and the numbers left over are all prime. On computer, we can take a pencil and literally
# cross out each composite number on the screen by hand. So we have to find another way to mark composites in this
# consecutive integers.
# To initialize all the items in the list with boolean value - True helps us prepare to "mark off" some of them.
# When we find any composite, we don't have to literally cross out them with pencil. Instead, we flip the boolean value
# whose index is that composite number.


# Now that we have a list of boolean values whose indices are exactly the example integers from which we're gonna find
# all the prime numbers:
#
# [True, True, True, True, True, True, True, True, True, True, True, True, ..., True, True, True, True, True]
#   0     1     2     3     4     5     6     7     8     9     10    11   ...,  96    97    98    99    100
#
# for i = 2, 3, 4, ..., not exceeding √n:
#   if A[i] is True:
#     for j = i**2, i**2 + i, i**2 + 2i, i**2 + 3i, ..., not exceeding n:
#       A[j] := False.
for i in range(2, int(sqrt(n))+1):  # Assign 'i' values from 2 up to √n
    if A[i] is True:  # The boolean item whose index number has been found to be composite has been updated to be False.
        m = 0
        j = 0
        while j < n:
            j = i ** 2 + m * i  # 'i ** 2' is 'i * i'. We start off at 'i*i' because all multiples less than i*i have
            # been marked off as multiples of numbers smaller than i. Additionally, to make 'j' grow in increments of i
            # from i**2 to n (inclusive/exclusive), we have to put a coefficient 'm' before 'i'.
            if j > n:  # not exceeding n
                break
            A[j] = False  # Assigning False to the bool item whose index has been proven to be composite.
            m += 1
# When the above for statements complete, we got an updated list which looks like this:
# [True, True, True, True, False, True, False, True, False, False, False, True, ..., False, True, False, False, False]
#   0     1     2     3      4     5      6     7      8      9      10    11   ...,   96    97     98     99    100

# Output: all i such that A[i] is true.
primes = []
for i in range(2, n+1):  # Why the range starts at 2 (not 0)? Because 1 is neither prime nor composite.
    if A[i] is True:
        primes.append(i)
print(f"There are {len(primes)} primes less than or equal to {n}, which are: \n{primes}")


# ====== Program Test ======
# Prime numbers under 200 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
# 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199.
test_list = []  # Before test, you need to pass in a list of integers to the empty list on the right-hand side of the = (assignment) operator.
if primes == test_list:
    print("You made it! Congrats!")
