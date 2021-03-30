from functions import getSearchName, writeDataToJson, returnJsonAsDict
import requests


def getData():
    API_KEY = "c1e412b1-5131-49f9-b7a2-bdfda4371684"
    choice = input("Type <JSON> to load from JSON otherwise it'll use the API ")
    if choice.lower() == "json":
        data = returnJsonAsDict.getRecentSearch()
        return data
    else:
        flag = True
        while flag:
            name = getSearchName.searchName()
            data = requests.get(f"https://api.hypixel.net/player?key={API_KEY}&name={name}").json()
            if data['success'] == True:
                writeDataToJson.writeFile(data)
                return data
            else:
                print("You have recently searched for this name, please wait before searching again.")
