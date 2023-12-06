# tic_tac_toe_inclass
Welcome to my tic-tac-toe game! Enjoy!

## Description

This is a simple implementation of the Tic Tac Toe game with a command-line interface (CLI). The game supports both single-player (human vs. bot) and two-player (human vs. human) modes.

## How to Run the Game

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Run the game:

    ```bash
    python cli.py
    ```

3. Follow the prompts to select the game mode (single or two) and make moves according to the displayed board.

## How to Run Tests

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install dependencies (if needed):

    ```bash
    # Example for pip
    pip install -r requirements.txt
    ```

3. Run the tests:

    ```bash
    # Example using unittest
    python -m unittest tests.py

    # Example using pytest
    pytest tests.py
    ```

Adjust the commands based on your specific environment and package manager. Make sure to replace `<repository-url>` and `<repository-directory>` with your actual repository information.

## Test Coverage

The provided tests in `tests.py` cover the following features:

- Game initialization (mode, current player, board, winner)
- Player switching
- Checking for a winner in rows, columns, and diagonals
- Identifying a draw game
- Verifying the absence of a winner

Feel free to add more tests as needed to further enhance the test coverage.
