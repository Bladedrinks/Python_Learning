# This is a program which helps solve Exercise 2.1-20 in Thomas' Calculus.


# To DRY (which is an acronym for 'Don't Repeat Yourself') the code, we create UDFs for those repetitive lines of code.

def interpolate_and_in(list):
    """
    Return a string of comma-separated items from the given list. Between the last and the penultimate items
    a conjunction 'and' is interpolated. For example:
                                            Input: [1, 2, 3, 4]
                                            Output: 1, 2, 3 and 4
    The output is a string.
    """
    temp = list.copy()  # To prevent the for loop mutate the given list, we need to make a copy of it.
    for i in range(-1, -(len(list) + 1), -1):  # When counting backwards from the last character/item to the first
        # character/item, the first character/item's negative index is always the negated value of the length of the
        # given list. Since the 'end' parameter in the range(start, end, step) function is excluded, we have to add 1
        # to the 'len(list)' part.
        if i == -2:
            # Update the item by index assignment. The penultimate item is the most special item in this case.
            temp[i] = f'{temp[i]} and '  # Before 'and', sometimes we need a comma. You can interpolate one at any time.
        else:
            temp[i] = f'{temp[i]}, '
            # print(temp[i])
    str_with_and = ''.join(temp)[:-2]  # We make a slicing from the left end to the item at the index of -2 (not
    # included) because the string on output will look like this '1, 2, 3 and 4, '
    # if we don't eliminate the ', ' characters.
    return str_with_and


def names_of_moving(name, list_of_ordinal_numbers):
    """
    Return a list of names. Each 'item name' contains its ordinal number.

    For example:
                                Input: 'PQ', [1, 2, 3, 4, 5, 6]
                                Output: [PQ1, PQ2, PQ3, PQ4, PQ5, PQ6]
    """
    return [f'{name}{n}' for n in range(1, len(list_of_ordinal_numbers)+1)]


# Display the x-coordinate (i.e., abscissa) and y-coordinate (i.e., ordinate) of the moving point Q(T, f(T)).
x_vals = list(map(lambda h: 2 + h, [0.1 * pow(0.1, n-1) for n in range(1, 7)]))
# The values of h approaching zero (i.e., 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001) are a geometric sequence whose
# first item a=0.1, the common ratio r=1/10=0.1, and the rule is Xn = a * r^(n-1) = 0.1 * [0.1^(n-1)] where n is the
# ordinal number indicating the position of each item. For example, X1 = 0.1 * 0.1^(1-1) = 0.1 * 1 = 0.1
# , X2 = 0.1 * 0.1^(2-1) = 0.1 * 0.1^1 = 0.1 * 0.1 = 0.01 and X3 = 0.1 * 0.1^(3-1) = 0.1 * 0.1^2 = 0.001, etc.

# Instead of making reference to 'lambda expression', we can define a user-defined function for
# the 'function' parameter in the map(func, iter, ...) built-in function.
# def x_val_as_a_func_of(h):
#     """Return the x-coordinate (i.e. abscissa) as a function of h."""
#     return 2 + h
#
#
# x_vals = list(map(x_val_as_a_func_of, [0.1 * pow(0.1, n-1) for n in range(1, 7)]))

y_vals = list(map(lambda x: round(1 / x, 10), x_vals))
# Since f(t) = 1/t, the function coming after the colon should be 1 / x
print(f"\nThe t-coordinates (abscissae) of point Q are {interpolate_and_in(x_vals)}"
      f"\nThe y-coordinates (ordinates) of point Q are {interpolate_and_in(y_vals)}", end='\n\n')

# The x-y coordinates of points Q1, Q2, Q3, etc.
coords_of_Q = list(map(lambda x, y: (x, y), x_vals, y_vals))
names_of_Q = names_of_moving('Q', x_vals)
print(f"The abscissae and ordinates of points {interpolate_and_in(names_of_Q)} are: \n{interpolate_and_in(coords_of_Q)}"
      , end='\n\n')

# The slopes of the secants PQ1, PQ2, PQ3, etc. The point P is identified with (2, 0.5)
slopes_of_secant_PQ = list(map(lambda x, y: round((y - 0.5) / (x - 2), 10), x_vals, y_vals))
names_of_PQ = names_of_moving('PQ', x_vals)
print(f"The slopes of the secants {interpolate_and_in(names_of_PQ)} are approximately \n"
      f"{interpolate_and_in(slopes_of_secant_PQ)} .")
