# This file contains the source code downloaded from https://realpython.com/python-thinking-recursively/ and MY COMMENT.
# The problem which the source code fixes is finding the sum of the numbers 1 all the way through up to 10.
# The algorithm in this source code is quite different from the algorithm which I create in the file "sum_down_to_one".


def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum
    # Why 11?
    # The final goal of this sum_recursive() function is to return the summation of 1 all the way up to 10, meaning the
    # final operand in this addition operation is 10. 'current_number == 11' is just the condition which is used to
    # stop the process of successive addition.

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)


# Pass the initial state
print(sum_recursive(1, 0))
# The expected output: 55

# Call the sum_recursive() function on 1 and 0,
# which are 'current_number' (i.e., the starting number) and 'accumulated_sum', respectively.

# sum_recursive(1, 0)

# Calling sum_recursive() (on 1 and 0) triggers the definition:
# Since the current_number(=1) != 11, the control flow goes to the 'else' part:
# return: sum_recursive(1 + 1, 0 + 1), or sum_recursive(2, 1)

# Calling sum_recursive() (on 2 and 1) triggers the definition:
# Since the current_number(=2) != 11, the control flow goes to the 'else' part:
# return: sum_recursive(2 + 1, 1 + 2), or sum_recursive(3, 3)

# Calling sum_recursive() (on 3 and 3) triggers the definition:
# Since the current_number(=3) != 11, the control flow goes to the 'else' part:
# return: sum_recursive(3 + 1, 3 + 3), or sum_recursive(4, 6)

# Calling sum_recursive() (on 4 and 6) triggers the definition:
# Since the current_number(=4) != 11, the control flow goes to the 'else' part:
# return: sum_recursive(4 + 1, 6 + 4), or sum_recursive(5, 10)

# Calling sum_recursive() (on 5 and 10) triggers the definition:
# Since the current_number(=5) != 11, the control flow goes to the 'else' part:
# return: sum_recursive(5 + 1, 10 + 5), or sum_recursive(6, 15)

# Calling sum_recursive() (on 6 and 15) triggers the definition:
# Since the current_number(=6) != 11, the control flow goes to the 'else' part:
# return: sum_recursive(6 + 1, 15 + 6), or sum_recursive(7, 21)

# Calling sum_recursive() (on 7 and 21) triggers the definition:
# Since the current_number(=7) != 11, the control flow goes to the 'else' part:
# return: sum_recursive(7 + 1, 21 + 7), or sum_recursive(8, 28)

# Calling sum_recursive() (on 8 and 28) triggers the definition:
# Since the current_number(=8) != 11, the control flow goes to the 'else' part:
# return: sum_recursive(8 + 1, 28 + 8), or sum_recursive(9, 36)

# Calling sum_recursive() (on 9 and 36) triggers the definition:
# Since the current_number(=9) != 11, the control flow goes to the 'else' part:
# return: sum_recursive(9 + 1, 36 + 9), or sum_recursive(10, 45)

# Calling sum_recursive() (on 10 and 45) triggers the definition:
# Since the current_number(=10) != 11, the control flow goes to the 'else' part:
# return: sum_recursive(10 + 1, 45 + 10), or sum_recursive(11, 55)

# Calling sum_recursive() (on 11 and 55) triggers the definition:
# Since the current_number(=11) == 11, the control flow goes to the 'if' part:
# return: accumulated_sum(=55)

