import requests


def searchName():
    searchName = input('What name would you like to search for? ')
    return searchName


def getData():
    API_KEY = "c1e412b1-5131-49f9-b7a2-bdfda4371684"
    data = requests.get(f"https://api.hypixel.net/player?key={API_KEY}&name={searchName()}").json()
    print(data)
    return data


def filterData():
    skywarsNames = ['sw', 'skyw', 'skywars', 'swars', 'sky', 'skywar', 'sky wars', 'sky war']
    bedNames = ['bw', 'bedw', 'bedwars', 'bwars', 'bed', 'bedwar', 'bed wars', 'bed war']
    hungerGamesNames = ['hg', 'hunger', 'hungergames', 'hgs', 'survivalgames', 'sg', 'survival games', 'hunger games']

    flag = True
    while flag:
        searchGame = input("What gamemode would you like to search for? ")
        if searchGame.lower() in skywarsNames:
            return "SkyWars"
        if searchGame.lower() in bedNames:
            return "Bedwars"
        if searchGame.lower() in hungerGamesNames:
            return "HungerGames"


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


displayData(getData(), filterData())
