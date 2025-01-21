# Number Guessing Game

## Project Overview

This is a simple number guessing game where players try to guess a randomly generated number within a specified range.

## Project Structure

The project consists of three main Python files:

### 1. `game.py`

Contains the core game logic class `Game` with two main methods:

- `__init__`: Initializes the game with a range
- `check_guess`: Validates player guesses

### 2. `driver.py`

The main program that:

- Sets up the game
- Handles user input
- Manages the game loop

### 3. `tests.py`

Contains unit tests to verify:

- Number generation within specified ranges
- Correct guess validation
- Multiple test cases with random ranges

## Setup and Running

### Prerequisites

- Python 3.6 or higher
- Git installed on your system

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/number-guessing-game.git
```

2. Navigate to the project directory:

```bash
cd number-guessing-game
```

### Running the Game

Run the game using Python:

```bash
python driver.py
```

### Running the Tests

Execute the test suite with:

```bash
python -m unittest tests.py
```

## Project Goals

1. Implement the `Game` class methods
2. Ensure all tests pass

## Expected Behavior

- Game generates a random number within the specified range
- Players input guesses until correct
- Program provides feedback on each guess
