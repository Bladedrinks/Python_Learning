# This is a new version of UDF which interpolates the word 'and' in between the last and penultimate items in a list.


def interpolate_and_in(list):
    """Return a string of comma-separated items from the given list. Between the last and the penultimate items
    a conjunction 'and' is interpolated."""
    temp = list.copy()
    for i in range(-1, -(len(list) + 1), -1):
        if i == -2:
            temp[i] = temp[i] + ' and '
        else:
            temp[i] = temp[i] + ', '
            # print(temp[i])
    str_with_and = ''.join(temp)[:-2]
    return str_with_and




