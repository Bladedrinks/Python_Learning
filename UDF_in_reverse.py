# User-defined function to print a list in reverse order (from the last to the first item)
# using 'while' and 'for' in loops.


def in_reverse(list):
    """Return the original list in reverse order."""
    list_in_reverse = []
    i = len(list) - 1
    while i >= 0:
        list_in_reverse.append(list[i])
        i = i - 1
    return list_in_reverse


# ====== Test Function ======
test_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(in_reverse(test_list))
