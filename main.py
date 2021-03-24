from functions import displayData, getData, getGameMode, getKillsDeaths, getRatio, gameModeStatsDict

allPlayerData = getData.getData()
selectedGame = getGameMode.getGameMode()

kills = getKillsDeaths.getKills(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)
deaths = getKillsDeaths.getDeaths(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)

displayData.displayData(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)

getRatio.ratio(kills, deaths)

