# This program helps investigate what the computer values of f(x) = [(x^2 + 100)^(1/2) - 10] / x^2 as x approaches 0 .

# ====== Introduction ======
# Page 70 in the book called Thomas' Calculus says, as x approaches 0 through the values ±1, ±0.5, ±0.10, and ±0.01,
# the function seems to approach 0.05; as we take even smaller values of x, ±0.0005, ±0.0001, ±0.00001, and ±0.000001,
# the function appears to approach 0 .
# This is a bit too weird since generally as the values of x approach some number, the function value is gonna be
# approaching a single value, not two values.
# The book believes that computer should be blamed for this 'error'.

# ====== Source Code ======
import math
# Create a list of x-values containing ±1, ±0.5, ±0.1, ±0.01, ±0.0005, ±0.0001, ±0.00001, and ±0.000001
abscissae = [1, 0.5, 0.1, 0.01, 0.0005, 0.0001, 0.00001, 0.000001]

# Calculate the y-values corresponding to the given x-values using lambda expression and the built-in map() function.
ordinates = list(map(lambda x: (math.sqrt(pow(x, 2) + 100) - 10) / pow(x, 2), abscissae))

# Display all the x-values and the corresponding function values in a tuple form.
list_of_coordinates = list(map(lambda x, y: (x, y), abscissae, ordinates))
for coords in list_of_coordinates:
    print(coords)
# Output:
# (1, 0.049875621120889946)
# (0.5, 0.049968789001574976)
# (0.1, 0.049998750062485435)
# (0.01, 0.04999998751031853)
# (0.0005, 0.04999999703159119)
# (0.0001, 0.05000000413701855)
# (0.00001, 0.050004445029117044)
# (0.000001, 0.04973799150320701)


# Conclusion: the weird thing appears at the end of the list of coordinates. The function value of x=0.000001 should be
# greater than 0.05 at least. Instead, it's 0.04973... which is less than 0.05.
