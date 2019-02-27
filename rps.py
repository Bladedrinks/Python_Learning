# Program downloaded from 'The Hello World Program' with my comment on it. The link is:
# (https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/)

from random import randint

# create a list of play options
t = ["Rock", "Paper", "Scissors"]  # As a list name, 't' is too short. To avoid confusing the reader of code, I think
# we'd use a longer variable name, like 'choices" or "plays".

# assign a random play to the computer
computer = t[randint(0, 2)]
# random.randint(a, b) is a function which belongs to the 'random' module. This function returns a random integer N such
# that a <= N <= b. So in this case, randint(0, 2) returns a random integer which would be either 0 or 1 or 2 each time.
# 't[randint(0, 2)]' returns values with indices from 0 to 2 in the list 't'. 'randint(0, 2)' returns one number at a
# time, which could be 0 or 1 or 2. Numbers 0, 1 or 2 are exactly the indices of items in the list 't'.
# Let's say, we got a number of 1 from the random.randint(a, b) function, then the right side of the = (assignment)
# operator is t[1]. Inside the square brackets is '1'. We use 't[1]' to slice along with index to obtain the specific
# value (which, in this case, is 'paper'). Now that we have obtained a value of 'paper', we then assign it to the
# variable 'computer'. That is the play/choice that the 'computer' player make.
# About how to access values in a list, see:
# https://www.tutorialspoint.com/python/python_lists.htm

# set player to False (After my inspection and retry with 'True', I found that setting player to 'True' works too!)
player = False

while player == False:

    # set player to True
    player = input("Rock, Paper, Scissors?")  # I don't like this input prompt, since it should be an imperative
    # sentence like "Enter your play/choice: "
    if player == computer:
        print("Tie!")  # Bad hard code. The user must be wondering why tie?! What's the play of 'computer' player?
        # So the output in this 'tie' scenario should be: print(f"Tie! You and Computer both plays {computer}.")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)  # Paper covers rock.
        else:   # computer == "scissors"
            print("You win!", player, "smashes", computer)  # Rock smashes scissors.
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)  # Scissors cut paper.
        else:  # computer == "rock"
            print("You win!", player, "covers", computer)  # Paper covers rock.
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)  # Rock smashes paper.
        else:  # computer == "paper"
            print("You win!", player, "cut", computer)  # scissors cut paper.
    else:
        print("That's not a valid play. Check your spelling!")
    # As long as the variable contains values (in other words, is not an empty sequence/string), player was set to True,
    # but we want it to be False so the loop continues, since the condition of while is 'player == False'.

    player = False
    computer = t[randint(0, 2)]
