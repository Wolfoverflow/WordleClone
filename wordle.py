from termcolor import colored
from random import choice
import wordle_words

words = wordle_words.words
def correct(letter):
    return colored(letter, 'white', 'on_green', attrs=['bold'])
def present(letter):
    return colored(letter, 'white', 'on_yellow', attrs=['bold'])
def absent(letter):
    return colored(letter, 'white', 'on_grey', attrs=['bold'])

def check(word, guess):
    output = []
    counter = {}

    for i in word:
        counter[i] = 0
    for i in word:
        counter[i] += 1

    for iter, i in enumerate(guess):
        if i == word[iter]:
            counter[i] -= 1

    for iter, i in enumerate(guess):
        if i == word[iter]:
            output.append(correct(i))
        elif i in word:
            if counter[i] != 0:
                output.append(present(i))
                counter[i] -= 1
            else:
                output.append(absent(i))
        else:
            output.append(absent(i))

    print("\r\r" + ''.join(output) + "                     ")


def main():
    word = choice(words)
    print("Best of luck!")
    for i in range(6):
        guess = input("_____\r")
        while guess not in words:
            print("\rInvalid guess. Try again.")
            guess = input("_____\r")
        check(word.upper(), guess.upper())
        if guess == word:
            print(correct(guess.upper()))
            print(f"You won with {5-i} guesses left!")
            break
    else:
        print(f"You lost! The word was {word}.")

main()
