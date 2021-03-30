import json


def writeFile(data):
    with open('../resources/recentSearch.json', 'w') as json_file:
        json.dump(data, json_file)
