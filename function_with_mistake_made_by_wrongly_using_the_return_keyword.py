# This file contains a buggy/broken function definition
# and the solution to the bug which results from the 'return' statement.
# Source: https://www.udemy.com/the-modern-python3-bootcamp/learn/quiz/4368530#bookmarks


# ====== Source Code (buggy version) ======
def count_dollar_signs_v1(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
        return count


# ====== A Walk-through Before Fixing The Bug ======
# The goal of this function is:
# Return the number of the $ (dollar sign) characters in the given string literal.
# For example, if we call the 'count_dollar_signs' function on the string literal '$uper $ize',
# the function should return a number 2, in that the given literal contains two $ characters in total.
#
# Now, let's walk through the entire code line by line:
#
# We start with the 'count' variable and initialize it to 0, since the reason we create this variable is
# to record or count up how many times the $ character appears in the given string literal, or how many
# instances of the dollar sign are there in the given string literal. With the help of the increment counter
# (i.e., count += 1), each time when we find an instance of dollar sign, it will add 1 to the 'count' variable.
#
# We loop through each 'char' (i.e., character) in 'word', which contains the given string literal.
# If the 'char' is '$', we add 1 to 'count'. Right after the body of the 'if' statement is executed,
# we return 'count'.

# ====== Bug Finding And Fixing ======
# Since the 'return' statement is aligned with the 'if' statement, when the suite of the 'for' statement
# is executed, it will be executed right after the 'if' statement.
# When the iteration encounters the first $ character, the 'condition' (or 'test_expression') of the 'if' statement
# is True, then 'count' is assigned 0 + 1, which is 1.
# And then, as we said before, the 'return' statement is aligned with the 'if' statement,
# it will be executed on the spot.
# When the 'return' statement is executed, the execution of the entire function is terminated immediately.
# And finally what we could get is a return value of 1, rather than the expected value of 2.
# Therefore, to fix the bug, we have to indent the 'return' statement correctly, or out-dent/un-indent it from
# the original place one 'tab' to the left, just like the corrected version shown below.
# Since the 'return' statement now is aligned with the 'for' statement, it will only be executed after the entire for
# statement is exhausted or finished. Thus, what 'count' contains is the total number of the $ characters.


# Without adding any new lines of code, make count_dollar_signs work as intended:
def count_dollar_signs_v2(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count


# ====== TEST ======
word = "$uper $ize"
print("The string literal '{0}' contains {1} $ (dollar sign characters).".format(word, count_dollar_signs_v2(word)))
