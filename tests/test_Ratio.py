from unittest import TestCase
from functions import Ratio


class Test(TestCase):
    def test_ratio(self):
        self.assertEqual(Ratio.ratio(20,10), 2)


