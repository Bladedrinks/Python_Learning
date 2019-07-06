# This file shows how metasyntactic variables are used while programming, specifically for teaching programming
# languages. The most commonly used names/words for metasyntactic variable include (but are by no means limited to :
# 'foo', 'fum', 'bar', 'foobar', 'qux', 'spam', 'ham', 'egg', 'ham egg', etc. (By the way, 'metasyntactic variable'
# literally means 'the variables that are beyond the syntax of (a specific programming language, say, Python')

# When do we use "metasyntactic variables"?
# For example, when you are teaching students how to define a function that returns the sum of two squares and you don't
# know how to name that function properly at the time, and don't want to spend time on function naming, then you can use
# "metasyntactic variables" (say, 'foo', 'bar', 'foobar', 'spam', 'ham', 'egg', etc.) to name the function temporarily.
# You and your students both know that these "nonsense" function names are just placeholders to be used for helping us
# complete the teaching goal - how to define a function returning the sum of two squares.

# Here's an example for illustrating in what kind of situation we use metasyntactic variables.

# Let's see how we define a function by referring to the other function defined by the user before.


# First we define a function named 'foo' (Notice, 'foo' as a variable name is nonsense. You don't have to wonder why we
# use this word here since it's just a metasyntactic variable or a placeholder.)
def foo():
    """Print out three lines of string starting with the word 'foo' and ending with 'line X' where 'X' is different
    depending on the position of the line."""
    print("foo line 1")
    print("foo line 2")
    print("foo line 3")


# Define a function named 'fum'
def fum():
    """Print out three lines of string. Each line of words starts with the metasyntactic variable name 'fum'."""
    print("fum line 1")
    print("fum line 2")
    print("fum line 3")


def bar():
    """Print out two lines of string. Each line of words starts with the metasyntactic variable names 'bar'.
    and invoke the functions foo() and fum() defined above."""
    print("bar line 1")
    foo()
    fum()
    print("bar line 4")


def go():
    """Invoke the function bar() defined right above."""
    bar()


go()
