# Program to find all the primes less than or equal to an integer 'n',
# using the Sieve of Eratosthenes and the pseudocode based off of it.
# The pseudocode is from:
# (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode)

from math import sqrt

# Input: an integer n > 1.
n = int(input("Enter the number which you want to find all the primes less than or equal to: "))

# Let A be an array of Boolean values, indexed by integers 2 to n,
# initially all set to True.
A = []
for i in range(n + 1):
    A.append(True)
# To make sure the last index is equal to 'n',
# we need to set the range() equal to 'range(n + 1)' so that this 'A' list has 'n+1' items,
# whose indices are like this: 0, 1, 2, 3, 4, ..., 98, 99, 100 (if 'n+1' is set equal to 101)
# Remember any list's index starts at 0 and ends at (len(list) - 1)

# for i = 2, 3, 4, ..., not exceeding √n:
#   if A[i] is True:
#     for j = i**2, i**2+i, i**2+2i, i**2+3i, ..., not exceeding n:
#       A[j] := False.
for i in range(2, int(sqrt(n))+1):
    if A[i] is True:
        m = 0
        j = 0
        while j < n:
            j = i ** 2 + m * i
            if j > n:  # not exceeding n
                break
            A[j] = False
            m += 1

# Output: all i such that A[i] is true.
primes = []
for i in range(2, n+1):
    if A[i] is True:
        primes.append(i)
print(f"There are {len(primes)} primes less than or equal to {n}, which are: \n{primes}")


# ====== Test ======
# Prime numbers under 200 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
# 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199.
test_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
if primes == test_list:
    print("You made it! Congrats!")
