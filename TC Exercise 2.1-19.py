# This files contains a program which helps us solve Exercise 2.1-19 in Thomas' Calculus.
import math


def interpolate_and_in(list):
    """Return a string of comma-separated items from the given list. Between the last and the penultimate items
    a conjunction 'and' is interpolated."""
    temp = list.copy()  # To prevent the for loop mutate the given list, we need to make a copy of it.
    for i in range(-1, -(len(list) + 1), -1):
        if i == -2:
            temp[i] = f'{temp[i]} and '  # Before 'and', sometimes we need a comma. You can interpolate one at any time.
        else:
            temp[i] = f'{temp[i]}, '
            # print(temp[i])
    str_with_and = ''.join(temp)[:-2]
    return str_with_and


# Display the x and y values of the moving point Q, respectively.
x_vals = list(map(lambda h: 1 + h, [1 / pow(10, n) for n in range(1, 7)]))
y_vals = list(map(lambda x: round(math.sqrt(x), 10), x_vals))
print(f"\nThe x values of point Q are {interpolate_and_in(x_vals)}"
      f"\nThe y values of point Q are {interpolate_and_in(y_vals)}", end='\n\n')

# The x-y coordinates of points Q1, Q2, Q3, etc.
coords_of_Q = list(map(lambda x, y: (x, y), x_vals, y_vals))
names_of_Q = [f"Q{n}" for n in range(1, len(x_vals) + 1)]
print(f"The coordinates of points {interpolate_and_in(names_of_Q)} are: \n{interpolate_and_in(coords_of_Q)}", end='\n\n')

# The slopes of the secants PQ1, PQ2, PQ3, etc.
slopes_of_secant_PQ = list(map(lambda x, y: round((1 - y) / (1 - x), 10), x_vals, y_vals))
names_of_PQ = [f'PQ{n}' for n in range(1, len(x_vals)+1)]
print(f"The slopes of the secants {interpolate_and_in(names_of_PQ)} are approximately \n"
      f"{interpolate_and_in(slopes_of_secant_PQ)} .")
