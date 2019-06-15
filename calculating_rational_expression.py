# This is a program to calculate the values of a rational expression (i.e., the ratio of two polynomials)
# of (x^2 - 1) / (x^2 + x - 2) as its variable x approaches 1 from both sides.


# Define a function for the given rational expression - (x + 1) / (x + 2) .
def fn(x):
    """This is the function standing for the given rational expression - (x + 1) / (x + 2)"""
    return round((x + 1) / (x + 2), 8)


# List of the corresponding values of the rational expression
# as x gets close to 1, going through 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.9, 0.99, 0.999, and 0.9999.

# Create a list of x values.
increments = [round(0.9 * (0.1**(n-1)), 10) for n in range(1, 5)]
# increments = [0.9, 0.09, 0.009, 0.0009]
x_vals = []
x = 0
for increment in increments:
    x += increment
    x_vals.append(x)

# Another version of creating 'x_vals' by referring to list comprehension.
# x_vals = [9 * int('1' * n) * 10**(-n) for n in range(1, 5)]

print(f"x_vals = {x_vals}")
for i, new_item in enumerate([round(0 + 0.1*(n-1), 10) for n in range(1, 7)], 0):
    # The target list of [0, 0.1, 0.2, 0.3, 0.4, 0.5] is an arithmetic sequence whose first term is 0
    # and the common difference is 0.1 .
    x_vals.insert(i, new_item)
print(f"The definite x_vals = {x_vals}")

# Create a list of the corresponding function values as x approaches 1, traversing through numbers of the list x_vals.
# , by substituting each number in the 'x_vals' list for x .
y_vals = list(map(fn, x_vals))
print(f"The corresponding y-values are {y_vals}")
coordinates = list(map(lambda x, y: (x, y), x_vals, y_vals))
for tuple in coordinates:
    print(tuple)
