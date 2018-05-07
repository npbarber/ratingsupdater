import unittest

import update_ratings

class UpdateTargetDataTestCase(unittest.TestCase):
    def test_player_ratings_are_updated(self):
        left = {
            '123': {'rating': 300},
            '456': {'rating': 900},
        }
        right = {
            '123': {'rating': 200},
            '456': {'rating': 900},
        }
        got = update_ratings.update_target_data(left, right)
        expected = {
            '123': {'rating': 300},
            '456': {'rating': 900},
        }
        self.assertEqual(expected, got)

    def test_players_missing_from_target_are_added(self):
        left = {
            '123': {'rating': 300},
            '456': {'rating': 900},
        }
        right = {
            '123': {'rating': 200},
        }
        got = update_ratings.update_target_data(left, right)
        expected = {
            '123': {'rating': 300},
            '456': {'rating': 900},
        }
        self.assertEqual(expected, got)
