def writeToFile(data):
    for item in data:
        PlayerDataQueries.append(item)
        PlayerDataQueries.append(", ")
    PlayerDataQueries.append("\n")
