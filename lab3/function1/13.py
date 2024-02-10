# Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20.
# This is how it should work when run in a terminal:

# Hello! What is your name?
# KBTU

# Well, KBTU, I am thinking of a number between 1 and 20.
# Take a guess.
# 12

# Your guess is too low.
# Take a guess.
# 16

# Your guess is too low.
# Take a guess.
# 19

# Good job, KBTU! You guessed my number in 3 guesses!

import random

def game(rand: int, name: str):
    count = 0
    while True:
        count += 1
        num = int(input("Take a guess.\n"))
        if num < rand:
            print ("Your guess is too low.")
        elif num > rand:
            print ("Your guess is too high.")
        elif num == rand:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break

name = str(input(("Hello! What is your name?\n")))

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
rand = random.randint(1, 20)

game(rand, name)

#done