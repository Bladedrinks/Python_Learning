# This is a program which helps estimate the limit of any function (which is represented by 'fn' in this program)
# as X approaches a particular value (which is denoted by 'X0' in the program),
# first by calculating the values of 'fn' as X approaches X0 (say, -6) from one side (say, -5.9, -5.99, -5.999, etc)
# and then by calculating the values of 'fn' as x approaches X0 from the other side (say, -6.1, -6.01, -6.001, etc.).


# To make the code 'DRY' (acronym for 'Don't Repeat Yourself.'), we make a UDF or User-Defined Function for the
# fractional part of each of the x-values approaching X0.
def fractional_part(a, r, n):
    """
    Return the value of the term 'Xn', which is equal to ar^(n-1), in the geometric sequence looking like:
    0.1, 0.01, 0.001, 0.0001, 0.00001, etc.

    In the expression of Xn (Rule for any term in geometric sequence), 'a' stands for the first term,
    'r' for the common ratio, and 'n' for the ordinal number of the specific term or the number of terms.
    """
    Xn = a * r**(n - 1)
    return Xn


def fn_expression(a, b, c, d, e, f):
    """
    Return a rational function (ratio of two polynomials) of the form:

                            ax^2 + bx + c
                          -----------------
                            dx^2 + ex + f

    where a, b, c, d, e and f are the coefficients of the terms of polynomials on top and bottom.

    Example:

    If the function is defined as:

                            x^2 + 3x + 2
                          -----------------
                               -x + 2

    , we have to pass in '1, 3, 2, 0, -1, 2' as the parameter where the delimiter is one comma and one whitespace.
    """
    return lambda x: (a*x**2 + b*x + c) / (d*x**2 + e*x + f)


def fn_value(fn_expression, x, n):
    """Return the value of the given function 'fn' rounded to 'n' decimal digits/places/numbers."""
    fn = fn_expression
    return round(fn(x), n)


X0 = int(input("X0 = "))
x_values_from_left = [round((X0-1) + (1 - fractional_part(0.1, 0.1, n)), 10) for n in range(1, 7)]
x_values_from_right = [round(X0 + fractional_part(0.1, 0.1, n), 10) for n in range(1, 7)]
print(f"x-values from the left : {x_values_from_left}\nx-values from the right: {x_values_from_right}", end='\n\n')

# Create a list of the function values as X approaches X0 from the left.
coefficients_in_str = input("Enter the coefficients of the top and bottom polynomials of your rational expression "
                            "(separated by a comma and a whitespace, like this: \"1, -2, 3, 0, 4, -5\"): ")
a, b, c, d, e, f = [int(num_in_str) for num_in_str in coefficients_in_str.split(sep=', ')]
y_values_at_x_values_from_left = [fn_value(fn_expression(a, b, c, d, e, f), x, 10) for x in x_values_from_left]
print(f"\ny-values at x-values from left: {y_values_at_x_values_from_left}")

# Create a list of the function values as X approaches X0 from the right.
y_values_at_x_values_from_right = [fn_value(fn_expression(a, b, c, d, e, f), x, 10) for x in x_values_from_right]
print(f"y-values at x-values from right: {y_values_at_x_values_from_right}")


table_of_fn_and_x = list(map(lambda x_left, y_left, x_right, y_right: (x_left, y_left, x_right, y_right),
                             x_values_from_left, y_values_at_x_values_from_left,
                             x_values_from_right, y_values_at_x_values_from_right))

# Make a list of the lengths (or the numbers of digits) of x_values approaching X0 from the left and return the length
# result which is gonna be used to make the table look neat and clear:
lengths_of_items_in_x_left = [len(str(num)) for num in x_values_from_left]

# Make a list of the lengths (or the numbers of digits) of x_values approaching X0 from the right and return the length
# result which is gonna be used to make the table look neat and clear:
lengths_of_items_in_x_right = [len(str(num)) for num in x_values_from_right]

# Make a list of the lengths (or the numbers of digits) of y_values as x approaches X0 from left and return the length
# result which is gonna be used to make the table look neat and clear:
lengths_of_items_in_y_left = [len(str(num)) for num in y_values_at_x_values_from_left]

# Make a table of the function values as X approaches X0 from both sides:
print(f"\nTable of the function values as x approaches {X0} from both sides:", end='\n\n')
print(f"x(left){' ' * (max(lengths_of_items_in_x_left) - len('x(left)') + 1)} "
      f"y(left){' ' * (max(lengths_of_items_in_y_left) - len('y(left)') + 1)} "
      f"x(right){' ' * (max(lengths_of_items_in_x_right) - len('x(right)') + 1)} "
      f"y(right)")
for x_left, y_left, x_right, y_right in table_of_fn_and_x:
    print(f"{x_left}{' ' * (max(lengths_of_items_in_x_left) - len(str(x_left)))}",
          f"{round(y_left, 6)}{' ' * (max(lengths_of_items_in_y_left) - len(str(round(y_left, 6))))}",
          f"{x_right}{' '* (max(lengths_of_items_in_x_right)-len(str(x_right)))}",
          round(y_right, 6), sep='  ')
if round(y_values_at_x_values_from_left[-1], 3) == round(y_values_at_x_values_from_right[-1], 3):
    print(f"\nThe limit of the function value as x approaches {X0} is: {round(y_values_at_x_values_from_left[-1], 3)}")
