# This is a program which helps estimate the limit of a trigonometric function (which is represented by 'trig_fn' in
# this program) as X approaches a particular value (which is denoted by 'X0' in the program), first by calculating the
# values of 'trig_fn' as X approaches X0 (say, 0) from one side (say, -0.1, -0.01, -0.001, etc.) and then by calculating
# the values of 'trig_fn' as x approaches X0 from the other side (say, -0.1, -0.01, -0.001, etc.).
import math


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


def fn(x):
    """Return the value of the given function."""
    import math
    # return (x**4 - 16) / (x - 2)
    # return ((1 + x)**(1/3) - 1) / x
    # return (x**2 - 9) / (math.sqrt(x**2 + 7) - 4)
    # return (1 - math.cos(x)) / (x * math.sin(x))
    return 2*x**2 / (3 - 3*math.cos(x))


X0 = int(input("X0 = "))
ndigits_for_x = int(input("Round each x-value to: "))
x_values_from_left = [round((X0-1) + (1 - fractional_part(0.1, 0.1, n)), ndigits_for_x) for n in range(1, 7)]
x_values_from_right = [round(X0 + fractional_part(0.1, 0.1, n), ndigits_for_x) for n in range(1, 7)]
print(f"x-values from the left : {x_values_from_left}\nx-values from the right: {x_values_from_right}", end='\n\n')

# Create a list of the function values as X approaches X0 from the left.
ndigits_for_y = int(input("Round each y-value to: "))
y_values_at_x_values_from_left = [round(fn(x), ndigits_for_y) for x in x_values_from_left]
print(f"\ny-values at x-values from left: {y_values_at_x_values_from_left}")

# Create a list of the function values as X approaches X0 from the right.
y_values_at_x_values_from_right = [round(fn(x), ndigits_for_y) for x in x_values_from_right]
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
print(f"\nTable of the function values as x approaches {X0} from both sides:")
for x_left, y_left, x_right, y_right in table_of_fn_and_x:
    print(f"{x_left}{' ' * (max(lengths_of_items_in_x_left) - len(str(x_left)))}",
          f"{y_left}{' ' * (max(lengths_of_items_in_y_left) - len(str(y_left)))}",
          f"{x_right}{' '* (max(lengths_of_items_in_x_right)-len(str(x_right)))}", y_right, sep='  ')
if int(y_values_at_x_values_from_left[-1]) > int(y_values_at_x_values_from_left[0]) \
        and int(y_values_at_x_values_from_right[-1]) > int(y_values_at_x_values_from_right[0]):
    if y_values_at_x_values_from_left[-1] > 0 and y_values_at_x_values_from_right[-1] > 0:
        print(f"\nThe limit of the function value as x approaches {X0} is: infinity")
    else:
        print(f"\nThe limit of the function value as x approaches {X0} is: -infinity")
else:
    # round(y_values_at_x_values_from_left[-1], 3) == round(y_values_at_x_values_from_right[-1], 3)
    print(f"\nThe limit of the function value as x approaches {X0} is: {round(y_values_at_x_values_from_left[-1], 5)}")
