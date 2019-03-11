# This is a mini game program named 'Rock! Paper! Scissors!'(abbreviated to 'RPS')
#
# Compared to the first version of this program (rps_modified_by_me_v1), this version has several quirks different from
# the first version:
#
# (1) It offers the user two play modes: 'Person vs Person' and 'Person vs Computer'.
#
# (2) It offers the user a way to quit the game by answering a question raised by the computer right after each set of a
# single round or each round of the game.
#
# (3) The human players can enter their name before playing.
#
# (4) The game rule can be set by the user before playing by setting the number 'n' in 'best of n'. 'Best of 3' means
# whoever is first to win 2 sets of a single round wins the round (By the way, how many rounds you'd like to play
# depends on the users). 'Best of 5' means whoever is first to win 3 sets of a single round wins the round. The numbers
# '2' in 'best of 3' and '3' in 'best of 5' are called the 'winning score' which is calculated by the formula:
#
#                                     x = (n + 1) / 2
#
# x stands for the winning score.


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
    while len(p1_name) > 10:
        p1_name = input("\n      * * * User Tip: User name can only contain at most 10 characters. * * *\n"
                        "\nHuman player 1, enter your name: ")
    p2_name = input("\nHuman player 2, enter your name: ")
    while len(p2_name) > 10:
        p2_name = input("\n      * * * User Tip: User name can only contain at most 10 characters. * * *\n"
                        "\nHuman player 2, enter your name: ")
else:  # p2_id == "c":
    p1_name = input("\nHuman player, enter your name: ")
    while len(p1_name) > 10:
        p1_name = input("\n      * * * User Tip: User name can only contain at most 10 characters. * * *\n"
                        "\nHuman player, enter your name: ")
    p2_name = "Computer"

# The game rule should be set before playing.
# The game rule is basically the common 'best of n' or 'best of n sets' - whoever is first to win half of (n + 1) sets
# wins the whole round (by the way, you can play as many rounds as you want. The number of rounds is unrestricted).
# For example, if the user wants to play 'best of three', he/she should type '3' at the very beginning
# and whoever is first to win 2 sets (half of 3 + 1 is 2) wins the whole round/game.
# (Therefore, the 'winning score' is 2, since (3 + 1) / 2 = 2.)
# If the user want to play 'best of five', he/she should type '5' at the very beginning
# and whoever is first to win 3 sets (half of 5 + 1 is 3) wins the whole round/game.
# (Therefore, the 'winning score' is 3, since (5 + 1) / 2 = 3.)
n = int(input("\nSet the number 'n' in 'best of n' before playing: "))  # Say, n = 5, meaning the user wants to play
# 'best of five'.
while n % 2 == 0 or n < 0:
    n = int(input("\n      * * * User Tip: Only odd positive number is valid input. * * *\n"
                  "\nSet the number 'n' in 'best of n' before playing: "))
winning_score = (n + 1) / 2  # If n = 5, then 'winning score' is 3, since (5 + 1) / 2 = 3. Whoever is first to win three
# sets wins the whole round.

set = 1  # The number of sets of each round.
round = 1  # The number of rounds.
p1_wins = 0  # The number of victories which Player 1 in each round gets.
p2_wins = 0  # The number of victories which Player 2 in each round gets'

