from functions import getData, getSearchName
import json

def getDataTest():

    flag = True
    while flag:
        name = getSearchName.searchName()
        with open ('resources/testGetDataInput.json') as json_file:
            data = json.load(json_file)
            if data['success'] == True:
                return (data)
            else:
                print("You have recently searched for this name, please wait before searching again.")

