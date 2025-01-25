from game import Game

# Define the minimum and maximum values for the guessing range
min_val = int(input("Enter a minimum: "))
max_val = int(input("Enter a maximum: "))

print("Welcome to the guessing game!")

# Create an instance of the Game with the specified range
game = Game(min_val, max_val)

guess = -1  # Initialize the guess variable

# Continue looping until the player makes a correct guess
while not game.check_guess(guess):
    try:
        # Prompt the player to enter their guess within the specified range
        guess = int(input(f"Guess the number between {min_val} and {max_val}: "))
    except ValueError:
        # Handle cases where the input is not a valid integer
        print("Please enter a valid integer.")

print("You guessed correctly!")
