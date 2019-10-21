# This file tells us what is the nature of assignment.


x = 10  # Bind a name 'x' to a value 10 (which is an object in computer memory)
y = x  # This line of code would better be read as "Bind a name 'y' to the value of 'x'."
# What we bind 'y' to is not the name 'x', but the value of it, or the value to which it is bound to.
# So, we bind 'y' to the value 10. That is, the assignment statement y = x is equivalent to y = 10.
z = y  # Same thing happens in this line of code. We bind a name 'z' to the value of 'y', which is 10.
# So, z = y is equivalent to z = 10
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

x = 20
print("------ After x = 20 ------")
print("")  # An empty string plus a newline character prints out a blank line.
print(f"x = {x}")  # x = 20
print(f"y = {y}")  # y = 10
print(f"z = {z}")  # z = 10

y = 30
print("------ After y = 30 ------")
print("")
print(f"x = {x}")  # x = 20
print(f"y = {y}")  # y = 30
print(f"z = {z}")  # z = 10

z = x  # Rebind the name 'z' to the value of 'x', which is 20, so the assignment statement z = x is equivalent to z = 20
print("------ After z = x ------")
print("")
print(f"x = {x}")  # x = 20
print(f"y = {y}")  # y = 30
print(f"z = {z}")  # z = 20

y = z  # Rebind the name 'y' to the current value of 'z', which is 20, so y = z is equivalent to y = 20
print("------ After y = z ------")
print(f"x = {x}")  # x = 20
print(f"y = {y}")  # y = 20
print(f"z = {z}")  # z = 20

# Notice: Each time we rebind a name to a new value, that implies the binding or the association of the name
# to the previous value is broken.
