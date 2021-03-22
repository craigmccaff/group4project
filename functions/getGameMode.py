def inputGameMode():
    return input("What game mode would you like to search for? (Skywars, Bedwars, HungerGames)")


def getGameMode():

    searchGame = inputGameMode()

    skywarsNames = ['sw', 'skyw', 'skywars', 'swars', 'sky', 'skywar']
    bedNames = ['bw', 'bedw', 'bedwars', 'bwars', 'bed', 'bedwar']
    hungerGamesNames = ['hg', 'hunger', 'hungergames', 'hgs', 'survivalgames', 'sg']

    flag = True
    while flag:
        if searchGame.lower() in skywarsNames:
            flag = False
            return "SkyWars"
        if searchGame.lower() in bedNames:
            flag = False
            return "Bedwars"
        if searchGame.lower() in hungerGamesNames:
            flag = False
            return "HungerGames"
        else:
            print("Incorrect value please enter: skywars, bedwars or hungergames")
            searchGame = inputGameMode()

