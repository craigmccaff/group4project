import unittest
import json
from unittest.mock import MagicMock
from functions import getDataAdapter, getSearchName

def test_getDataOutput(self):
    with open ('resources/testGetDataInput.json') as json_file:
        output = json.load(json_file)
    getSearchName.searchName = MagicMock(return_value="jif")
    self.assertEqual(getDataAdapter.getDataTest(), output)

test_getDataOutput()