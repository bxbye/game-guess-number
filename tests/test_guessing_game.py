import unittest
# 4 lines below this sentence are about recognise classes module
import os
import sys
script_dir = os.path.abspath(__file__)
project_dir = os.path.dirname(os.path.dirname(script_dir))
sys.path.append(project_dir)
from classes.guessing_game import GuessingGame, RandomNumberGenerator

class TestGuessingGame(unittest.TestCase):
    # define setup
    def setUp(self) -> None:
        attempt_limit = 10
        self.number_generator = RandomNumberGenerator()
        self.game = GuessingGame(self.number_generator, attempt_limit)
    
    # test target number generation
    def test_target_number(self):
        self.assertGreaterEqual(self.game.target_number, 1)
        self.assertLessEqual(self.game.target_number, 100)
        self.assertEqual(self.game.attempts, [])
        self.assertEqual(self.game.flag, None)

    # test for limited guess. player has max 3 guess.
    def test_end_condition_of_game(self):
        while not self.game.end_condition():
            guess = self.game.get_user_input()
            self.game.check_guess(guess)
        #attempt_limit should be greater then game's attempts lenght
        self.assertGreaterEqual(self.game.attempt_limit, len(self.game.attempts))


        





if __name__ == '__main__':
    unittest.main()