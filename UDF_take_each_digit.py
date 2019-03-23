# Program to return a list consisting of all the digits of a given number.


def take_each_digit(num):
    """
    Return a list consisting of all the digits of a given number which can be negative.

    Example: We have a number 65473298 and pass in the number as parameter.

    Output: [6, 5, 4, 7, 3, 2, 9, 8]  # It's a list consisting of all digits that make 65473298

    """
    if num < 0:
        num = -num
    # if 'num' is negative, the floor() function won't return its integral part but the greatest integer less than or
    # equal to it. So we have to convert the negative number into a positive number. (By the way, another way to negate
    # a positive number is using the *= operator - 'num *= -1')
    from math import floor
    digits = []
    for t in range(len(str(num))):
        digit_at_1s = num % 10  # Calling the modulus operation on any integer returns the digit at the ones' place.
        digits[len(digits):] = [digit_at_1s]  # list[len(list):] is equivalent to the list.append(x) method, adding
        # an item to the end of the given list.
        num = num // 10  # Note that The floor division doesn't return the integral part of the given number if that
        # number is non-negative. For more information about the floor division, see:
        # https://docs.python.org/3/glossary.html#term-floor-division

        # Alternate way to perform the same task as 'num = num // 10' does:
        # num = floor(num / 10)
        # Any integer (say, 12345) divided by 10 gets us a decimal (say, 1234.5) whose fractional part has only one
        # decimal digit. And then calling the floor() function on that decimal returns the integral part (say, 1234)
        # if the decimal is non-negative (Because the floor(x) function returns the floor of x, the largest integer less
        # than or equal to x. About the floor(x) function, see:
        # https://docs.python.org/3/library/math.html
    digits.reverse()
    return digits


# ====== UDF Test ======
test_list = [123456, 456789, -98765, 348623948, -32423427987]
for number in test_list:
    print(f"The list of all digits in {number} is: {take_each_digit(number)}")


