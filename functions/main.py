from functions import displayData, getData, getGameMode, gameModeStatsDict

allPlayerData = getData.getData()
selectedGame = getGameMode.getGameMode()

displayData.displayData(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)

