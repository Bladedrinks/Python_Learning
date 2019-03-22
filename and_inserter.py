# A user-defined function to insert 'and' between the second-last and the last items (two versions).

# Version 1:


def insert_and_in(list):
    """Insert the conjunction of " and " into a string (usually between the penultimate item and the last item.
    For example, we got a list:

                                          factors = [1, 3, 7, 21].

    We want to change it into a string without square brackets outside, like this:

                                                1, 3, 7 and 21
    """
    list_in_str = ""
    # test case: list = [45, 98, 45]
    # index:             -3  -2  -1
    # test case: list = [45]
    # index:             -1

    for i in range(-len(list), 0):  # Negating len(list), we get the negative index of the first item,
        # so the range(-len(list), 0) yields a sequence of all negative indices of items in the given list.
        # In the test case, for i in [-3, -2, -1]
        if i == -1:
            list_in_str += f"{list[i]}"
        elif i == -2:
            list_in_str += f"{list[i]} and "
        else:  # not(i == -1 or i == -2); the index of items is neither -1 nor -2 goes down here.
            list_in_str += f"{list[i]}, "
    return list_in_str


# Version 2 (refactored):


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



