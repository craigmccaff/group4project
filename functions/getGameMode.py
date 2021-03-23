def inputGameMode():
    return input("What game mode would you like to search for?")


def getGameMode():

    searchGame = inputGameMode()

    skywarsNames = ['sw', 'skyw', 'skywars', 'swars', 'sky', 'skywar']
    bedNames = ['bw', 'bedw', 'bedwars', 'bwars', 'bed', 'bedwar']
    hungerGamesNames = ['hg', 'hunger', 'hungergames', 'hgs', 'survivalgames', 'sg']

    flag = True
    while flag:
        if searchGame.lower() in skywarsNames:
            return "SkyWars"
        if searchGame.lower() in bedNames:
            return "Bedwars"
        if searchGame.lower() in hungerGamesNames:
            return "HungerGames"
        else:
            searchGame = input("Incorrect input: What gamemode would you like to search for? (Skywars, Bedwars, HungerGames)")

