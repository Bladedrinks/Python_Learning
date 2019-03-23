# Two UDF equivalent to the built-in list.reverse() method.


def reverse_v1(list):
    """Return a copy of the given list in reverse order using the for loop."""
    new_list = []
    for i in range(len(list)):
        new_list.append(list.pop())
    return new_list


def reverse_v2(list):
    """Return a copy of the given list in reverse order using the while loop"""
    new_list = []
    temp = list[:]
    i = 0
    while i < len(temp):
        new_list.append(list.pop())
        i += 1
    return new_list
