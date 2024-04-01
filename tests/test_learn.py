import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(1, root_dir)

import unittest
from unittest.mock import MagicMock
from src.learn import learn

class TestLearnFunction(unittest.TestCase):

    def test_learn_update_dict(self):
        data_mock = MagicMock()
        row_mock = MagicMock()

        # Test case 1
        my_dict_1 = {'n': 5, 'tries': 2, 'acc': 1, 'datas': {'class1': data_mock}}
        learn(data_mock, row_mock, my_dict_1)
        self.assertEqual(my_dict_1['n'], 6)
        self.assertEqual(my_dict_1['tries'], 2)
        self.assertEqual(my_dict_1['acc'], 1)

        # Test case 2
        my_dict_2 = {'n': 5, 'tries': 2, 'acc': 1, 'datas': {'class1': data_mock}}
        learn(data_mock, row_mock, my_dict_2)
        self.assertIn('class1', my_dict_2['datas'])
        self.assertEqual(my_dict_2['datas']['class1'], data_mock)

if __name__ == "__main__":
    unittest.main()