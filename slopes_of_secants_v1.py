# This is a program to return a list of numbers which are the slopes of secant PQ, or Δs/Δt (meters/sec).

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

# Calculate the slopes of the secant PQ using a for loop
# and put the results in a list named 'slopes_of_secant_PQ'.
# coords_of_Q = [(10.0, 225.0), (14.0, 375.0), (16.5, 475.0), (18.0, 550.0)]

# Ask the user for the coordinates of point P and convert the input to a tuple:
coords_of_P = tuple(float(val) for val in input("Enter the x and y values of point P respectively, "
                                                "separated by a whitespace character: ").split())
print(coords_of_P)

x_val_of_P, y_val_of_P = coords_of_P  # Assign values to t and s of point P using sequence unpacking.
slopes_of_secant_PQ = []  # Initialize the variable that will contain
# the slopes of the secant PQ as point Q approaches point P.
for x, y in coords_of_Qs:  # Since each item in the 'coords_of_Qs' list is a 2-tuple of x and y values, we can combine
    # the 'sequence unpacking' thing with the for statement.
    # slope_of_secant_PQ = Δy / Δx = (650 - y) / (20 - x)
    slope = round((y_val_of_P - y) / (x_val_of_P - x), 2)
    slopes_of_secant_PQ.append(slope)
# The for loop can be rewritten as a list comprehension:
# slopes_of_secant_PQ = [round((y_val_of_P - y) / (x_val_of_P - x), 2) for x, y in coords_of_Qs]
print(f"The slopes of the secant PQ are approximately: {slopes_of_secant_PQ}")
