# This is a temp file for retrieve the algorithm of finding the nth Fibonacci series from my memory to my mind.


# This is a user-defined function for finding the nth term in a Fibonacci series with the first two numbers a and b.
# We will apply "recursive algorithm" to the programming.

# Before we begin coding, we have to retrieve the definition or the characteristics of "recursion" out of our memory.
# With recursive algorithm, the original problem can be solved or decomposed by solving simpler instances of the same
# problem on and on and on until the control flow meets the base case. The base case is the case which can not be
# further divided or decomposed, which can be thought of as the final point and the turning point in a U-turn shape.
# The rum time stack of function calls at this turning point starts to be removed in the direction opposite to the order
# of the function calls. As opposed to "Base Case", the "Recursive Case" refers to the part in the definition which
# calls the function first occurred in the header coming right after the keyword 'def'.


def fib_num(n, a, b):
    """Returns the nth term in a Fibonacci series with the first two numbers being a and b.
    In this definition, all the terms are indexed starting from 1, not 0; thus, the nth term is really the nth term in
    the sequence. The sequence will look like this (if a = 0 and b = 1):

        a,     b,
        0,     1,     1,     2,     3,     5,     8,     13,     21,     34,     55,      ...,
        5,     3,     8,     11,    19,    30,    49,    79,     128,    207,    335,    542, 877, 1419, 2296, 3715, 6011, 9726, 15737, 25463
        F(1),  F(2),  F(3),  F(4),  F(5),  F(6),  F(7),  F(8),   F(9),   F(10),  F(11),   ...,  F(n-2),  F(n-1),  F(n)
    """
    # Base Case (which contains two parts)
    if n == 1:  # Part I of Base Case
        return a
    elif n == 2:  # Part II of Base Case
        return b

    # Recursive Case (which also contains two parts)
    else:
        # Remember? Any Fibonacci number is the sum of the two previous numbers except for the first two terms, which
        # have been included in the Base Case and excluded from the Recursive Case.
        # F(n), or the original problem in the header, is equal to the sum of F(n-2) + F(n-1)
        return fib_num(n-2, a, b) + fib_num(n-1, a, b)


n = int(input("Which term in the Fibonacci series do you want? (n>3): "))
a = int(input("The first term is: "))
b = int(input("The second term is: "))
print("The ", n, "th term in a Fibonacci series with the first two numbers being ", a, " and ", b, " is: ",
      fib_num(n, a, b), sep='')
