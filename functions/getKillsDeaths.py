def getKills(allPlayerData, selectedGame, gamemodeStats):
    try:
        return allPlayerData['player']['stats'][selectedGame][gamemodeStats[selectedGame][0]]
    except:
        return "0"


def getDeaths(allPlayerData, selectedGame, gamemodeStats):
    try:
        return allPlayerData['player']['stats'][selectedGame][gamemodeStats[selectedGame][1]]
    except:
        return "0"
