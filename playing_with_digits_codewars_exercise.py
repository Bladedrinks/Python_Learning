# ====== Introduction ======

# This is a program to find out an integer k (if it exists) which a given integer n is multiplied by to get the sum of
# the given integer's own digits each raised to the power which comes from a series of numbers starting from p and
# ending with p + (d - 1). 'd' stands for the number of the given integer's digits.

# Given an integer n and a jumping-off power of p, the program should return the integer k mentioned above if it exists;
# returns -1 if there's no k that satisfies the property.

# Example 1:
# Given an integer n = 46288 and the jumping-off power of p = 3, we should find that there's an integer k = 51 such that
# 46288 x 51 = 4^3 + 6^4 + 2^5 + 8^6 + 8^7 = 64 + 1296 + 32 + 262144 + 2097152
# Notice: The powers to which the given integer's own digits are raised are exactly a successive number sequence
# starting from 3, which has been given as a precondition to us.

# Example 2:
# Given an integer n = 92 and the jumping-off power of p = 1, we should find that there's no such an integer k as making
# 92 x k equal to 9^1 + 2^2, since 9^1 + 2^2 = 13, which is indivisible by 92, or we can say, the result of 13 divided
# by 91 is not an integer.


# ====== Solution ======

# Step 1:
# Compute the sum of the given integer's own digits each raised to the power which comes from a series of numbers
# starting from p and ending with p + (d - 1). 'd' stands for the number of the given integer's digits.
# The result of Step 1 should be, say, 2360688, which is the sum of 4^3, 6^4, 2^5, 8^6, and 8^7, in the example of 46288

# Step 2:
# Divide the known sum value by the given integer and check if the quotient of this division is an integer.
# The example continues here: 2360688 / 46288 = 51, which is an integer.

# Step 3:
# Return the integer k if it exists; -1 otherwise.


# ====== Source Code ======

def dig_pow(n, p):
    """The documentation is EMPTY temporarily."""
    import math
    digits = []
    temp = n
    for t in range(len(str(temp))):
        rem = temp % 10
        digits.append(rem)
        temp = math.floor(temp / 10)
    powers = []
    t = 1
    temp = digits.copy()
    while t <= len(digits):
        digit = temp.pop()
        powers.append(pow(digit, p))
        t += 1
        p += 1
    Σ = sum(powers)
    k = Σ / n
    if k - math.floor(k) == 0:
        return int(k)
    else:
        return -1


# ====== Test ======
print(dig_pow(46288, 3))
