# This is a game program named 'Rock! Paper! Scissors!'
#
# Compared to the first version of this program (rps_modified_by_me_v1), this version offers the user a way to quit the
# game by answering a question raised by the computer right after each round of the game.
#
# Logically, in this rps game, we need to two players: one is a human player and the other is a computer player.
# Initialize the variable for the computer player by using the random.randint(a, b) method and accessing the three play
# options based off of their indices.
# 'i' is short for 'index'


from random import randint  # import the 'random' module, otherwise the random.randint(a, b) method will be viewed as
# "undefined" by the Python Interpreter.


def stay_or_quit():
    """
    (1) Return 'n' if the 'decision' variable is assigned 'n'.
    (2) Display nothing and the control of the program goes to the first statement after this UDF
        if the 'decision' variable is assigned 'y';
    (3) Keep displaying "User Tip: only 'y' and 'n' are valid inputs" and "Do you want to keep playing? (y/n)"
        if the 'decision' variable is not assigned either 'y' or 'n'.
    """
    decision = input("Do you want to keep playing? (y/n)  ")
    while not (decision == "y" or decision == "n"):
        decision = input("\n      * * * User Tip: only 'y' and 'n' are valid inputs. * * *\n"
                         "\nDo you want to keep playing? (y/n)  ")
    if decision == "n":
        return "n"


winning_score = int(input("Set the winning score before playing: "))
r = 1  # The number of sub-Rounds of each 'Triple Round'
tri_r = 1  # The number of Triple Rounds
computer_wins = 0  # The number of victories of 'p1'(the computer player) in each 'Triple Round'
human_wins = 0  # The number of victories of 'p2'(the human player) in each 'Triple Round'
while True:
    print(f"\n         Computer {computer_wins} : {human_wins} You")
    # The first player whose number of victories accumulates to 2 in a single 'Triple Round' wins the 'Triple Round'.
    if computer_wins == winning_score:
        print(f"\n\U0001F62D Computer won Triple Round {tri_r} \U0001F62D \n")
        if stay_or_quit() == "n":
            print("\nThanks for playing. Bye!")
            break
        tri_r += 1
    elif human_wins == winning_score:
        print(f"\n\U0001F389 You won Triple Round {tri_r} \U0001F389 \n")
        if stay_or_quit() == "n":
            print("\nThanks for playing. Bye!")
            break
        tri_r += 1

    # As soon as one of the two players wins (the number of victories reaches 2),
    # the numbers of victories of the computer and human players are reassigned 0 and the number of sub-rounds of each
    # 'Triple Round' is also reassigned 1 in preparation for the next Triple Round and its sub-rounds.
    if computer_wins == winning_score or human_wins == winning_score:
        computer_wins = 0
        human_wins = 0
        r = 1

    print(f"\n\n\n     ------ Triple Round {tri_r} ({r}) ------")

    # Initialize the variable for the human player bt asking the user for their input:
    human = input("\n     You play: ")

    # Initialize the variable for the computer player bt using the random.randint() method.
    plays = ["rock", "paper", "scissors"]
    i = randint(0, 2)
    computer = plays[i]
    print(f"Computer play: {computer}")

    # The human player plays one of the three valid options:
    if human == "rock" or human == "paper" or human == "scissors":

        # (1) Tie/Draw (p1 == p2);
        if computer == human:
            print(f"\nTie!")

        # (2) The computer player wins ("Rock crushes scissors", "Paper covers rock" or "Scissors cut paper")
        elif computer == "rock" and human == "scissors":
            print(f"\nComputer won!")
            computer_wins += 1
        elif computer == "paper" and human == "rock":
            print(f"\nComputer won!")
            computer_wins += 1
        elif computer == "scissors" and human == "paper":
            print(f"\nComputer won!")
            computer_wins += 1

        # (3) The human player wins ("Rock crushes scissors", "Paper covers rock" or "Scissors cut paper")
        else:
            print("\nYou won!")
            human_wins += 1

        r += 1  # The number of 'Round' is incremented by 1 right after the human player enters a valid input (notice:
        # only 'rock', 'paper' and 'scissors' are valid input) each time. Since invalid input doesn't make a new round,
        # we have to put the counter increment statement 'r += 1' under the 'if' part, instead of putting it under
        # the 'else' part.

    # The human player plays gibberish (including nothing):
    else:
        print("\n      * * * User Tip: Only 'rock', 'paper' and 'scissors' are valid plays. * * * ")
