import json


def getRecentSearch():
    with open('../resources/recentSearch.json', 'r') as json_file:
        return json.load(json_file)


def getTestJson():
    with open('../resources/testJson.json') as json_file:
        return json.load(json_file)
