import random

class Game:
    def __init__(self, min: int, max: int):
        """
        Initialize the game with a minimum and maximum value.
        - Store the min and max values.
        - Generate a random number within this range for the player to guess.
        """
        self.answer = random.randint(min, max)


    def check_guess(self, guess: int) -> bool:
        """
        Check if the player's guess is correct.
        - Compare the guess to the target number.
        - Return True if correct, False otherwise.
        """
        if self.answer == guess:
            return True
        else:
            return False