import json
import random

words = json.load(open("data.json"))
keys = list(words.keys())


def hangman():
    turns = 10
    the_word = random.choice(keys).lower()
    while " " in the_word or "-" in the_word:
        the_word = random.choice(keys).lower()
    #print(the_word)
    valid = "abcdefghijklmnopqrstuvwxyz"
    guessemade = ""

    while len(the_word) > 0:
        main = ""
        missed = 0

        for letter in the_word:
            if letter in guessemade:
                main = main + letter
            elif letter == " ":
                main = main + " " + " "
            else:
                main = main + "_ " + " "

        if main == the_word:
            print(main)
            print("You win")
            break

        print("Guess the word: ", main)
        guess = input()

        if guess in valid:
            guessemade = guessemade + guess
        else:
            print("Enter a valid character \n")
            guess = input().lower()

        if guess not in the_word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turn left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name = input('Enter your name \n')
print('welcome ', name)
print("---------------------------")
print("try to guess the word in less than 10 turns!")
hangman()
