import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(1, root_dir)

import src.tricks as tricks
import unittest
from unittest.mock import mock_open, patch

class TestTricksFunction(unittest.TestCase):
    # Tricks test cases start here
    def test_coerce_with_valid_input(self):
        result = tricks.coerce("42")
        self.assertEqual(result, 42)

    def test_coerce_with_invalid_input(self):
        result = tricks.coerce("invalid")
        self.assertEqual(result, "invalid")

    @patch('builtins.open', mock_open(read_data='1,2,3\n4,5,6\n'))
    def test_csv_parser(self):
        result = list(tricks.csv(file="example.csv"))
        expected_output = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(result, expected_output)
    # Tricks test cases end here
        

if __name__ == "__main__":
    unittest.main()