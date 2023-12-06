import unittest
from unittest.mock import patch
from io import StringIO
import logic
from cli import Game

# there are 3 functions in logic.py and the check_winner() to be tested.
class TestLogic(unittest.TestCase):

    # test for the make_empty_board function
    def test_make_empty_board(self):
        empty_board = logic.make_empty_board()
        expected_board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(empty_board, expected_board)

    # test for get_winner function
    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    # additional tests for the check_winner function
    def test_check_winner(self):
        boards = [
            (  # Board 1:
                [
                    ['X', 'X', 'X'],
                    ['O', 'X', 'O'],
                    ['O', 'O', 'X'],
                ],
                'X'  # Expected winner
            ),
            (  # Board 2:
                [
                    ['X', 'O', 'X'],
                    ['O', 'O', 'O'],
                    ['O', 'X', 'X'],
                ],
                'O'  # Expected winner
            ),
            (  # Board 3: 
                [
                    ['O', 'O', 'X'],
                    ['O', 'X', 'O'],
                    ['O', 'O', 'O'],
                ],
                'O'  # Expected winner
            ),
            (  # Board 4: It's a draw
                [
                    ['X', 'O', 'X'],
                    ['O', 'X', 'O'],
                    ['O', 'X', 'O'],
                ],
                None  # Expected winner
            ),
            (  # Board 5:
                [
                    ['X', 'O', 'X'],
                    ['X', '', ''],
                    ['X', '', ''],
                ],
                'X'  # Expected winner
            ),
            (  # Board 6:
                [
                    ['X', 'O', 'O'],
                    ['', 'O', ''],
                    ['', 'O', ''],
                ],
                'O'  # Expected winner
            ),
            (  # Board 7:
                [
                    ['X', '', 'O'],
                    ['', '', 'O'],
                    ['O', '', 'O'],
                ],
                'O'  # Expected winner
            ),
            (  # Board 8: 
                [
                    ['', '', ''],
                    ['', '', ''],
                    ['', '', ''],
                ],
                None  # Expected winner
            ),
            (  # Board 9: 
                [
                    ['X', '', 'X'],
                    ['', 'X', 'O'],
                    ['X', 'O', 'X'],
                ],
                'X'  # Expected winner
            ),
            (  # Board 10: 
                [
                    ['O', 'X', 'O'],
                    ['', 'O', 'O'],
                    ['X', 'X', 'O'],
                ],
                'O'  # Expected winner
            ),
        ]

        for i, (board, expected_winner) in enumerate(boards, start=1):
            with self.subTest(board_number=i):
                self.assertEqual(logic.get_winner(board), expected_winner)

    # test for the other_player function
    def test_other_player(self):
        player_x = 'X'
        player_o = 'O'
        self.assertEqual(logic.other_player(player_x), 'O')
        self.assertEqual(logic.other_player(player_o), 'X')

class TestGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['single'])
    def test_game_init_single_mode(self, mock_input):
        game = Game(mode='single')
        self.assertEqual(game.mode, 'single')

    @patch('builtins.input', side_effect=['two'])
    def test_game_init_two_players_mode(self, mock_input):
        game = Game(mode='two')
        self.assertEqual(game.mode, 'two')

    def test_game_init_empty_board(self):
        game = Game(mode='single')
        self.assertEqual(game.board, logic.make_empty_board())

if __name__ == '__main__':
    unittest.main()