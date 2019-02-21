# Program to display a Fibonacci sequence based off of the first two terms which are given by the user.

# To reduce confusion, we call the 1st term of the Fibonacci sequence 'x', instead of calling it 'n1', 'n_01', etc.
x = int(input("Enter the 1st term: "))
# For the same reason, we call the 2nd term 'y', instead of calling it 'n2', 'n_02', etc.
y = int(input("Enter the 2nd term: "))
# A Fibonacci sequence can be infinite,
# but here we have to make a finite one by asking the user for the number of terms.
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
# Initialize the list of a Fibonacci sequence.
Fib_seq = [x, y]

while len(Fib_seq) <= n:
    # The rule of Fibonacci sequence is X(n) = X(n-1) + X(n-2). Here, we use the variable 'z' for 'X(n)'.
    z = x + y
    Fib_seq.append(z)
    x = y
    y = z
print(f"The Fibonacci sequence you want is: {Fib_seq}")