while True:  # Since the number of rounds is unrestricted, we can keep playing the game as many rounds as we want until
    # we decide to quit by typing 'quit' or 'q' and break out of the while loop.
    print(f"\n         {p1_name} {p1_wins} : {p2_wins} {p2_name}")
    # Whoever is first to reach the 'winning score' in a single round wins the round.
    if p1_wins == winning_score:  # 'p1_wins' must go from 0 wins to the 'winning score' to win a single round.
        print(f"\n      \U0001F44D {p1_name} won Round {round} \U0001F44D \n")  # U0001F44D is for 'Thumbs Up' 👍
        if stay_or_quit() == "n":  # 'stay_or_quit()' is a UDF which has been defined before.
            print("\n   \U0001F44B Thanks for playing. Bye! \U0001F44B")  # U0001F44B is for 'Goodbye'👋
            break
        round += 1  # The ordinal number of 'round' is incremented by 1 only when either of the two players wins the
        # previous round.
    elif p2_wins == winning_score:  # 'p2_wins' must go from 0 wins to the 'winning score' to win a single round.
        print(f"\n       \U0001F389 {p2_name} won Round {round} \U0001F389 \n")  # U0001F389 is for 'Celebration' 🎉
        if stay_or_quit() == "n":
            print("\n   \U0001F44B Thanks for playing. Bye! \U0001F44B")  # U0001F44B is for 'Goodbye'👋
            break
        round += 1  # The ordinal number of 'round' is incremented by 1 only when either of the two players wins the
        # previous round.

    # As soon as either of the two players wins a single round, the numbers of victories of the two players are all
    # reset equal to 0 and the number of sets of each round is also reset equal to 1 in preparation for the counting
    # thing with the next round and its sets.
    if p2_wins == winning_score or p1_wins == winning_score:
        p2_wins = 0
        p1_wins = 0
        set = 1

    # Show which round and set the game reaches.
    print(f"\n\n\n     ------ Round {round} (Set {set}) ------")

    # For a better typographical appearance, add whitespace characters to the beginning of the player's name whose
    # length is longer so that the ':' mark can be aligned.
    if len(p1_name) > len(p2_name):
        p2_name_temp = " " * (len(p1_name) - len(p2_name)) + p2_name
        p1_name_temp = p1_name
    else:  # len(p2_name) >= len(p1_name)
        p1_name_temp = " " * (len(p2_name) - len(p1_name)) + p1_name
        p2_name_temp = p2_name

    # Initialize Player 1's play/option:
    p1_play = input(f"\n* * * User Tip: Type 'quit' or 'q' to quit the game. * * * \n{p1_name_temp} plays: ")
    if p1_play == "quit" or p1_play == "q":
        print("\n   \U0001F44B Thanks for playing. Bye! \U0001F44B")
        break
    # Initialize Player 2's play/option (Since Player 2 can be another human player or the computer player,
    # the initialization is more complicated than Player 1):
    if p2_id == "p":  # if Player 2 is a person: (when the user chooses the 'Person vs Person' play mode)
        print("\n\n       ! ! ! No Cheating ! ! !\n" * 10, end="")
        p2_play = input(f"\n* * * User Tip: Type 'quit' or 'q' to quit the game. * * * \n{p2_name_temp} plays: ")
        if p2_play == "quit" or p2_play == "q":
            print("\n   \U0001F44B Thanks for playing. Bye! \U0001F44B")
            break
    else:  # elif p2_id == "c"  (when the user chooses the 'Person vs Computer' play mode)
        # Create a list which contains three play options - 'rock', 'paper' and 'scissors'.
        plays = ["rock", "paper", "scissors"]
        # Yield a random integer using the random.randint(a, b) function in order to help us access certain item
        i = randint(0, 2)
        p2_play = plays[i]
        print(f"{p2_name_temp} plays: {p2_play}")

    # Below is the conditional logic part:
    # The first statement right below is to check if the input (play options) is valid or not.
    # If Player 1 plays one of the three valid plays and, at the same time, Player 2 (under the 'Person vs Person' play
    # mode) plays one of the three valid plays, we go and check the rest of the conditional part; if not, the 'User Tip'
    # part is triggered.
    if (p1_play == "rock" or p1_play == "paper" or p1_play == "scissors") \
            and (p2_play == "rock" or p2_play == "paper" or p2_play == "scissors"):

        # Scenario 1: Tie/Draw (p1 == p2);
        if p2_play == p1_play:
            print(f"\nTie!")

        # Scenario 2: Player 2 wins ("Rock crushes scissors", "Paper covers rock" or "Scissors cut paper")
        elif p2_play == "rock" and p1_play == "scissors":
            print(f"\n{p2_name} won this set!")
            p2_wins += 1
        elif p2_play == "paper" and p1_play == "rock":
            print(f"\n{p2_name} won this set!")
            p2_wins += 1
        elif p2_play == "scissors" and p1_play == "paper":
            print(f"\n{p2_name} won this set!")
            p2_wins += 1

        # Scenario 3: Player 1 wins ("Rock crushes scissors", "Paper covers rock" or "Scissors cut paper")
        else:
            print(f"\n{p1_name} won this set!")
            p1_wins += 1

        set += 1  # 'set' (the number of sets) is incremented by 1 right after the two players enter the valid inputs
        # (notice: only 'rock', 'paper' and 'scissors' are valid input) each time. Since invalid input doesn't make a
        # new round, we have to put the counter increment statement 'set += 1' under the 'if' part, instead of putting
        # it under the 'else' part.

    # When either of the human players plays gibberish (including nothing entered), the control of the program goes here
    else:
        print("\n* * * User Tip: Only 'rock', 'paper' and 'scissors' are valid plays. Check your spelling. * * * ")
