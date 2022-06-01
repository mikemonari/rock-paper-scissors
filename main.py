#Assigned values
#"R" = "Rock"
#"P" = "Paper"
#"S" = "Scissors"

import random
while True:
    list = ["Rock", "Paper" ,"Scissors"]

    computer = random.choice(list)
    player = None

    while player not in list:
        player = input("pick: Rock, Paper or Scissors: ")

        if player == computer:
            print("computer: ", computer)
            print("player: ", player)
            print("Tie!")

        elif player == "Rock":
            if computer == "Paper":
                print("computer: ", computer)
                print("player: ", player)
                print("Lose!")

            if computer == "Scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("win!")

        elif player == "Paper":

            if computer == "Scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("Lose!")

            if computer == "Rock":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("Win!")

        elif player == "Scissors":
            if computer == "Paper":
                print("computer: ", computer)
                print("player: ", player)
                print("Win!")


            if computer == "Rock":
                print("computer: ", computer)
                print("player: ", player)
                print("Lose!")

    play_on = input("do you want to play on? (Yes or No): ")
    if play_on != "Yes":
        break

print("game over!")
