# Program for prime factorization,
# which only print each prime factor one time even if it occurs more than one time.

# ========== Test ==========
# n = 3 x 5 = 15

n = int(input("Enter an integer: "))  # n = 15
print(f"\n{n} contains prime factor(s):\n")

i = 1

while i <= n:                               # i is assigned 3     i(3) <= n(15), which is True
    print("\n========")
    k = 0                                   # k is assigned 0     The statement 'k = 0' is put there to update k to be 0
                                            # again, since k has been reassigned different value in the below nested
                                            # while loop
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




# Detailed explanation:


# The first layer of the program and also part of the program to generate all integers from 1 (included) up to the given
# number itself (included).
n = int(input("Enter your number: "))
i = 1  # Initialize the assistant variable 'i'.
while i <= n:  # i = 1, 2, 3, ..., n - 2, n - 1, n
    # k = 0
    if n % i == 0:  # Tests if 'i' is a factor of 'n'. If 'n' is divisible by 'i', then execute the body of if.
    #     j = 1
    #     while j <= i:
    #         if i % j == 0:
    #             k = k + 1
    #         j = j + 1
    #     if k == 2:
    #         print(f"prime factor: {i}")
    i = i + 1  # Keeps the while loop continue until i becomes greater than n
# Notice that this function in the outer layer doesn't use for loop, but a while loop. And the variable 'i' is
# initialized to be 1 (which is a factor for both prime and composite) and the final value it takes is the value of 'n'
# itself, meaning i takes values from 1 to the given number itself. So we can't check the given number is prime or not
# based off of this part of the program since both prime and composite can be evenly divided by 1 and itself.
#
# The above layer of the program can be rewritten as a user-defined function like this:
def factors(n):
    """Print all factor(s) of a given positive number one at a time including 1 and the number itself;
    print nothing if the given number is non-positive."""
    f = 1
    while f <= n:
        if n % f == 0:
            print(f)
        f = f + 1
# End of the UDF definition.




# The nested while loop and the nested if statement.
# ...
# ...
    k = 0
#   ...
        j = 1
        while j <= i:
            if i % j == 0:
                k = k + 1
            j = j + 1
        if k == 2:  # 'if k == 2' is another way to say, 'if i is a prime number', since only prime numbers have just
            # two chances to make the 'i % j == 0' condition evaluates to True and then reassign 'k' twice - first k = 1
            # and second k = 2
            print(f"prime factor: {i}")
#
# The above inner part of the program is a relatively independent module which is used to check if each factor of
# the given 'n' (mentioned above) is prime or not. If it is prime, then print it out.
# The algorithm it is based off of can be used to define a function to check if a given number is prime or not.
# Below is the UDF (user-defined function) that I write based on the algorithm:

# UDF to check if a given number is prime or not and/or print all factors of a given number.
def is_prime(i):
    """Return 'True' if 'i' is prime; 'False' otherwise."""
    # 'i' stands for the given number for which you might ask the user.
    d = 1  # Initialize the divisor 'd'. Without the assignment of 'd', the Python Interpreter is gonna be freak out and
    # throw us an error, since you reference a (local) variable before assigning it an initial value.
    c = 0  # Initialize the counter 'c' for the sake of helping us record how many times 'i' is evenly divided by 'd'.
    # Why c is initially assigned 0? Why not 1? 2? ... Because counting the number of times when 'i' is evenly divided
    # by 'd' must start at 1. 'c = 0' can help the 'c = c + 1' statement initially assign 1 (= 0 + 1) to 'c'.
    while d <= i:
        if i % d == 0:
            c = c + 1
        d += 1  # Also written as d = d + 1
    if c == 2:  # The value of 'c' stands for how many times 'i' is evenly divided by numbers from 1 to 'i' itself.
        return "is prime"
    return "is not prime"
    # The three lines of code right above can be replace with the following four lines of code to print out 'i' is prime
    # or not prime:
    # if c == 2:  # The value of 'c' stands for how many times 'i' is evenly divided by numbers from 1 to 'i' itself
    #     print(f"{i} is prime")
    # else:
    #     print(f"{i} is not prime")

# Below is the second UDF that I write based on the algorithm:
# UDF to check if a given number is prime or not and/or print all factors of a given number.
def composite_check(x):
    # Take each value from 1 to 'x' itself to divide 'x' to see if it can evenly divide 'x'.
    f = 1
    k = 0
    while f <= x:
        if x % f == 0:
            k = k + 1  # 'k' tells us the number of times when 'x' is evenly divided by 'f'.
            # If 'x' is negative, f(1) is never less than or equal to a negative number, so the body of while loop will
            # never be executed and the value of 'k', 0, will never change.
            # If 'x' is 0, f(1) is also never less than or equal to 0, so the body of while loop will never be executed
            # and the value of 'k', 0, will never change.
            # If 'x' is 1, f(1) is less than or equal to 1, so the body of while loop can be executed but only once and
            # the value of 'k' will change to be 1, since 'f' as in 'f = f + 1' will be updated to be 2 (= 1 + 1).
            # 2 is not less than or equal to x(1).
            # If 'x' is greater than 1 and can be evenly divided by 'f' only twice, then we are 100% sure that 'x' is a
            # prime number since prime numbers can only be evenly divided by 1 and themselves. And the value of 'k' will
            # updated to be 2, finally.
            # If 'x' is greater than 1 and can be evenly divided by 'f' more than twice, then we are sure that 'x' is a
            # composite number, since composite numbers can be evenly divided by at least one smaller number other than
            # 1 and themselves. And the value of 'k' will be updated to be 3 or more, finally.
            #
            #                                      Variable      'x'     'k'
            #                                                 negative    0
            #                                                     0       0
            #                                                     1       1
            #                                                   prime     2
            #                                                composite   >2
        f = f + 1
    # if k > 2:
    #     return f"{x} is composite"
    # if k == 2:
    #     return f"{x} is prime"
    # if k == 1:
    #     return f"{x} is 1"
    # if k == 0:
    #     return f"{x} is 0 or negative"
    if k > 2:
        print("composite")
    if k == 2:
        print("prime")
    if k == 1:
        print("is not both composite and prime!")
    if k == 0:
        print("is not both composite and prime")


# ====== Test Function ======
for num in range(-10, 31):
    print(f"\n{num} is: ")
    composite_check(num)
