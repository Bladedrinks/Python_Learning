# This is a program to help estimate the limit of f(x) = (x^2 - 9) / (x + 3) as x approaches -3
# at first by calculating the values of f(x) as x approaches -3 from the left (say, -3.1, -3.01, -3.001, etc.)
# and then by calculating the values of f(x) as x approaches -3 from the right (say, -2.9, -2.99, -2.999, etc.).


# To make the code 'DRY' (acronym for 'Don't Repeat Yourself.'), we make a UDF or User-Defined Function for the
# fractional part of each of the x-values approaching -3.
def fractional_part(a, r, n):
    """
    Return the term Xn, which is equal to ar^(n-1), in the geometric sequence looking like:
    0.1, 0.01, 0.001, 0.0001, 0.00001, etc
    a is the first term, r is the common ratio, and n is the ordinal number of it.
    """
    Xn = a * r**(n - 1)
    return Xn


def f(x):
    """Return the value of function f(x) = (x^2 - 9) / (x + 3)."""
    return round((x**2 - 9) / (x + 3), 6)


# Create a list of x-values which looks like this [-3.1, -3.01, -3.001, -3.0001, -3.00001, -3.000001]
# x_values_from_left = [-(3 + (0.1 * 0.1**(n-1))) for n in range(1, 7)]
# Each number in this list consists of two parts:
# one is the integral part (-3) and the other is the fractional part (0.1, 0.01, 0.001, etc.).
# Another version using UDF:
x_values_from_left = [-(3 + fractional_part(0.1, 0.1, n)) for n in range(1, 7)]
print(x_values_from_left)

# Create a list of x-values which looks like this [-2.9, -2.99, -2.999, -2.9999, -2.99999, -2.999999]
# x_values_from_right = [round(-(2 + (1 - (0.1 * 0.1**(n-1)))), 10) for n in range(1, 7)]
# Another version using UDF:
x_values_from_right = [round(-(2 + (1 - fractional_part(0.1, 0.1, n))), 10) for n in range(1, 7)]
print(x_values_from_right)

# Create a list of the function values as x approaches -3 from the left.
y_values_at_x_values_from_left = [f(x_value) for x_value in x_values_from_left]
print(y_values_at_x_values_from_left)
# Create a list of the function values as x approaches -3 from the right.
y_values_at_x_values_from_right = [f(x_value) for x_value in x_values_from_right]
print(y_values_at_x_values_from_right)

# Now we make a table of the values of f(x) as x approaches -3 from both sides.
table_of_fn_and_x = list(map(lambda x_left, y_left, x_right, y_right: (x_left, y_left, x_right, y_right),
                             x_values_from_left, y_values_at_x_values_from_left,
                             x_values_from_right, y_values_at_x_values_from_right))
for row in table_of_fn_and_x:
    print(row)
