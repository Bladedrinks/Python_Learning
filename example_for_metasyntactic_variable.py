# This file shows how metasyntactic variables are used while programming, specifically for teaching programming
# languages. The most commonly used names/words for metasyntactic variable include (but are by no means limited to :
# 'foo', 'fum', 'bar', 'foobar', 'qux', 'spam', 'ham', 'egg', 'ham egg', etc. (By the way, 'metasyntactic variable'
# literally means 'the variables that are beyond the syntax of (a specific programming language, say, Python')


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
