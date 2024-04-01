import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(1, root_dir)

import unittest
from unittest.mock import MagicMock
from src.row import ROW

class TestRowFunction(unittest.TestCase):

    #Row test cases start here
    def test_Row(self):
        row_list = [1,2,3,4,5]
        row = ROW(row_list)
        self.assertEqual(row.cells, row_list)
        

    #Row test cases end here


if __name__ == "__main__":
    unittest.main()