# Program to display an upside-down equilateral triangle (like below),
# using a nested for loop (a for inside another for).

# Example (the length of each side, or 'l', is 6, and the length of each line, 'n', is changing from 6 to 1):
# * * * * * *  Line 1, n = 6: 0 whitespaces; l - n == 0 whitespaces
#  * * * * *   Line 2, n = 5: 1 whitespaces; l - n == 1 whitespaces
#   * * * *    Line 3, n = 4: 2 whitespaces; l - n == 2 whitespaces
#    * * *     Line 4, n = 3: 3 whitespaces; l - n == 3 whitespaces
#     * *      Line 5, n = 2: 4 whitespaces; l - n == 4 whitespaces
#      *       Line 6, n = 1: 5 whitespaces; l - n  == 5 whitespaces

# Ask the user for the number of lines (also the length of the equilateral triangle):
l = int(input("Enter the number of lines (the length of each side): "))
unit = input("Enter the unit you want to build up the triangle: ")
for n in range(l, 0, -1):
    print(" " * (l - n), end="")
    for m in range(n):
        print(unit, end=" ")
    print("\n", end="")
