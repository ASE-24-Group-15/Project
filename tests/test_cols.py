import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(1, root_dir)

import unittest

from src.num import NUM
from src.sym import SYM
from src.cols import COLS
from src.row import ROW

class TestColsFunction(unittest.TestCase):
    
    def test_COLSInitialization(self):
        # Test case 1: Check if the class is initialized properly
        row = ROW(["A", "b", "c"])
        cols = COLS(row)

        x = {0: NUM,1: SYM, 2: SYM}
        self.assertDictEqual( {k: type(v) for k, v in cols.x.items()}, x)

        x_txt = {0: "A", 1: "b", 2: "c"}
        self.assertDictEqual( {k: v.txt for k, v in cols.x.items()}, x_txt)

        y = {}
        self.assertDictEqual( {k: type(v) for k, v in cols.y.items()}, y)

        all = [NUM, SYM, SYM]

        self.assertEqual( [type(v) for v in cols.all.values()], all)

        klass = None
        self.assertEqual( cols.klass, klass)
        names = row.cells
        self.assertEqual( cols.names, [names])

        # Test case 2: Check if columns with "!+-" are added to self.x only and names ending with "X" are not taken
        row = ROW(["A", "b!", "C", "dX"])
        cols = COLS(row)

        x = {0: NUM, 2: NUM}
        self.assertDictEqual( {k: type(v) for k, v in cols.x.items()}, x)

        x_txt = {0: "A", 2: "C"}
        self.assertDictEqual( {k: v.txt for k, v in cols.x.items()}, x_txt)

        y = {1: SYM}
        self.assertDictEqual( {k: type(v) for k, v in cols.y.items()}, y)

        all = [NUM, SYM, NUM, SYM]
        self.assertEqual( [type(v) for v in cols.all.values()], all)

        klass = SYM
        self.assertEqual(type(cols.klass), klass)

        names = row.cells
        self.assertEqual( cols.names, [names])

    def test_COLS_add(self):

        # Test case: Check if col.add works

        row = ROW(["A", "b", "c"])
        cols = COLS(row)

        new_row = ROW([1, "e", "f"])
        cols.add(new_row)

        x = {0: NUM,1: SYM, 2: SYM}
        self.assertDictEqual( {k: type(v) for k, v in cols.x.items()}, x)

        x_txt = {0: "A", 1: "b", 2: "c"}
        self.assertDictEqual( {k: v.txt for k, v in cols.x.items()}, x_txt)

        y = {}
        self.assertDictEqual( {k: type(v) for k, v in cols.y.items()}, y)

        all = [NUM, SYM, SYM]

        self.assertEqual( [type(v) for v in cols.all.values()], all)

        klass = None
        self.assertEqual(cols.klass, klass)
        names = row.cells
        self.assertEqual( cols.names, [names])
            
if __name__ == "__main__":
    unittest.main()