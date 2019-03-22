# Program to display all the indices of a given number in a list.


def decision():
    """The control of the program will break out of the while loop if the user input is 'n'; the while loop will
    continue if the user input is 'y'; and the program will keep asking the user to enter the valid input if they
    enters neither 'y' nor 'n'."""
    decision = input("Do you want to keep searching? (y/n)  ")
    while not(decision == "y" or decision == "n"):
        decision = input("* * * User Tip: only 'y' and 'n' are valid input * * *\n"
                         "Do you want to keep searching? (y/n)  ")
    return decision


def insert_and_in(list):
    """
    Return a string form of the given list where a conjunction 'and' is inserted between the second-last item
    and the last item in a given list.

    Example:
                        nums = [3, 2, 3, 4, 5, 3, 6, 7, 8, 3, 9, 10, 11, 12, 3, 13, 14]
                      index:   0  1  2  3  4  5  6  7  8  9  10 11  12  13  14 15  16  17(= len(nums))
             negative index:                                         ...    -3 -2  -1
                                                                            14 - 17 = -3
                                                                            15 - 17 = -2
                                                                            16 - 17 = -1
                                                                            ...
                                                                     index - length = negative index

    Output:
                                3, 2, 3, 4, 5, 3, 6, 7, 8, 3, 9, 10, 11, 12, 3, 13 and 14

    We see that the output is a string, not a list any more, and a conjunction "and" has been inserted between
    the items '13' and '14'. This makes the string looks more like the English language, as a natural language, goes.
    """
    list_in_str = ""
    for item in list:
        if list.index(item) - len(list) == -2:  # The index of an item minus the length of the list is exactly equal to
            # the item's negative index
            list_in_str += str(item) + " and "
        else:
            list_in_str += str(item) + ", "
    return list_in_str[:-2]


ls = [1, 7, 3, 4, 5, 3, 6, 7, 1, 3, 7, 10, 11, 12, 3, 13, 14, 1, 1, 7, 3, 4, 99, 99, 3, 5]
#    0  1  2  3  4  5  6  7  8  9  10 11  12  13  14 15  16  17 18 19 20 21 22  23  24 25
# Indices of number '3' are: index 2, index 5, index 9, and index 14

# Another 'ls' test case:
# ls = ["Alabama", "Arantxa", "Atlas", "Bentlee", "Chichi", "Diem", "Drishti", "Atlas", "Arantxa", "Diem", "Arantxa", "Drishti", "Arantxa", "Bentlee", "Diem", "Bentlee", "Diem"]
# #     0          1          2        3          4         5       6          7        8          9      10         11         12         13         14      15         16

while True:
    # Ask the user for the number which he/she wants to know how many times appears in the list and whose indices are.
    # item = int(input("Enter the item: "))
    # Uncomment the following line if the given list is a list consisting of string items.
    item = input("Enter the item: ")

    # The number of times 'num' appears in the 'numbers' list.
    c = ls.count(item)
    # The given number must appear at least once in the list, otherwise the 'else' part will be triggered.
    # If 'c' is equal to 0, then the test_expression of if will evaluate to False and the 'else' part will be triggered.
    if c:
        # The indices of the given number is appended to 'indices' as a string data type.
        indices = []
        # 'i' stands for each 'index' of the given number. The initial value is set to -1 in order to make the initial
        # 'start' argument equal to 0, since the first iteration/loop would better start at the index of 0 (the first
        # item in the list) when we don't know whether the given number appears at the very beginning of the list.
        i = -1
        # 't' stands for 'times'. Since the condition of 'while' is set to 't <= c', the initial value of 't' is set
        # equal to 1.
        t = 1
        while t <= c:  # Say, c = 1, we only need to calling the .index() method once; c = 3, the condition of 'while'
            # becomes '1 <= 3' initially. From 1 to 3 (inclusive), we have three chances to call the .index() method.
            i = ls.index(item, i + 1)
            # The syntax of .index() method is:  list.index(x[, start[, end]])
            # Here, in addition to 'x', we only pass in the 'start' optional argument, because we can't be sure about
            # what is the end of the sub-sequence of the list where the given number appears.
            indices.append(i)
            t += 1
        if c > 1:
            print(f"The item \"{item}\" appears {ls.count(item)} times in this list "
                  f"and its indices are: {insert_and_in(indices)}")
        else:
            print(f"The item \"{item}\" appears only {ls.count(item)} time in this list "
                  f"and its index is: {insert_and_in(indices)}")
    else:
        print(f"Sorry. {item} appears {c} times in this list. We have no index to show you.")

    if decision() == "n":
        print("Thanks for using the app.")
        break


