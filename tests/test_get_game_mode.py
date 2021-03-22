import unittest
from unittest.mock import MagicMock
from functions import getGameMode


class GetGameModeTest(unittest.TestCase):
    def test_searchGameValue(self):
        getGameMode.inputGameMode = MagicMock(return_value = "sky")
        self.assertEqual(getGameMode.getGameMode(), "SkyWars")

if __name__ == '__main__':
    unittest.main()
