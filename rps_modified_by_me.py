# Program of 'Rock! Paper! Scissors!' based off of the version downloaded from 'The Hello World Program'.

from random import randint

# Create a list of play options made by the computer player.
play_options = ["rock", "paper", "scissors"]
# There are three possible play options that you and the computer can make on each turn rock, paper and scissors.

# Let the 'computer' player access its play, using the random.randint(a, b) function and index.
# i = randint(0, 2)
# p1 = plays[i]  # For convenience, we call the computer player 'p1' and the human player 'p2'.
# Once 'i' gets a value from the above random.randint(a, b) function, the value 'i' contains never change.

# To keep the game on and on and on until the players want to stop playing, we need to use the while loop and a special
# counter - boolean value.

# Initialize 'p2'(the human player) - assign 'False' to 'p2'.
p2 = False  # Why 'False'? (Actually 'True' is okay, either.) Once the while loop starts, the computer will patiently
# wait for you to make your play. As soon as you take your turn, your status changes from 'False' to 'True' because any
# value assigned to the variable 'p2' makes 'p2' True.


n = 1
while p2 == False and n > 0:  # while the human play equals 'False', go execute the body of while,
    # otherwise the program control will exit the while loop.
    print(f"\nRock! Paper! Scissors! Round {n}")

    # 'p1'(the computer player) has to make a play option at the very beginning or the end of each iteration
    # for each round.
    p1 = play_options[randint(0, 2)]  # We assign a random play to 'p1'(the computer player), using the list of play
    # options created before and the random.randint function. Why (0, 2)? Because the computer starts counting at 0,
    # rather than 1. The "rock" item in the list 'play_options' is in the 0 position/index, the "paper" item is in the 1
    # position/index, and so on.

    # 'p2'(the human player) makes a play option for which we ask the user. We use the input() function to pass the new
    # value to the variable 'p2'. By the way, once you assign a value (any non-empty value including whitespace
    # characters) to the variable 'p2', the boolean value it contains changes from 'False' to 'True'. Your input will
    # determine which statement will be triggered later.
    p2 = input("I play: ")

    if p2 == "rock" or p2 == "paper" or p2 == "scissors":
        # In the 'if...elif...else' statements, we're gonna program based off of the final results,
        # which are 'tie/draw', 'p1 wins' or 'p2 wins'. And the last results can be put into the final 'else' part.

        # Scenario 1: tie/draw
        if p1 == p2:
            print(f"Tie! You and computer both played {p1}.")

        # Scenario 2: p1(computer) wins
        # This scenario has a multiple of sub-scenarios based off of what p1 plays.
        elif p1 == "rock" and p2 == "scissors":
            print(f"Computer won! Computer played {p1}. You played {p2}. Rock crushes scissors.")
        elif p1 == "paper" and p2 == "rock":
            print(f"Computer won! Computer played {p1}. You played {p2}. Paper covers rock.")
        elif p1 == "scissors" and p2 == "paper":
            print(f"Computer won! Computer played {p1}. You played {p2}. Scissors cut paper.")

        # Scenario 3: p2(human) wins
        # In addition to the scenario of 'p2 wins', all other possible scenarios have been taken into account,
        # or you can say, have been exhausted. So the leftover scenarios, no matter what sub-scenarios the 'Scenario 3'
        # has, can be put into a single 'else' container collectively.
        else:
            print(f"You won! You played {p2}. Computer played {p1}. ")
        n += 1  # Only the round with valid play option is counted as a formal round. So we put the 'counter increment'
        # inside the nested 'if...elif...else' statements.
    else:
        print("Sorry, that's an invalid play! Must enter a play and check your spelling. Only \"rock\", \"paper\" and "
              "\"scissors\" are allowed.")

    # To restart the game automatically, we need to reassign 'False' to 'p2'
    # in order to make the condition 'p2 == False' evaluate to 'True'.
    p2 = False  # Notice that here we use the = (single-equal or assignment) operator, instead of using the == (double-
    # equal or comparison) operator, since we just want to assign a (boolean) value to 'p2'.


