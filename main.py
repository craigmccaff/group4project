from functions import displayData, getData, getGameMode, getKillsDeaths, getRatio, gameModeStatsDict

<<<<<<< Updated upstream
allPlayerData = getData.getData()
selectedGame = getGameMode.getGameMode()

kills = getKillsDeaths.getKills(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)
deaths = getKillsDeaths.getDeaths(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)
=======
def searchName():
    searchName = input('What name would you like to search for? ')
    return searchName
>>>>>>> Stashed changes


displayData.displayData(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)

getRatio.ratio(kills, deaths)

