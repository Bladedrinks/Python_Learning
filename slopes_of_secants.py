# This is a program to return a list of numbers which are the slopes of secant PQ, or Δs/Δt (meters/sec).

# Ask the user for the s and t coordinates of points Q
# and add each pair of s-t coordinates as a 2-tuple to a list named 'coords_of_Q'.
coords_of_Q = []
c = 1
while True:
    print(f"The t and s coordinates of Point Q{c}: ")
    t = float(input(f"Enter the t value of point Q{c}: "))
    s = float(input(f"Enter the s value of point Q{c}: "))
    coords_of_Q.append((t, s))
    decision = input("Do you want to keep adding points? (y/n) ")
    while not(decision == 'y' or decision == 'n'):
        decision = input("User Tip: Only 'y' or 'n' is valid."
                         "\nDo you want to keep adding points? (y/n) ")
    if decision == 'n':
        break
    c += 1
print(f"The coordinates of points Q (from Q1 to Q4) are: {coords_of_Q}")

# Calculate the slopes of the secant PQ using a for loop
# and put the results in a list named 'slopes_of_secant_PQ'.
# coords_of_Q =
coords_of_P = tuple(float(val) for val in input("Enter the t and s values of point P respectively, "
                                                "separated by a whitespace character: ").split())
print(coords_of_P)
t_val_of_P, s_val_of_P = coords_of_P  # Assign values to t and s of point P using sequence unpacking.
slopes_of_secant_PQ = []
for coord_of_Q in coords_of_Q:
    t, s = coord_of_Q  # Sequence unpacking
    # slope_of_secant_PQ = Δs / Δt = (650 - s) / (20 - t)
    slope = round((s_val_of_P - s) / (t_val_of_P - t), 4)
    slopes_of_secant_PQ.append(slope)
print(f"The slopes of the secant PQ are approximately: {slopes_of_secant_PQ}")
