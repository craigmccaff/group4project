def displayData(allPlayerInfo, selectedGame):
    gamemodeStats = {
        "SkyWars": ['kills', 'deaths', 'wins'],
        "Bedwars": ['kills_bedwars', 'deaths_bedwars', 'wins_bedwars'],
        "HungerGames": ['kills', 'deaths', 'wins']
    }

    for counter in gamemodeStats[selectedGame]:
        try:
            print(counter + str(allPlayerInfo['player']['stats'][selectedGame][counter]))
        except:
            print(counter + "0")