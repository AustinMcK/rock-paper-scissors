import random


user = 0            # user score
user_rock = 0       # user rock count
user_paper = 0      # user paper count
user_scissors = 0   # user scissor count
comp = 0            # computer score
comp_rock = 0       # computer rock count
comp_paper = 0      # computer paper count
comp_scissors = 0   # computer scissor count


moves = ["rock", "paper", "scissors", "Rock", "Paper", "Scissors"]  # I do this to allow case insensitivity
moves_pref = [0, 1, 2, 3, 4, 5]                                     # This reflects the moves\options the user has
moves_comp = [0, 1, 2]


def play():
    global user
    global comp
    global user_rock
    global user_paper
    global user_scissors
    global comp_rock
    global comp_paper
    global comp_scissors

    print("Welcome to Rock, Paper, Scissors!\nThe first of many pieces by Austin M.\n")   # Home screen
    user_move = input("Rock, Paper, or Scissors? ")
    try:
        user_move = moves_pref[moves.index(user_move)]
        comp_move = random.choice(moves_comp)
    except ValueError:
        print("Please type only rock, paper, or scissors.")
        return 1

    print("Computer Player: ", moves[comp_move])
    if comp_move == 0:
        comp_rock += 1
    if comp_move == 1:
        comp_paper += 1
    if comp_move == 2:
        comp_scissors += 1
    if user_move == 0:
        user_rock += 1
    if user_move == 3:
        user_rock += 1
    if user_move == 1:
        user_paper += 1
    if user_move == 4:
        user_paper += 1
    if user_move == 2:
        user_scissors += 1
    if user_move == 5:
        user_scissors += 1
    if user_move == comp_move:
        print("That's a tie!")
    if user_move == 3 and comp_move == 0:
        print("That's a Tie!")
    if user_move == 4 and comp_move == 1:
        print("That's a Tie!")
    if user_move == 5 and comp_move == 2:
        print("That's a Tie!")
    elif user_move == 0 and comp_move == 2:
        user += 1
        print("You win!")
    elif user_move == 3 and comp_move == 2:
        user += 1
        print("You win!")
    elif user_move == 1 and comp_move == 0:
        user += 1
        print("You win!")
    elif user_move == 4 and comp_move == 0:
        user += 1
        print("You win!")
    elif user_move == 2 and comp_move == 1:
        user += 1
        print("You win!")
    elif user_move == 5 and comp_move == 1:
        user += 1
        print("You win!")
    elif comp_move == 0 and user_move == 2:
        comp += 1
        print("Aw the computer wins this one!")
    elif comp_move == 0 and user_move == 5:
        comp += 1
        print("Aw the computer wins this one!")
    elif comp_move == 1 and user_move == 0:
        comp += 1
        print("Aw the computer wins this one!")
    elif comp_move == 1 and user_move == 3:
        comp += 1
        print("Aw the computer wins this one!")
    elif comp_move == 2 and user_move == 1:
        comp += 1
        print("Aw the computer wins this one!")
    elif comp_move == 2 and user_move == 4:
        comp += 1
        print("Aw the computer wins this one!")


counter = "y"
while True:
    if counter == "Score" or counter == "score":
        print("The score is:\nYou\tComputer\n"+str(user)+"\t"+str(comp))
        counter = input("Do you want to play again? (Y/N) ")
    if counter == "User Count" or counter == "user count":
        print("The user choice count is:\nRock\tPaper\tScissors\n"+str(user_rock)+"\t"+str(user_paper)
              + "\t"+str(user_scissors))
        counter = input("Do you want to play again? (Y/N) ")
    if counter == "Comp Count" or counter == "comp count":
        print("The computer choice count is:\nRock\tPaper\tScissors\n"+str(comp_rock)+"\t"+str(comp_paper)
              + "\t"+str(comp_scissors))
        counter = input("Do you want to play again? (Y/N) ")
    if counter == "N" or counter == "n" or counter == "No" or counter == "no":
        print("The ending score is:\nYou\tComputer\n"+str(user)+"\t"+str(comp)+"\nThanks for playing my game! ")
        break
    elif counter == "Y" or counter == "y" or counter == "Yes" or counter == "yes":
        play()
        counter = input("Do you want to play again? (Y/N)\nTo check the current score type 'score'."
                        "\nTo check the choice count type either 'user count' or 'comp count'. ")
    else:
        print("Required response is either yes/no.")
        counter = input("Do you want to play again? (Y/N) ")
    print("\n\n")
    
