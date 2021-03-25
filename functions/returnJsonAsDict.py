import json


def getOutput():
    with open('../resources/testGetDataOutput.json') as json_file:
        return json.load(json_file)


def getInput():
    with open('../resources/testGetDataInput.json') as json_file:
        return json.load(json_file)
