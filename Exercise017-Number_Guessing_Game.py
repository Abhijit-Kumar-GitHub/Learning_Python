"""GUESS THE NUMBER BETWEEN 1 AND 100"""
# TAKE A RANDOM NO. BETWEEN 1 TO 100, THEN LET THE USER GUESS IT AND IF WRONG GIVE HINTS LIKE LOW OR HIGH
#   AND COUNT THE NO. OF GUESSES AS WELL

import random

low = 1
high = 100
number = random.randint(low, high)
count= 0

while True:
    guess = int(input(f"Enter a number between {low}-{high}: "))
    count+=1

    if guess > number:
        print(f"Your guess, {guess} is too high.")
    elif guess < number:
        print(f"Your guess, {guess} is too low.")
    else:
        print(f"Your guess, {guess} is correct.")
        break

print(f"This round took you {count} attempts.")