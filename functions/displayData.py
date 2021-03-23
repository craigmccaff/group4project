
def displayData(allPlayerData, selectedGame, gamemodeStats):

    for counter in gamemodeStats[selectedGame]:
        try:
            print(counter.capitalize() + " " + str(allPlayerData['player']['stats'][selectedGame][counter]))
        except:
            print(counter.capitalize() + " " + "0")
