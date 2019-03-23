# User-defined function to produce the floor of a number, the largest integer less than or equal to that number.
from random import uniform


def floor(x):
    """
    Return the floor of x, the greatest integer less than or equal to x.

    Examples:
              If x = 2.4, then floor(x) returns a value of 2;
              If x = -2.4, then floor(x) returns a value of -3.

    You might've wondered why -3? Why not -2?

    Among integers that are less than or equal to -2.4 are -3, -4, -5, etc.
    -2 is not included since -2 is greater than -2.4
    We see the largest integer among the integers mentioned above is -3,
    so the function returns it as the output, not -2.
    """
    return int(x // 1)


# ====== UDF Test ======
for t in range(1, 31):
    num = uniform(-100, 100)
    print(f"Test {t}: The floor of {num} is {floor(num)}")
