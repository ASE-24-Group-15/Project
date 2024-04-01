import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(1, root_dir)

import unittest
from unittest.mock import MagicMock
from src.sym import SYM
import src.config as config
from src.gate import argument_parser, SLOTS

class TestSymFunction(unittest.TestCase):

    #Sym test cases start here
    def test_Sym(self):
        sym = SYM()
        syms = ['s', 's', 'd', 'd', 's', 's']
        for s in syms:
            sym.add(s)

        # Test mid and div methods
        self.assertEqual('s', sym.mid())
        self.assertAlmostEqual(0.9182958340544896, sym.div(), places=12)
        
        # args = argument_parser().parse_args()
        # config.the = SLOTS(__doc__= __doc__, **vars(args))
        config.the = SLOTS()
        
        # Test like method
        x = 's'
        prior = 0.5
        config.the.m = 1
        result = sym.like(x, prior)

        expected_result = (sym.has.get(x, 0) + config.the.m * prior) / (sym.n + config.the.m)
        self.assertEqual(expected_result, result)

    #Sym test cases end here

if __name__ == "__main__":
    unittest.main()
