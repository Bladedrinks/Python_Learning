# Define a function to add ordinal suffix (like 'st' in '1st', 'nd' in '2nd', 'rd' in '3rd', 'th' in '4th', etc) to
# a ordinal number.


def ordinal(num):
    """Returns the ordinal form of the given number.
    For example, if the parameter is '2', the function will return '2nd'.
    If the parameter is 12, the function will return '12th'."""
    num = str(num)
    if num[-2:] == "11" or num[-2:] == "12" or num[-2:] == "13":
        return f"{num}th"
    elif num[-1] == "1":
        return f"{num}st"
    elif num[-1] == "2":
        return f"{num}nd"
    elif num[-1] == "3":
        return f"{num}rd"
    else:
        return f"{num}th"



