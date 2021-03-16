import unittest
from unittest.mock import MagicMock
from functions import getSearchName


class GetSearchNameTest(unittest.TestCase):
    def test_getName(self):
        getSearchName.searchName = MagicMock(return_value="jif")
        self.assertEqual(getSearchName.searchName(), "jif")

if __name__ == '__main__':
    unittest.main()
