from functions import getKillsDeaths, gameModeStatsDict, getRatio


def displayData(allPlayerData, selectedGame, gamemodeStats):
    kills = getKillsDeaths.getKills(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)
    deaths = getKillsDeaths.getDeaths(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)
    for counter in gamemodeStats[selectedGame]:
        try:
            print(counter.capitalize() + " " + str(allPlayerData['player']['stats'][selectedGame][counter]))
        except:
            print(counter.capitalize() + " " + "0")
    getRatio.ratio(kills, deaths)
