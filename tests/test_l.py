import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(1, root_dir)

from src.l import l
import unittest

class TestLScript(unittest.TestCase):
    def test_rnd_test(self):
       self.assertEqual(l().rnd(23.324234), 23.32)
       self.assertEqual(l().rnd(23.324234, 3), 23.324)

    def test_keysort(self):
            # Define a sample list to be sorted
            t = [4, 2, 5, 1, 3]

            # Define a sorting function
            def square(x):
                return x ** 2

            # Apply the keysort method
            sorted_list = l().keysort(t, square)

            # Expected result after sorting by squares: [1, 2, 3, 4, 5]
            expected_result = [1, 2, 3, 4, 5]

            # Check if the sorted list matches the expected result
            self.assertEqual(sorted_list, expected_result)

if __name__ == "__main__":
    unittest.main()