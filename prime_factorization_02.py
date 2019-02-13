# Program for prime factorization,
# which only print each prime factor one time even if it occurs more than one time.

# ========== Test ==========
# n = 3 x 5 = 15

n = int(input("Enter an integer: "))  # n = 15
print(f"\n{n} contains prime factor(s):\n")

i = 1

while i <= n:                               # i is assigned 3     i(3) <= n(15), which is True
    print("\n========")
    k = 0                                   # k is assigned 0

    if n % i == 0:                          # n(15) is divisible by i(3), which is True
                                            # i(3) is a factor of n(15), but we have to check if i(3) is prime.
        j = 1                               # j is assigned 1

        while j <= i:                       # j(1) <= i(3), which is True  --> Check if j[1, 3] is a factor of i(1)
            print(f"j({j}) <= i({i})")
            if i % j == 0:                  # i(3) is divisible by j(3), which is True  -->
                                            # (Only when i is prime can i be divisible by j only twice.
                                            # The first time is when j equals 1 and the second time is when j equals i
                                            # i, as a prime, is evenly divided by 1, then k = 0 + 1 = 1
                                            # i, as a prime, is evenly divided by itself, then k = 1 + 1 = 2
                                            # when j is assigned i + 1, exit the while loop. Since k = 2 (meaning i is a
                                            # prime factor of n), print out 'i'. Remarkable!
                k = k + 1                   # k = 1 + 1 = 2
                print(f"k = {k - 1} + 1 = {k}")
            j = j + 1                       # j = 1 + 1 = 2
            print(f"j = {j - 1} + 1 = {j}")
        if k == 2:  # 'if k == 2' is another way to say, 'if i is a prime number', since only prime numbers have just
            # two chances to make the 'i % j == 0' condition evaluates to True and then reassign 'k' twice - first k = 1
            # and second k = 2
            print(f"prime factor: {i}")
    i = i + 1                               # i = i(2) + 1 = 3
# (Whatever the above block of code is executed or not, 'i' will be updated
# by adding 1 to become i + 1 at the bottom of the body of the outer while
# loop. Adding 1 to 'i' keeps incrementing the value of 'i' so that each
# number in the range from 1 (included) up to 'n' (included) can be taken
# until the condition of the outer while loop evaluates to False.

# Problem Solution
# 1. Take the value of the integer and store in a variable.
# 2. Using a while loop, first obtain the factors of the number.
# 3. Using another while loop within the previous one, compute if the factors are prime or not.
# 4. Exit.

# Program Explanation
# 1. User must first enter the value and store it in a variable.
# 2. The while loop is used and the factors of the integer are computed by using the modulus operator
#    and checking if the remainder of the number divided by i is 0.
# 3. Then the factors of the integer are then again checked if the factor is prime or not.
# 4. If the factor of the integer has two factors, the factor is prime.
# 5. The prime factor of the integer is printed.
