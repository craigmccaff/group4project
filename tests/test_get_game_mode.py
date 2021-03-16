import unittest
from unittest.mock import MagicMock
import main


class SearchNameTest(unittest.TestCase):
    def test_searchGame(self):
        main.searchGame = MagicMock(return_value = "sky")
        self.assertEqual(main.filterData(), "SkyWars")

if __name__ == '__main__':
    unittest.main()
