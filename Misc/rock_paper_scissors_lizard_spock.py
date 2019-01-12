#The Lizard-Spock Expansion: A Simple Python Program
#From the hit TV show: The Big Bang Theory

from random import randint

myList = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

userChoice = False

AI = myList[randint(0, 4)]

while userChoice == False:
    userChoice = input("Enter your choice: Rock/Paper/Scissors/Lizard/Spock:\n")
    if userChoice == AI:
        print("DRAW!")
    elif userChoice == "Rock":
        if AI == "Scissors" or AI == "Lizard":
            print("You Win! Rock crushes Scissors and crushes Lizard - AI chose:", AI)
        else:
            print("You Lose! AI chose:", AI)

    elif userChoice == "Paper":
        if AI == "Rock" or AI == "Spock":
            print("You Win! Paper covers Rock and disproves Spock - AI chose:", AI)
        else:
            print("You Lose! AI chose:", AI)

    elif userChoice == "Scissors":
        if AI == "Paper" or AI == "Lizard":
            print("You Win! Scissors cuts Paper and decapitates Lizard - AI chose:", AI)
        else:
            print("You Lose! AI chose:", AI)

    elif userChoice == "Lizard":
        if AI == "Spock" or AI == "Paper":
            print("You Win! Lizard poisons Spock and eats Paper - AI chose:", AI)
        else:
            print("You Lose! AI chose:", AI)

    elif userChoice == "Spock":
        if AI == "Rock" or AI == "Scissors":
            print("You Win! Spock vaporises Rock and smashes Scissors - AI chose:", AI)
        else:
            print("You Lose! AI chose:", AI)

    else:
        print("Invalid Choice")

'''
OUTPUT 1:
Enter your choice: Rock/Paper/Scissors/Lizard/Spock:
Rock
You Lose! AI chose: Paper

OUTPUT 2:
Enter your choice: Rock/Paper/Scissors/Lizard/Spock:
Paper
DRAW!

OUTPUT 3:
Enter your choice: Rock/Paper/Scissors/Lizard/Spock:
Scissors
You Win! Scissors cuts Paper and decapitates Lizard - AI chose: Paper

OUTPUT 4:
Enter your choice: Rock/Paper/Scissors/Lizard/Spock:
Lizard
You Lose! AI chose: Scissors

OUTPUT 5:
Enter your choice: Rock/Paper/Scissors/Lizard/Spock:
Spock
You Win! Spock vaporises Rock and smashes Scissors - AI chose: Scissors

OUTPUT 6:
Enter your choice: Rock/Paper/Scissors/Lizard/Spock:
James T. Kirk
Invalid Choice
'''
