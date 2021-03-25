from functions import displayData, getData, getGameMode, getKillsDeaths, getRatio, gameModeStatsDict
# import json
#
# with open('resources/testGetDataInput.json') as testData:
#     testData = json.load(testData)
#
# print(testData["success"])

allPlayerData = getData.getData()
selectedGame = getGameMode.getGameMode()

kills = getKillsDeaths.getKills(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)
deaths = getKillsDeaths.getDeaths(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)

displayData.displayData(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)

getRatio.ratio(kills, deaths)
