from unittest import TestCase
from functions import getRatio


class Test(TestCase):
    def test_ratio(self):
        self.assertEqual(getRatio.ratio(20,10), "KD Ratio 2.0")


