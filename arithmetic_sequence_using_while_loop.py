# The while loop, unlike the if statement, will carry out the instructions over and over again if the condition is True.
# So the while loop need to have something that changes each time it runs - otherwise it will run forever.
# That's why the while loops are often used with a counter.

# Program to produce an arithmetic sequence with the first term, the common difference and the number of terms that are
# given by the user.
# Ask the user for the first term:
a = int(input("Enter your first term: "))
d = int(input("Enter the common difference: "))
n = int(input("Enter the number of terms: "))
ari_seq = []
counter = 1
while counter <= n:
    ari_seq.append(a)
    a = a + d
    counter = counter + 1
print(f"Your arithmetic sequence is: {ari_seq}")
