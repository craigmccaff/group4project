from unittest import TestCase
from functions import getRatio


class Test(TestCase):
    def test_ratio(self):
        self.assertEqual(getRatio.ratio(10, 5), 2)


