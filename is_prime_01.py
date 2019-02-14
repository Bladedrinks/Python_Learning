# User-defined functions to check if a given number is prime or not.
# source: https://www.youtube.com/watch?v=2p3kwF04xcA&t=1s


import math
import time


# Define a function to return True if the given number is prime. False otherwise.

# Before we begin, we need to recall what prime number is and what composite number is.
# A prime number is an integer greater than 1 that can only be divisible by 1 and itself, like 2, 3, 5, 7, 11, 13, etc.
# A composite number is an integer greater than 1 that can be divisible by smaller integer, in addition to 1 and itself,
# like 4, 6, 8, 9, 10, 12, 14, etc.
# For the sake of keeping the Fundamental Theorem of Arithmetic true, or for making the unique prime factorization of
# any composite number, mathematicians consider 1 to be neither prime nor composite and call 1 "unit".


# Version 1 (v1) of the UDF.
def is_prime_v1(n):
    """Returns 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False  # 1 is not prime (1 is not composite, either)
    # d stands for divisor. Since any number greater than 1 (prime or composite) can be exactly divided by 1 and itself,
    # we skip 1 and n and only iterate over the items in the sequence from 2 through n - 1 (Remember in the range()
    # function the stop value is not included.)
    for d in range(2, n):
        # % is the modulus operator. The right-hand side is the remainder of the operation of division of n by d.
        # If n is divisible by d, the remainder is equal to 0; if not, the remainder is not equal to 0.
        # So the test_expression of n % d == 0 means n is divisible by d. If the test_expression is True, control of the
        # program flows to the body of if and execute the return statement. The function exits and meanwhile the boolean
        # value of False is returned.
        if n % d == 0:
            return False
    # If each items in the sequence generated from the range doesn't make the test_expression True, meaning n is not
    # divisible by any smaller number, then we can consider n is prime and return True after the items in the sequence
    # exhaust without the for loop being stopped halfway.
    return True
# End of the function definition.


# Version 2 (v2) of the UDF.
def is_prime_v2(n):
    """Returns True is n is a prime number; False otherwise."""
    # To spare time and make the program fast forward, we need reduce the test divisors.
    # To see the rule of integer factorization, we need to take an example of 64 and 32.
    # Let's take a look at all the ways that we factor 64, 32 and 144 as a product of two smaller integers:
    # 64 = 1 x 64                   32 = 1 x 32                                   144 = 1 x 144
    #    = 2 x 32                      = 2 x 16                                       = 2 x 72
    #    = 4 x 16                      = 4 x 8                                        = 3 x 48
    #    = 8 x 8   dividing line       = √32 x √32 (5.65 x 5.65)  dividing line       = 4 x 36
    #    = 16 x 4                      = 8 x 4                                        = 6 x 24
    #    = 32 x 2                      = 16 x 2                                       = 8 x 18
    #    = 64 x 1                      = 32 x 1                                       = 9 x 16
    #                                                                                 = 12 x 12  dividing line
    #                                                                                 = 16 x 9
    #                                                                                 = 18 x 8
    #                                                                                 = 24 x 6
    #                                                                                 = 36 x 4
    #                                                                                 = 48 x 3
    #                                                                                 = 144 x 1
    #                                                                                 = 72 x 2
    # The first three factorizations of 64 is the same as the last factorization, just in reverse order.
    # Since 64 is a perfect square (or square number or integer that is the product of another integer multiplied by
    # itself), it can be factored as 8 times 8, which is the dividing line between the duplicate factorizations.
    # Not all integers are perfect square. For example, 32 is not a perfect square, since it can not be the square of
    # an integer. 5 squared equals 25. 6 squared equals 36. Between 5 and 6 there is no other integers. But we can still
    # find the dividing line, which is the square root of 32 times the square root of 32. For 32, the same thing
    # happens. The first three factorizations are the same as the last three factorizations.
    # For any integer n greater than 1, the same thing happens.
    # n = 1 x n
    #   = a x b
    #   = ...
    #   = √n x √n
    #   = ...
    #   = b x a
    #   = n x 1
    # If n is able to be divided by a evenly, then that is to say n is also able to be divided by b evenly. So we don't
    # necessarily have to test the last half possible divisors. Since any number greater than 1 is divisible by 1, we
    # skip 1 and 2 is the least possible divisor to test. The largest possible divisor is the square root of n. Since
    # n might not be a perfect number, the square root of n might be a decimal number (just like the square root of 32
    # equals 5.65. What we need to test are all integers, so we need to round the square root of n down to the nearest
    # integer, which is the integer part of √n (in the case of 32, which is 5).

    # "divisor" has the same meaning as "factor". A factor of a whole number is a positive integer that is multiplied by
    # another positive integer to get the first whole number.

    max_divisor = int(math.sqrt(n))
    # To take the max divisor, we need to take the square root of n and round it down to the greatest integer less than
    # or equal to it, using the floor() function or the int() function. (Note: Don't use the round() function, since it
    # will round off the value to the least integer greater than or equal to it.

    for d in range(2, max_divisor + 1):
        # To include max_divisor into the sequence over which we're gonna iterate, we have to add 1 to it since the stop
        # parameter is not included in the sequence generated from the range() function in Python.
        if n % d == 0:
            return False
    return True


# Version 3 of the UDF.
def is_prime_v3(n):
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    # if n == 3:
    #     return True
    max_divisor = int(math.sqrt(n))
    for d in range(3, max_divisor + 1, 2):
        # If we already know that 'n' is an odd number, then do we have to test if each smaller integer greater than 1
        # can evenly divide 'n'?
        # No, not necessary. The ultimate goal to test smaller integers is to find if there is an integer which can
        # evenly divide 'n'. In other words, we don't know if these smaller integers can evenly divide 'n' before we
        # test them. But what if we know part of them really can evenly divide 'n' based off on the known mathematical
        # theorem? Well, that means we don't have to waste time in testing these smaller integers since we've already
        # know they can't divide 'n'. The known mathematical theorem is:
        #
        #  Operations    Result
        #  Even x Even = Even
        #  Even x Odd  = Even
        #  Odd  x Even = Even
        #  Odd  x Odd  = Odd
        #
        # So we can say that any odd number can only be evenly divided by another smaller odd number. An odd number can
        # not be evenly divided by another smaller even number, since Odd equals Odd times Odd.
        # Since we've already known that any odd number can not be divisible by even numbers, we don't necessary to test
        # those smaller integers. We only need to test the rest odd smaller integers.
        # The rest odd smaller integers are like: 3, 5, 7, 9, 11, 13, ...
        # You might have noticed that the number sequence shown above is an arithmetic sequence with a common difference
        # , which is 2, since 3 + 2 = 5, 5 + 2 = 7, 7 + 2 = 9, ...
        # To let the range() function generate a list of odd smaller integers, we need to set it like this:
        #
        # range(3, n, 2)
        #
        # which generates a list like this: [3, 5, 7, 9, 11, 13, 15, ..., n - 2] where the last item is not 'n' itself,
        # but the penultimate item 'n - 2'.
        # Since the factorization of any integer greater than 1 (especially composite one) can be split into two
        # duplicate halves between which there is a dividing line - √n x √n = n. The first half of ways of factoring and
        # the second half of ways of factoring are the same, just in reverse order. Therefore, we only need to check the
        # first half. So, the range() function can be updated into:
        #
        # range(3, int(math.sqrt(n)) + 1, 2)
        #
        # since the square root of n might be a decimal number, its integer part is
        # likely to be a possible factor/divisor which should be included into the range. Therefore, we have to take the
        # integer part of √n and add 1 to it.
        if n % d == 0:
            return False
    return True


# Version 4 of the UDF (substituting a while loop for the for loop in Version 3)
def is_prime_v4(n):
    """Return 'prime' if 'n' is prime; 'composite' if 'n' is composite; 'not prime' is 'n' is less than 1."""
    if n < 2:
        return "not prime"
    if n == 2:
        return "prime"
    if n > 2 and n % 2 == 0:
        return "composite"
    d = 3
    while d <= int(math.sqrt(n)):
        if n % d == 0:
            return "composite"
        d = d + 2
    return "prime"


# Version 5 of the UDF (based off of a very basic property of prime numbers - only prime number can be evenly divided by
# a number that is within the interval from 1 (included) to itself (included). This version was originally part of a
# larger program which deals with print prime factors of a given number. To see the original program, here is the link:
# source: https://www.youtube.com/watch?v=2p3kwF04xcA&t=1s
def is_prime_v5(i):
    # ...  (The ... (three dots) symbol stands for the part that has been deleted since these deleted parts have nothing
    #      to do with this very UDF.
    # ...
    k = 0
    #   ...
    j = 1
    while j <= i:
        if i % j == 0:
            k = k + 1
        j = j + 1
    if k == 2:  # 'if k == 2' is another way to say, 'if i is a prime number', since only prime numbers have just
        # two chances to make the 'i % j == 0' condition evaluates to True and then reassign 'k' twice - first k = 1
        # and second k = 2
        return f"{i} is prime"
    return f"{i} is not prime"


# ========= Test Function =========
for n in range(-21, 21):
    print(is_prime_v5(n))


# ========= Time Function =========
# Figure out how long the version 2 takes to test an extraordinary number (say, 300000000) using the time module and its
# time.time() function.
# The time.time() function returns the number of seconds have passed since the epoch (the moment where time begins for
# unix system, which is January 1st, 1970, 00:00:00). Therefore, in order to calculate the length of time the test
# function takes to perform its task, we have to make a subtraction between the length of time when the function
# finishes its task (we call it "t1") and the length of time when the function begins its task (we call it "t0").
#
# Initialize t0.
# t0 = time.time()
# print(f"t0 = {t0}")
# # To get t1, we need to test the UDF (user-defined function) immediately after t0 and right before t1. The difference of
# # t1 - t0 is the length of time the test function takes to complete its task (that is, to return True/False if the given
# # number is prime/composite.
# for n in range(1, 100000):
#     is_prime_v5(n)
# t1 = time.time()
# print(f"t1 = {t1}")
# print(f"Time required: {t1 - t0}")
