# This function is based off of the source code downloaded from:
# https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming

# It looks more succinct than the version adopting the recursive algorithm.


def fib_num(n, a, b):
    """Returns the nth number in a Fibonacci series with a and b being the initial two terms."""
    for count in range(n-2):
        c = a + b
        # Here, local variables 'a', 'b', and 'c' can be thought of
        # as three placeholders representing F(n-2), F(n-1), and F(n).
        # So we need to assign new values (i.e., the two numbers the sum of which is the next) to
        # the placeholders 'a' and 'b'.
        a = b
        b = a + b
        # Uncomment the below line to rewrite the above two lines of code using multiple assignment
        # a, b = b, a+b
    return c


# ====== TEST ======
n = int(input("n = "))
a = int(input("a = "))
b = int(input("b = "))
print("The ", n, "th number in the Fibonacci series with ", a, " and ", b, " being the starting two terms is: ",
      fib_num(n, a, b), sep='')
