# This is a game program named 'Rock! Paper! Scissors!'(abbreviated to 'RPS')
#
# Compared to the first version of this program (rps_modified_by_me_v1), this version offers the user a way to quit the
# game by answering a question raised by the computer right after each round of the game.
#
# Logically, in this RPS game, we need at least two players: one is a human player and the other is a computer player.


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


# Set the 'Play Mode' before playing. The user has two choices: 'Person vs Person' and 'Person vs Computer'
p2_id = input("Play Mode: 'Person vs Person' or 'Person vs Computer'? (p/c)  ")
while not(p2_id == "p" or p2_id == "c"):  # p2_id != "p" and p2_id != "c"
    p2_id = input("\n      * * * User Tip: only 'p' and 'c' are valid inputs. * * *\n"
                  "\nPlay Mode: 'Person vs Person' or 'Person vs Computer'? (p/c)  ")
if p2_id == "p":
    p1_name = input("\nHuman player 1, enter your name: ")
    p2_name = input("\nHuman player 2, enter your name: ")
else:  # p2_id == "c":
    p1_name = input("\nHuman player, enter your name: ")
    p2_name = "Computer"



# The game rule should be set before playing.
# The game rule is basically the common 'best of n' or 'best of n sets' - whoever is first to win half of (n + 1) sets
# wins the whole round (by the way, you can play as many rounds as you want. The number of rounds is unrestricted).
# For example, if the user want to play 'best of three', he/she should type '3' at the very beginning
# and whoever is first to win 2 sets (half of 3 + 1 is 2) wins the whole round/game.
# (Therefore, the 'winning score' is 2, since (3 + 1) / 2 = 2.)
# If the user want to play 'best of five', he/she should type '5' at the very beginning
# and whoever is first to win 3 sets (half of 5 + 1 is 3) wins the whole round/game.
# (Therefore, the 'winning score' is 3, since (5 + 1) / 2 = 3.)
n = int(input("\nSet the number 'n' in 'best of n' before playing: "))  # Say, n = 5, meaning the user wants to play 'best
# of five'.
while n % 2 == 0 or n < 0:
    n = int(input("\n      * * * User Tip: Only odd positive number is valid input. * * *\n"
                  "\nSet the number 'n' in 'best of n' before playing: "))
winning_score = (n + 1) / 2  # If n = 5, then 'winning score' is 3, since (5 + 1) / 2 = 3. Whoever is first to win three
# sets wins the whole round.

set = 1  # The number of sets of each round.
round = 1  # The number of rounds.
p1_wins = 0  # The number of victories 'p2'(the human player) in each round gets.
p2_wins = 0  # The number of victories 'p1'(the computer player) in each 'Triple Round'

while True:
    print(f"\n         {p1_name} {p1_wins} : {p2_wins} {p2_name}")
    # The first player whose number of victories accumulates to 2 in a single 'Triple Round' wins the 'Triple Round'.
    if p1_wins == winning_score:
        print(f"\n      \U0001F44D {p1_name} won Round {round} \U0001F44D \n")  # U0001F44D is for 'Thumbs Up' 👍
        if stay_or_quit() == "n":
            print("\n   \U0001F44B Thanks for playing. Bye! \U0001F44B")  # U0001F44B is for 'Goodbye'👋
            break
        round += 1
    elif p2_wins == winning_score:
        print(f"\n       \U0001F389 {p2_name} won Round {round} \U0001F389 \n")  # U0001F389 is for 'Celebration' 🎉
        if stay_or_quit() == "n":
            print("\nThanks for playing. Bye!")
            break
        round += 1

    # As soon as one of the two players wins (the number of victories reaches 2),
    # the numbers of victories of the computer and human players are reassigned 0 and the number of sub-rounds of each
    # 'Triple Round' is also reassigned 1 in preparation for the next Triple Round and its sub-rounds.
    if p2_wins == winning_score or p1_wins == winning_score:
        p2_wins = 0
        p1_wins = 0
        set = 1

    print(f"\n\n\n     ------ Round {round} (Set {set}) ------")

    # Initialize the variable for the human player bt asking the user for their input:
    p1_play = input(f"\n* * * User Tip: Type 'quit' or 'q' to quit the game. * * * \n{p1_name} plays: ")
    if p1_play == "quit" or p1_play == "q":
        print("\n   \U0001F44B Thanks for playing. Bye! \U0001F44B")
        break

    if p2_id == "p":
        p2_play = input(f"\n* * * User Tip: Type 'quit' or 'q' to quit the game. * * * \n{p2_name} plays: ")
        if p2_play == "quit" or p2_play == "q":
            print("\n   \U0001F44B Thanks for playing. Bye! \U0001F44B")
            break
    else:  # elif p2_id == "c"  (when the user chooses the 'Person vs Computer' play mode)
        # Create a list which contains three play options - 'rock', 'paper' and 'scissors'.
        plays = ["rock", "paper", "scissors"]
        # Yield a random integer using the random.randint(a, b) function in order to help us access certain item
        i = randint(0, 2)
        p2_play = plays[i]
        print(f"{p2_name} plays: {p2_play}")

    # Any human player plays one of the three valid options:
    if (p1_play == "rock" or p1_play == "paper" or p1_play == "scissors") \
            and (p2_play == "rock" or p2_play == "paper" or p2_play == "scissors"):

        # (1) Tie/Draw (p1 == p2);
        if p2_play == p1_play:
            print(f"\nTie!")

        # (2) Player 2 wins ("Rock crushes scissors", "Paper covers rock" or "Scissors cut paper")
        elif p2_play == "rock" and p1_play == "scissors":
            print(f"\n{p2_name} won this set!")
            p2_wins += 1
        elif p2_play == "paper" and p1_play == "rock":
            print(f"\n{p2_name} won this set!")
            p2_wins += 1
        elif p2_play == "scissors" and p1_play == "paper":
            print(f"\n{p2_name} won this set!")
            p2_wins += 1

        # (3) Player 1 wins ("Rock crushes scissors", "Paper covers rock" or "Scissors cut paper")
        else:
            print(f"\n{p1_name} won this set!")
            p1_wins += 1

        set += 1  # The number of 'Round' is incremented by 1 right after the human player enters a valid input (notice:
        # only 'rock', 'paper' and 'scissors' are valid input) each time. Since invalid input doesn't make a new round,
        # we have to put the counter increment statement 'r += 1' under the 'if' part, instead of putting it under
        # the 'else' part.

    # When human player plays gibberish (including nothing entered):
    else:
        print("\n* * * User Tip: Only 'rock', 'paper' and 'scissors' are valid plays. Check your spelling. * * * ")
