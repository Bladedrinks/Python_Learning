# This file shows us a very typical wrong way to swap variables in Python and two other correct solutions.


# Below is a wrong way to swap variables x and y.
x = 1
y = 2
y = x  # Look up the value of 'x' in memory before performing the assignment operation. After searching Memory for x,
# we find x is equal to 1. Then, break the previous binding/association of the name 'y' to the value 2, and rebind 'y'
# to the new value 1. Thus, the name 'y' is bound to a new value 1 in memory, written as y = 1.
x = y  # Look up the value of 'y' in memory before doing the assignment statement. After searching the computer memory
# for y, we find out y is bound to 1. Then, we break the old binding/association of 'x' to 1, and rebind 'x' to the
# new value, which is also a 1. Therefore, the name 'x' is bound to 1 in memory, written as x = 1.

# For now, y is bound to 1 and x is also bound to 1

print(f"x = {x}")  # 1
print(f"y = {y}")  # 1


# ====== Correction ======
# Before running the following two correct solutions, we need to comment out the above code in order to avoid confusion.
#
# Solution 1 (a idiomatic way):
print("Solution 1:")
x = 1
y = 2
x, y = y, x
print(f"x = {x}")  # 2
print(f"y = {y}")  # 1

# Solution 2 (a common way without referring to any Python idioms):
print("Solution 2:")
x = 1
y = 2
temp = y
y = x
x = temp
print(f"x = {x}")  # 2
print(f"y = {y}")  # 1
# We create a new variable and bind it to the value of y in order to avoid losing the handle for the value 2.
# If we didn't make an intermediate variable 'temp' before rebinding 'y' to 1, the value of 'x', we would lose
# the handle for 2, the original value of y, and we would never get it back. If we lose the handle for the object 2
# in memory, how can we reuse it, later?


# To understand how the variables 'x', 'y', and 'temp' work, we draw an analogy between variables and sticky_notes.
