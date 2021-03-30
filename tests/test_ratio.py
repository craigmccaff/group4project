import unittest
from unittest import TestCase
from functions import getRatio


class Test(TestCase):
    def test_ratio(self):
        self.assertEqual(getRatio.ratio(20,10), "KD Ratio 2.0")

    def test_ratio_no_deaths(self):
        self.assertEqual(getRatio.ratio(10,0),"KD Ratio 10")

    def test_ratio_no_kills(self):
        self.assertEqual(getRatio.ratio(0,1),"KD Ratio 0.0")

    def test_ratio_no_kills_or_deaths(self):
        self.assertEqual(getRatio.ratio(0,0),"KD Ratio 0")

if __name__ == '__main__':
    unittest.main()

