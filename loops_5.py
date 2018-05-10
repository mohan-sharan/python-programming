import random

letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
randomLetter = random.choice(letterList)

numberOfGuesses = 0

print("\nYou have 4 tries to guess a letter between (a-h)\n")

while numberOfGuesses < 4:
    print("Try {}:".format(numberOfGuesses + 1))
    letter = input("Guess a letter between (a-h): ")

    if letter == randomLetter:
        print("\nYou Win! {} was the right guess!!".format(randomLetter))
        break
    numberOfGuesses = numberOfGuesses + 1

    if letter not in letterList:
        print("\n{} is not present between (a-h). Game Over!".format(letter))
        break

else:
    print("\nYou lose! the letter to be guessed was", randomLetter)

'''
OUTPUT 1:
You have 4 tries to guess a letter between (a-h)

Try 1:
Guess a letter between (a-h): b
Try 2:
Guess a letter between (a-h): c
Try 3:
Guess a letter between (a-h): d
Try 4:
Guess a letter between (a-h): a

You lose! the letter to be guessed was f
'''

'''
OUTPUT 2:
You have 4 tries to guess a letter between (a-h)

Try 1:
Guess a letter between (a-h): k

k is not present between (a-h). Game Over!
'''

'''
OUTPUT 3:
You have 4 tries to guess a letter between (a-h)

Try 1:
Guess a letter between (a-h): b
Try 2:
Guess a letter between (a-h): d

You Win! d was the right guess!!
'''	