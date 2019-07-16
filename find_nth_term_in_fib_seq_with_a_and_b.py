# This is a temp file for retrieving the algorithm of finding the nth number in a Fibonacci series
# from my memory to my mind.

# Below is the explanation and the source code of a user-defined function
# for finding the nth term in a Fibonacci series with the first two numbers a and b.
# We will apply "recursive algorithm" to the programming.


# ====== Explanation ======

# Before we begin coding, we have to retrieve the definition or the characteristics of "recursion" out of our memory.
# With recursive algorithm, the original problem can be solved or decomposed by making simpler instances of the same
# problem on and on and on until the control flow meets the base case.

# The base case is the case which can not be further divided or decomposed,
# which can be thought of as the final point and the turning point in a U-turn shaped route.
# The rum time stack of function calls at this turning point starts to be removed one by one
# , or specifically, 'call frame' by 'call frame', in the direction opposite to the order of the functions being called.
# As opposed to "Base Case", "Recursive Case" refers to the part in the definition which
# calls the function first occurred in the header coming right after the keyword 'def'.


# ====== Source Code ======


def fib_num(n, a, b):
    """Returns the nth term in a Fibonacci series with a and b being the first two numbers.
    In this definition, all the terms are indexed starting from 1, not 0; thus, the nth term is really the nth number in
    the sequence. The sequence will look like this (if a = 0 and b = 1):

        a,     b,    |----------------------------------------- F(n) for n > 2 ---------------------------------------|
        0,     1,     1,     2,     3,     5,     8,     13,     21,     34,     55,      ...  # if a = 0 and b = 1
        5,     3,     8,     11,    19,    30,    49,    79,     128,    207,    335,     ...  # if a = 5 and b = 3
        F(1),  F(2),  F(3),  F(4),  F(5),  F(6),  F(7),  F(8),   F(9),   F(10),  F(11),   ...,  F(n-2),  F(n-1),  F(n)
    """
    # Base Case (which contains two parts)
    if n == 1:  # F(1), or Part I of Base Case
        return a  # 'a' is the variable signifying the value of F(1), the first term given by the user.
    elif n == 2:  # F(2), or Part II of Base Case
        return b  # 'b' is the variable signifying the value of F(2), the second term given by the user.

    # Recursive Case (which also contains two parts, not standing alone, but combined using the addition operation)
    else:
        # Remember? Any Fibonacci number is the sum of the two previous numbers except for the first two terms, which
        # have been included in the Base Case, but excluded from the Recursive Case.
        # F(n), or the original problem in the header, is equal to the sum of F(n-2) + F(n-1)
        return fib_num(n-2, a, b) + fib_num(n-1, a, b)


n = int(input("Which term in the Fibonacci series do you want? (n > 2): "))
a = int(input("The first term is: "))
b = int(input("The second term is: "))
print("The ", n, "th term in a Fibonacci series with the first two numbers being ", a, " and ", b, " is: ",
      fib_num(n, a, b), sep='')
