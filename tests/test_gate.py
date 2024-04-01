import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(1, root_dir)

import unittest
from unittest.mock import patch, MagicMock
from src.gate import argument_parser, main

class TestGateScript(unittest.TestCase):

    def test_argument_parser_defaults(self):
        parser = argument_parser()
        args = parser.parse_args([])
        self.assertEqual(args.bins, 16)
        self.assertEqual(args.Bootstraps, 512)
        self.assertEqual(args.cohen, 0.35)
        self.assertEqual(args.Cliffs, 0.2385)
        self.assertEqual(args.file, "../data/auto93.csv")
        self.assertEqual(args.Far, 0.95)
        self.assertEqual(args.go, "help")
        self.assertEqual(args.Half, 256)
        self.assertEqual(args.p, 2)
        self.assertEqual(args.seed, 1234567891)
        self.assertEqual(args.rest, 3)
        self.assertEqual(args.todo, "help")
        self.assertEqual(args.Top, 10)
        self.assertEqual(args.k, 1)
        self.assertEqual(args.m, 2)

    @patch('src.gate.argument_parser')
    @patch('src.gate.DATA.stats')
    def test_stats_execution(self, mock_stats, mock_arg_parser):
        mock_args = MagicMock()
        mock_args.todo = 'stats'
        mock_arg_parser.return_value.parse_args.return_value = mock_args

        with patch('builtins.print'):
            main()

        mock_stats.assert_called_once()

    @patch('src.gate.argument_parser')
    @patch('src.gate.eg_bayes')
    def test_diabetes_execution(self, mock_eg_bayes, mock_arg_parser):
        mock_args = MagicMock()
        mock_args.todo = 'diabetes'
        mock_arg_parser.return_value.parse_args.return_value = mock_args

        with patch('builtins.print'):
            main()

        mock_eg_bayes.assert_called_once()

    @patch('src.gate.argument_parser')
    @patch('src.gate.eg_km')
    def test_soybean_execution(self, mock_eg_km, mock_arg_parser):
        mock_args = MagicMock()
        mock_args.todo = 'soybean'
        mock_arg_parser.return_value.parse_args.return_value = mock_args

        with patch('builtins.print'):
            main()

        mock_eg_km.assert_called_once()


if __name__ == "__main__":
    unittest.main()

