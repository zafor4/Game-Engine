# games/number_guessing.py

import random
from .game_base import GameBase

class NumberGuessing(GameBase):
    def __init__(self):
        self.number = random.randint(1, 5)

    def start(self):
        print("Starting Number Guessing Game")
        attempts = 3
        guess = None

        while attempts > 0 and guess != self.number:
            guess = int(input(f"Guess a number between 1 and 5 (You have {attempts} tries left): "))
            if guess < self.number:
                print("Too low!")
            elif guess > self.number:
                print("Too high!")
            else:
                print("You guessed it!")
                return
            attempts -= 1
        
        if guess != self.number:
            print(f"Sorry, you've run out of tries. The correct number was {self.number}.")

    def get_name(self):
        return "Number Guessing"
