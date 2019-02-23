# Program to display an isosceles triangle built up only by one kind of unit/symbol (such as *, $, ^, @, etc).
# The symbol and the number of the lines (the height of the triangle) are given by the user.
# Later we're gonna make a user-defined function based off of the program.

unit = input("Enter the shape you want to build up the triangle: ")
n = int(input("Enter the number of lines you want: "))
for i in range(1, n + 1):  # The iterator variable 'i' is assigned values of 1, 2, 3, 4 and 5
    print(" " * (n - i), end="")
    for j in range(i):
        print(unit, end=" ")
    print("\n", end="")
# When i = 1, j = 0. And the body of the nested for loop is executed once
# - '* ' (one asterisk and a whitespace character) is printed out.
# When i = 2, j = 0 and 1. Since we got two values (no matter what they are), the body of the nested for loop is
# executed two times - '* ' is printed out twice, or you can say, '* * ' (two asterisks and two whitespace characters
# interspersed in them) is printed out.
# When i = 3, j = 0, 1 and 2. Since we got three values, the body of the nested for loop is executed three times
# - '* ' is printed out three times, or you can say, '* * * ' is printed out.
# When i = 4, j = 0, 1, 2 and 3. Since we got four values, the body of the nested for loop is executed four times
# - '* ' is printed out four times, or you can say, '* * * * ' is printed out.
# When i = 5, j = 0, 1, 2, 3 and 4. Since we got five values, the body of the nested for loop is executed five times
# - '* ' is printed out five values, or you can say, '* * * * * ' is printed out.

# The final output is (if 'n'(the number of lines) is 5):
#     *      Line 1, i = 1: 4 whitespaces; n - i == 4 whitespaces
#    * *     Line 2, i = 2: 3 whitespaces; n - i == 3 whitespaces
#   * * *    Line 3, i = 3: 2 whitespaces; n - i == 2 whitespaces
#  * * * *   Line 4, i = 4: 1 whitespaces; n - i == 1 whitespaces
# * * * * *  Line 5, i = 5: 0 whitespaces; n - i == 0 whitespaces
#
# The final output is (if 'n'(the number of lines) is 6):
#      *       Line 1, i = 1: 5 whitespaces; n - i == 5 whitespaces
#     * *      Line 2, i = 2: 4 whitespaces; n - i == 4 whitespaces
#    * * *     Line 3, i = 3: 3 whitespaces; n - i == 3 whitespaces
#   * * * *    Line 4, i = 4: 2 whitespaces; n - i == 2 whitespaces
#  * * * * *   Line 5, i = 5: 1 whitespaces; n - i == 1 whitespaces
# * * * * * *  Line 6, i = 5: 0 whitespaces; n - i == 0 whitespaces


# ====== UDF version of the program ======
def isosceles_triangle(unit, n):
    """Prints an isosceles triangle of which the unit and the number of lines are given by the user.
    The first parameter must be a string, otherwise the Python Interpreter will freak out and throw
    an error, which says, 'invalid syntax'. And the first parameter must be a symbol of single character,
    such as '*', '%', '(', '@', 'o', but not '()'."""
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(i):
            print(unit, end=" ")
        print("\n", end="")


# ====== Test UDF ======
isosceles_triangle("+", 5)
