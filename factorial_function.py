# Program to display the factorial of a given number.

# Before we begin we need to figure out what the factorial of a number is.

# The factorial of an integer is the product of all whole numbers from the chosen number down to 1.
# For example, the factorial of 5 (written as 5!, which we call it "five shriek", "five bang" or "five factorial") is
# equal to 5 x 4 x 3 x 2 x 1 or 5 x 4!
# Therefore, the factorial of any positive integer 'n' can be written as: n * (n - 1)!, read as:
# 'n' times the factorial of 'n minus 1'.

# n = int(input("Enter your number: "))
# n_bang = 1
# f = 1
# while f <= n:
#     n_bang = n_bang * f
#     f = f + 1
# print(f"{n}! = {n_bang}")


# Define a function to work out the factorial of a given number.
def factorial_v1(n):
    """Return the factorial of the given number."""
    n_bang = 1
    f = 1
    while f <= n:
        n_bang = n_bang * f  # n_bang *= f
        f = f + 1
    return n_bang


# Version 2 which substitutes a for loop for the while loop in Version 1, using "iterative algorithm".
def factorial_v2(n):
    """Return the factorial of an integer n."""
    fact = 1
    for item in range(1, n+1):
        fact *= item
    return fact


# Version 3 is a refactored version using "recursive algorithm".
# About the recursive algorithm, see: https://realpython.com/python-thinking-recursively/
def factorial(n):  # factorial(n) can be thought of as 'factorial of n' or 'n!' in short.
    """
    Return the factorial of integer 'n' using recursive algorithm.

    Let's take n=4 as an example, meaning we are finding the factorial of 4:

    Below the lines of code for the definition, we call the factorial function on a number of 4:

    factorial(4)

    factorial(4) returns: None, since 4 * factorial(4-1) or 4 * factorial(3) and the factorial(3) part
    cannot directly return a concrete value, it has to refer to itself (i.e., to make self-reference to the definition
    of itself).

    Calling the factorial() function on 3 requires us to go back to the definition of factorial().

    factorial(3)

    factorial(3) returns: None, since 3 * factorial(3-1) or 3 * factorial(2) and the factorial(2) part is unable to give
    us a concrete numeric value, it ought to refer to the factorial() function in order to find the answer, meaning
    to make self-reference to itself.

    Calling the factorial() function on 2 requires us to go back to the definition of factorial().

    factorial(2)

    factorial(2) returns: None, since 2 * factorial(2-1) or 2 * factorial(1) and the factorial(1) part is not able to
    directly return a numerical value, it has to make self-reference to the factorial() function (yes, that is itself.)

    Calling the factorial() function on 1 requires us to go back to the definition of factorial().

    The definition says, if n == 1, then return a 1, meaning calling factorial() on 1 returns 1.

    Now that we have finished the decomposition job (decomposing the original problem into smaller instances of the same
    problem until the sub-problem is too small to break apart) and reached to the "base case", which in this case is
    factorial(1) or 1! == 1, we can start to multiply all the integers up together.

    4! = 4 * 3!
             ||
             3 * 2!
                 ||
                 2 * 1!
                     ||
                     1
       = 4 * 3 * 2 * 1 = 24
    """
    if n == 1:  # The if statement is intended for the "Base Case" - 1! = 1
        return 1
    else:  # The else statement is for the "Recursive case" - n! = n * (n-1)!
        return n * factorial(n-1)  # n * (n-1)!
    # The "recursive case" can be thought of as the recursive function itself.
    # In the above example, the problem we need to deal with is find the factorial of 4, and
    # the recursive case is find the factorial of some number.


# ====== TEST ======
# Say, we call the factorial_v3() function on an integer 4 and print out the returned value, which is expected to be:
# 4! = 4 x 3 x 2 x 1 = 24.
print(factorial(4))

# ------ Test Function ------
# Compute the factorials of numbers from 0 through 25.
# for num in range(0, 26):
#     print(f"{num}! = {factorial_v1(num)}")
