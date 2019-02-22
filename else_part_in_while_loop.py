# Program to show when the 'else' part in a while loop works.

counter = 1
while counter < 10:
    if counter == 10:
        break
    print(counter)
    counter = counter + 1  # When 'counter' on the right-hand side of the assignment operator equals 4, the 'counter' on
    # the left-hand side is set to 5.
else:  # The 'else' part in the while is similar to using the 'else" part with the if statement. It specifies what to do
    # when the condition of the while loop evaluates to False.
    # Now the question is when the condition evaluates to False. Let's take the 'counter < 10' expression as an example.
    # The initial value of 'counter' is set to 1. 'counter(1) < 10' is True, 'counter(2) < 10' is True, ...,
    # 'counter(9) < 10' is True, but when the 'counter' is assigned a value of 10, 'counter < 10' evaluates to False.
    # Right now, we can see that "evaluating to False" means the 'counter' takes all the possible values that can make
    # the test_expression True. But some people might say, "Huh, you forgot one scenario, which is the break statement.
    # Yes, but when the 'break' statement is executed, the test_expression is still True, so the 'else' part would not
    # be executed, either! In other words, if and only if the possible values of 'counter' exhaust, the 'else' part will
    # be executed.
    print("cool")
