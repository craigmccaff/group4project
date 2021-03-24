import unittest
from unittest.mock import MagicMock
from functions import getGameMode


class GetGameModeTest(unittest.TestCase):

    def test_searchGameMode(self):
        getGameMode.inputGameMode = MagicMock(return_value = "hungergames")
        self.assertEqual(getGameMode.getGameMode(), "HungerGames")

    def test_searchAcronym(self):
        getGameMode.inputGameMode = MagicMock(return_value = "sky")
        self.assertEqual(getGameMode.getGameMode(), "SkyWars")

    def test_capitalSearch(self):
        getGameMode.inputGameMode = MagicMock(return_value = "SKYWARS")
        self.assertEqual(getGameMode.getGameMode(), "SkyWars")

    def test_gameModeError(self):
        getGameMode.inputGameMode = MagicMock(side_effect = ["error handling works", "bedwars"])
        self.assertEqual(getGameMode.getGameMode(), "Bedwars")

if __name__ == '__main__':
    unittest.main()
