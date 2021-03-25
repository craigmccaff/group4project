# from unittest.mock import MagicMock, patch
# import unittest
# from functions import displayData, returnJsonAsDict, gameModeStatsDict, getGameMode
#
#
# class DisplayData(unittest.TestCase):
#     def testDisplay(self):
#         data = returnJsonAsDict.getInput()
#         getGameMode.getGameMode = MagicMock(return_value="SkyWars")
#         print(displayData.displayData(data, getGameMode.getGameMode(), gameModeStatsDict.gamemodeStats))
#         # self.assertEquals(displayData.displayData(data, getGameMode.getGameMode(), gameModeStatsDict.gamemodeStats), not None)
#
# if __name__ == '__main__':
#     unittest.main()