from termcolor import colored
from random import choice

with open('words.txt') as f:
    words = f.read()
def correct(letter):
    return colored(letter, 'white', 'on_green', attrs=['bold'])
def present(letter):
    return colored(letter, 'white', 'on_yellow', attrs=['bold'])
def absent(letter):
    return colored(letter, 'white', 'on_grey', attrs=['bold'])
def check(word, guess):
    for word_character, guess_character in zip(word, guess):
        if word_character == guess_character:
            print(correct(word_character), end='')
        elif guess_character in word and word_character != guess_character:
            print(present(guess_character), end='')
        else:
            print(absent(guess_character), end='')

def main():
    word = choice(words)
    for i in range(6):
        guess = input()
        while guess not in words:
            guess = input()
        check(word.upper(), guess.upper())
        if guess == word:
            print(f"You won with {5-i} guesses left!")
            break
    else:
        print(f"You lost! The word was {word}.")

main()
