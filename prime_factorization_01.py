# Python program to print prime factors

import math


# A function to print all prime factors of
# a given number n
def prime_factors(n):
    """Returns all prime factors of a given number in string type."""

    # Print the number of 2's that divide n
    # 1560 = 2 * 2 * 2 * 3 * 5 * 13
    # So there are three 2's which evenly divides 1560.
    while n % 2 == 0:
        print(2)
        n = int(n / 2)
        # When n = 1560
        # 1560 is divisible by 2
        # # Then print out a 2 (to show the user: Now you got your first prime factor of n = 1560)
        # We don't know the rest factor(s) of 1560 are primes or not, so we have to check.
        # First, we need to take all 2's out of 1560.
        # To take 2's, we need to keep dividing 1560 by 2
        # That's why we need to write a line of this:
        #        n = int(n / 2)
        # Actually you can't keep dividing the same number over and over and over, because after you first divided 1560
        # by 2, the number 1560 has disappeared and another number 780 (the quotient of 1560 / 2) has replaced it.
        # So what we keep dividing is not the original number 1560, but its changing factors. By the way, if n is not
        # changing all the time, the while loop will never stop.
        # Using while loop (rather than for loop) has only one aim, which is to find out all 2's among the prime factors
        # of n = 1560
        # So, now we divide n = 1560 by 2 to get 780 (product of 2 * 2 * 3 * 5 * 13) and assign 780 to n.
        # When we got 780, one iteration has been done. After one iteration, the while test_expression is checked again.
        # n is assigned a new value, which is 780. 780 is divisible by 2 (that is, 780 can make "n % 2 == 0" True),
        # so we can execute the body of while again.
        # # Print out a second 2
        # # Assign 390 (quotient of 780 / 2) to n, so n contains a new value - 390
        # The second iteration is done, so check the test_expression again. 390 is divisible by 2, so we can continue
        # to execute the body of while.
        # # Print out a third 2
        # # Assign 195 (quotient of 390 / 2) to n, so n is assigned a new value - 195
        # The third iteration is done, so check the test_expression again.
        # 195 divided by 2 equals 97 remainder 1, so 195 is not divisible by 2. It makes the test_expression False,
        # we need to exit the while loop and go to the rest of the code.
        # Up till now, we've got three 2's and n storing 195, meaning the original number 1560 has only three 2's as
        # the factor.
        # This process of while loop is actually another way to show the traditional pen-and-paper mathematical work:
        # 1560 / 2 = 780  (Try divide 1560 by 2 and we got 780)
        #  780 / 2 = 390  (Try divide  780 by 2 and we got 390)
        #  390 / 2 = 195  (Try divide  390 by 2 and we got 195)
        #  195 / 2 = 97 remainder 1 (195 can not be evenly divided by 2, so stop trying)
        # Now that we have known that 1560 has only three 2's as its factors while prime factorizing, the next task is
        # to test that 195 is prime or composite. If it is, then exit the function. If not, factor 195 until we find out
        # the last prime factor of 1560
        # To check if 195 is prime or not, we need to find out if 195 can be evenly divided by at least one smaller
        # integer except 1 and itself. If we use pen and paper, we need to keep trying each smaller integer from 2
        # through 194 until we find out an integer that can divide 195 evenly. If we find no such an integer, then we
        # can say, aha, 195 is a prime number, and exit the function.
        # The pen-and-paper work is tedious and incumbent and hard. Is there any more effective and easy algorithm to
        # fix this problem?

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for d in range(3, int(math.sqrt(n)) + 1, 2):
        # This for loop is designed only for checking if an odd number is prime or composite.

        # while d evenly divides n , print d and divide n
        while n % d == 0:
            print(d)
            n = int(n / d)
    # When n = 195, control of the function flows to the for loop.
    # the range() function never changes, even when n has got a new value and generate numbers from 3 up to 39,
    # since the original n is assigned 1560 whose square root is 39.49 (2dp)
    # while 195 is divisible by 3 (195 / 3 = 65), execute the body of while:
    # Print out 3
    # n is assigned 65 (or 195 / 3).
    # After the first iteration, the test_expression is checked again. 65 is not divisible by 3, so exit the while loop
    # and go back to the for loop to take the second item, 5, to test.
    # n (= 65) is divisible by 5, so execute the body of while:
    # Print out 5
    # n is assigned 13 (or 65 / 5)
    # After the second iteration, the test_expression is checked again. 13 is not divisible by 5, so exit the while loop
    # and go back to the for loop to take the third item, 7, to test.
    # n (= 13) is not divisible by 7, so the test_expression of while loop is made False and we can't enter into the
    # while loop. We go back to the for loop to take the fourth item, 9, to test.
    # n (= 13) is not divisible by 9, so the test_expression of while loop is made False and we can't enter into the
    # while loop. We have to go back to the for loop to take the fifth item, 11, to test.
    # n (= 13) is not divisible by 11, so the test_expression of while loop is made False and we can't enter into the
    # while loop. We have to go back to the for loop to take the sixth item, 13, to test.
    # n (=13) is divisible by 13, so the test_expression of while loop evaluates to True. We are allowed to execute into
    # the body of while:
    # Print out 13
    # n is assigned 1 (13 / 13)
    # n (= 1) is not divisible by 13, so the test_expression of while loop evaluates to False and we can't enter into
    # the body of while loop. We have to go back to the for loop to take the seventh item, 15, to test.
    # ...
    # The for loop continues until the last item, 39, is taken.

    # Since n = 1 and the condition of if evaluates to False, the function stops working.
    if n > 2:  # Since the smallest odd prime number is 3, the condition is n > 2, rather than n > 1
        print(n)
    # The last if statement is necessary, since the middle for loop can not find out all prime factors of the given
    # number. The middle for loop can only find out all prime factorizations of the given number.


n = int(input("Enter your number: "))
# input: 1560
print(f"All prime factors of {n} without exponents:")
prime_factors(n)
# output: 2, 2, 2, 3, 5 and 13


# 81 = 1  x  81
#    = 2  x  No factor
#    = 3  x  27
#    = 4  x  No factor
#    = 5  x  No factor
#    = 6  x  No factor
#    = 7  x  No factor
#    = 8  x  No factor
#    = 9  x  9  = √81 x √81  dividing line
#    = 10 x  No factor
#    = 11 x  No factor
#    = 12 x  No factor
#    = ...   ...
#    = 27 x  3
#    = 28 x  No factor
#    = 29 x  No factor
#    = ...   ...
#    = 81 x  1
# If n is a composite number, all the likely ways of factorization can be found before the dividing line, √n x √n
# Therefore, we only need to test numbers greater than 1 and less than or equal to √n
# But not all prime factors can be found before the dividing line. Let's take 999981 as an example.
#
# 999981 =       3 x 333327
#        =       9 x 111109
#        = √999981 x √999981 = 999 x 999  --- dividing line ---
#        =  111109 x 9
#        =  333327 x 3
# The prime factorization of 999981 is: 3 x 3 x 111109
# 111109 doesn't appear before the dividing line.

# This code is contributed by Harshit Agrawal



