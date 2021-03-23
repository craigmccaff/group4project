

def displayData(allPlayerData, selectedGame, gamemodeStats):

    for counter in gamemodeStats[selectedGame]:
        try:
            print(counter + str(allPlayerData['player']['stats'][selectedGame][counter]))
        except:
            print(counter + "0")
