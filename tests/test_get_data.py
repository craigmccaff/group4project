import unittest
from unittest.mock import MagicMock
from functions import getDataAdapter, getSearchName, getData, returnJsonAsDict


class GetDataTest(unittest.TestCase):
    def test_getDataReturnData(self):
        self.assertEqual(getDataAdapter.getDataTest(), returnJsonAsDict.getOutput())

    def test_checkName(self):
        getSearchName.searchName = MagicMock(return_value="Jif")
        self.assertEqual(getSearchName.searchName(), returnJsonAsDict.getOutput()["player"]["displayname"])

    def test_apiSuccess(self):
        getSearchName.searchName = MagicMock(
            side_effect=["Jif", "Skeppy", "Deathkiller", "Deathkiller2", "Deathkiller21", "Slab", "Technoblade"])
        self.assertEqual(getData.getData()["success"], True)


if __name__ == '__main__':
    unittest.main()
