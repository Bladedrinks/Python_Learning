# This is a program to return a list of numbers which are the slopes of secant PQ, or Δy/Δx.

# Ask the user for the x and y coordinates of points Q
# and add each pair of x-y coordinates as a 2-tuple to a list named 'coords_of_Qs',
# since we're gonna move point Q toward P along the curve in a bit to arbitrarily graph at least four secant lines PQ1,
# PQ2, PQ3, and PQ4.
coords_of_Qs = []  # Initialize a variable standing for the coordinates of Q1, Q2, Q3, and Q4.
c = 1  # Initialize the counter, or counting number, as 1.
while True:  # Since we don't how many points Q the user is gonna take,
    # we ought to set the while condition equal to True, a boolean value which can keep the while loop on and on and on.
    print(f"The x and y coordinates of point Q{c}: ")
    x = float(input(f"Enter the x value of point Q{c}: "))
    y = float(input(f"Enter the y value of point Q{c}: "))
    coords_of_Qs.append((x, y))
    decision = input("Do you want to keep adding points? (y/n - case insensitive) ").lower()
    while decision != 'y' and decision != 'n':  # which is equivalent to: not(decision == 'y' or decision == 'n')
        decision = input("User Tip: Only 'y' and 'n' (case insensitive) are valid answers."
                         "\nDo you want to keep adding points? (y/n) ").lower()
    if decision == 'n':
        break
    c += 1  # The 'counter increment' is set equal to 1.
print(f"The coordinates of points Q (from Q1 to Q4) are: {coords_of_Qs}")
# coords_of_Qs: [(10.0, 225.0), (14.0, 375.0), (16.5, 475.0), (18.0, 550.0)]

# Create two lists containing the x values and the y values of Point Q, respectively.
x_vals_of_Q = [coords[0] for coords in coords_of_Qs]
y_vals_of_Q = [coords[1] for coords in coords_of_Qs]
print(f"The x values of Point Q: {x_vals_of_Q}\nThe y values of Point Q: {y_vals_of_Q}")

# Calculate the slopes of the secant PQ using lambda expression and the built-in map() function.
# and put the results in a list named 'slopes_of_secant_PQ'.

# Ask the user for the coordinates of point P and convert the input to a tuple:
coords_of_P = tuple(float(val) for val in input("Enter the x and y values of point P respectively, "
                                                "separated by a whitespace character: ").split())
x_val_of_P, y_val_of_P = coords_of_P  # Assign values to t and s of point P using sequence unpacking.
slopes_of_secant_PQ = list(map(lambda x_of_Q, y_of_Q: round((y_val_of_P - y_of_Q) / (x_val_of_P - x_of_Q), 2),
                               x_vals_of_Q, y_vals_of_Q))
print(f"The slopes of the secant PQ are approximately: {slopes_of_secant_PQ}")
