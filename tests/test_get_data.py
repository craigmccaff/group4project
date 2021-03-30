import unittest
from unittest.mock import MagicMock
from functions import getDataAdapter, getSearchName, getData, returnJsonAsDict


class GetDataTest(unittest.TestCase):
    def test_getDataReturnData(self):
        self.assertEqual(getDataAdapter.getDataAdapter(), returnJsonAsDict.getRecentSearch())

    def test_checkName(self):
        getSearchName.searchName = MagicMock(return_value="Jif")
        self.assertEqual(getSearchName.searchName(), returnJsonAsDict.getTestJson()["player"]["displayname"])

    def test_apiSuccess(self):
        getSearchName.searchName = MagicMock(
            side_effect=["Jif", "Skeppy", "Deathkiller", "Deathkiller2", "Deathkiller21", "Slab", "Technoblade", "8", "G", "Car", "finalmouse"])
        self.assertEqual(getData.getData()["success"], True)


if __name__ == '__main__':
    unittest.main()
