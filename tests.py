import unittest
from game import Game
import random

class TestGame(unittest.TestCase):
    def generate_min_max_pairs(self, num_pairs=100):
        pairs = []
        for _ in range(num_pairs):
            # Generate random min and max values
            min_val = random.randint(-100, 100)
            max_val = min_val + random.randint(1, 100)  # Ensure max > min
            pairs.append((min_val, max_val))
        return pairs
    
for i in range(100):
    def create_test(i):
        def test(self):
            min_val = random.randint(-100, 100)
            max_val = min_val + random.randint(1, 100)
            game = Game(min_val, max_val)

            self.assertTrue(min_val <= game.number <= max_val, f"Generated number {game.number} not in range [{min_val}, {max_val}]")
            for guess in range(min_val, max_val + 1):
                if guess != game.number:
                    self.assertEqual(game.check_guess(guess), False)
                else:
                    self.assertEqual(game.check_guess(guess), True)

        return test

    setattr(TestGame, f'test_game_range_{i:03d}', create_test(i))

if __name__ == '__main__':
    unittest.main()