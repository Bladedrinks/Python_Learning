# Program to find and display all prime numbers from 2 up to an integer 'n',
# using the Sieve of Eratosthenes and list comprehension.
from math import sqrt
n = int(input("Enter the number which you want to find out all primes less than or equal to: "))
# Find out all composite numbers and assign them to a list named 'composites'.
# composite_ls = [j for i in range(2, int(sqrt(n))+1) for j in range(i**2, n+1, i)]
# There are many repeating numbers in this composite list, which is a defect in this algorithm.
# Uncomment the following line so that you can see there are lots of double entries contained in this composite list.
# print(f"The composite list is: {composite_ls} whose length is: {len(composite_ls)}")
# To solve this unbearable problem, we use set comprehension
# (uncomment the following line to see how the set comprehension works):
square_root_of_n = int(sqrt(n))
composite_set = {j for i in range(2, square_root_of_n + 1) for j in range(i**2, n+1, i)}  # The 'i' step is the common
# difference between multiples of 'i' from i**2 (= i*i): i**2, i**2 + i, i**2 + i + i, i**2 + i + i + i, ..., that is,
# any multiple of i minus the previous multiple of i is equal to i.
# NOTICE: THIS IS A SET COMPREHENSION, NOT A LIST COMPREHENSION, SINCE WE USE {...} CURLY BRACES, NOT SQUARE BRACKETS.
print(f"The composite set is: {composite_set} whose length is: {len(composite_set)}")
# For more details about how to use 'set comprehension', see:
# https://www.python-course.eu/python3_list_comprehension.php

# Display all prime numbers using 'not in' keywords with 'compos'.
prime_ls = [i for i in range(2, n+1) if i not in composite_set]
print(f"There are {len(prime_ls)} primes less than or equal to {n}, which are: \n{prime_ls}")


# ====== Program Test ======
# Prime numbers under 200 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
# 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199.
test_ls = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
             107, 109, 113, 127, 131, 137, 139, 149]
if prime_ls == test_ls:
    print("Congrats! You passed the test.")

