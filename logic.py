# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

def make_empty_board():
    """Creates an empty Tic-Tac-Toe board."""
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    for player in ['X', 'O']:
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            row_win = all(board[i][j] == player for j in range(3))
            col_win = all(board[j][i] == player for j in range(3))

            if row_win or col_win:
                return player

            diag1_win = all(board[i][i] == player for i in range(3))
            diag2_win = all(board[i][2 - i] == player for i in range(3))

            if diag1_win or diag2_win:
                return player
    return None

def other_player(player):
    """Given the character for a player, returns the other player."""
    return 'O' if player == 'X' else 'X'