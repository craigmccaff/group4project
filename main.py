import requests


def searchName():
    searchName = input('What name would you like to search for? ')
    return searchName


def getData():
    API_KEY = "c1e412b1-5131-49f9-b7a2-bdfda4371684"
    data = requests.get(f"https://api.hypixel.net/player?key={API_KEY}&name={searchName()}").json()
    return data


def filterData():
    skywarsNames = ['sw', 'skyw', 'skywars', 'swars', 'sky', 'skywar']
    bedNames = ['bw', 'bedw', 'bedwars', 'bwars', 'bed', 'bedwar']
    hungerGamesNames = ['hg', 'hunger', 'hungergames', 'hgs', 'survivalgames', 'sg']

    flag = True
    while flag:
        searchGame = input("What gamemode would you like to search for? ")
        if searchGame.lower() in skywarsNames:
            flag = False
            return "SkyWars"
        if searchGame.lower() in bedNames:
            flag = False
            return "Bedwars"
        if searchGame.lower() in hungerGamesNames:
            flag = False
            return "HungerGames"


# This may only work for SkyWars right now as that's the only game with the 'kills' field.
def displayData(allPlayerInfo, selectedGame):
    gamemodeStats = {
        "SkyWars": ['kills', 'deaths', 'wins'],
        "Bedwars": ['kills_bedwars', 'deaths_bedwars', 'wins_bedwars'],
        "HungerGames": ['kills', 'deaths', 'wins']
    }

    for counter in gamemodeStats[selectedGame]:
        if allPlayerInfo["player"]["stats"][selectedGame][counter] is None:
            allPlayerInfo["player"]["stats"][selectedGame][counter] = 0
        print(allPlayerInfo["player"]["stats"][selectedGame][counter])


displayData(getData(), filterData())
