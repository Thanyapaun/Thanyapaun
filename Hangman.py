# Project2: Hangman

import random
from words import words_list

player = int(input("Please select: 1 Player or 2 Players \n"))
if player == 2:
    word = input("Player 1 create a secret word here: ").upper()
    print(" \n" * 30)
else:
    word = random.choice(words_list)
    word = word.upper()

print("")
print("Let's play Hangman!")
print("")
print("     |-------")
print("     |      |")
print("     |")
print("     |")
print("     |")
print("     |")
print("     |")
print("     |")
print("    ---")
print("")

hidden = []

for letter in word:
    hidden.append("_")

attempts = 0
max_attempts = 3

isGameOver = False

while not isGameOver:
    print("")
    print(f"You can guess wrong {max_attempts} more times.")
    hiddenString = "".join(hidden)
    print("")
    print(f"The current word is: {hiddenString}")

    letterGuessed = input("Please guess a letter: ")
    LetterGuessed = letterGuessed.upper()

    if LetterGuessed in word:
        print("You guessed correctly! " + LetterGuessed + " is in the word!")
        for i in range(len(word)):
            character = word[i]
            if character == LetterGuessed:
                hidden[i] = word[i]
            hiddenString = "".join(hidden)
            if hiddenString == word:
                isGameOver = True
                print("")
                print("")
                print("     |-------")
                print("     |      |")
                print("     |")
                print("     |")
                print("     |")
                print("     |     /O/")
                print("     |      ||")
                print("     |     / |")
                print("    ---")
                print("")
                print("Congrats! YOU WON!")
                print("")
                break

    else:
        print(LetterGuessed + " is NOT in the word.")
        attempts += 1
        max_attempts -= 1
        print("")
        print("     |-------")
        print("     |      |")
        print("     |      " + "O" if attempts >= 1 else "     |")
        print("     |     " + "/ |" if attempts >= 2 else "     |")
        print("     |      " + "||" if attempts >= 3 else "     |")
        print("     |")
        print("     |")
        print("     |")
        print("    ---")
        print("")
        if max_attempts == 0:
            isGameOver = True
            print("")
            print("-----GAME OVER-----")
            print("")
            print("The word is:")
            print(word)
            print("")
            break
