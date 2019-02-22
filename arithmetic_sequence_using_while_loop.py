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
counter = 1  # Set 'counter' to 1.
while counter <= n:  # Enter a while loop that keeps repeating while 'counter' is less than or equal to 'n'.
    ari_seq.append(a)  # Each time the body of the while loop repeats, add a new term to the list 'ari_seq'.
    a = a + d  # Each time the body of the while loop repeats, add 'd', the common difference, to 'a', the previous term
    # , and assign the sum of the previous term and the common difference to 'a', which will be printed out to the
    # screen in the next time.
    counter = counter + 1  # Increment 'counter' by 1 so that some moment in the near future the condition of the while
    # loop will be evaluating to False and we can exit the while loop, otherwise the loop will go on forever.
print(f"Your arithmetic sequence is: {ari_seq}")
