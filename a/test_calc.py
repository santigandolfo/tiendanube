import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(1, calc.add(0,1))

    def test_add2(self):
        self.assertEqual(1, calc.add(0,1))

