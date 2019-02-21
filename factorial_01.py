# Program to display the factorial of a given number.

# Before we begin we need to figure out what the factorial of a number is.
# The factorial of an integer is the product of all whole numbers from the chosen number down to 1.
# For example, the factorial of 5 (written as 5!, which we call it "five shriek", "five bang" or "five fatorial") is
# equal to 5 x 4 x 3 x 2 x 1 or 5 x 4!
# Therefore, the factorial of any positive integer 'n' can be written as: n x (n - 1)!

# n = int(input("Enter your number: "))
# n_bang = 1
# f = 1
# while f <= n:
#     n_bang = n_bang * f
#     f = f + 1
# print(f"{n}! = {n_bang}")


# Define a function to work out the factorial of a given number.
def factorial(n):
    """Return the factorial of the given number."""
    n_bang = 1
    f = 1
    while f <= n:
        n_bang = n_bang * f
        f = f + 1
    return n_bang


# ------ Test Function ------
# Compute the factorials of numbers from 0 through 25.
for num in range(0, 26):
    print(f"{num}! = {factorial(num)}")
