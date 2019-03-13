# Program to define a function which solve for the absolute value of any real number.

import time


def abs_val_v1(x):
    """Return the absolute value of any real number."""
    # This function is coded based off of the following mathematical definition:
    # The absolute value of a number x, denoted by |x|, is defined by the formula:
    #
    #                             x, x >= 0
    #                      |x| =
    #                            -x, x <  0.
    #
    # (For more information, see: Maurice D. Weir, Joel Hass, and George B. Thomas, Jr., Thomas' Calculus: Early
    # Transcendentals (12th edition). Boston, US: Addison_Wesley, AP-4/5.)
    # According the mathematical definition shown above, we define the function as:
    if x >= 0:
        return x
    else:
        return -x


def abs_val_v2(x):
    """Return the absolute value of any real number."""
    import math
    # Since the symbol √a always denotes the non-negative square root of a, an alternative definition of the absolute
    # value of a number x is
    #
    #                      |x| = √(x^2)
    #
    # (For more information, see: Maurice D. Weir, Joel Hass, and George B. Thomas, Jr., Thomas' Calculus: Early
    # Transcendentals (12th edition). Boston, US: Addison_Wesley, AP-4/5.)
    # According the mathematical definition shown above, we define the function as:
    return round(math.sqrt(pow(x, 2)))
    # The time which this 'abs_val_v2' function takes is four times longer than the 'abs_val_01' function.


# ====== Test UDF ======
for num in range(-20, 21):
    print(f"The absolute value of {num} is {abs_val_v2(num)}")


# ====== Time Test ======
t1 = time.time()
for num in range(-10000000, 10000000):
    abs_val_v2(num)
t2 = time.time()
print(f"The test took {t2 - t1} seconds.")
# 27.41444420814514
