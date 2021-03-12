import unittest
from unittest.mock import MagicMock
import main


class SearchNameTest(unittest.TestCase):
    def test_searchName(self):
        main.searchName = MagicMock(return_value = "jif")
        self.assertEqual(main.searchName(), "jif")


if __name__ == '__main__':
    unittest.main()
