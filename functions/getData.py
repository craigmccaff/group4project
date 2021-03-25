from functions import getSearchName
import requests

def getData():
    API_KEY = "c1e412b1-5131-49f9-b7a2-bdfda4371684"

    flag = True
    while flag:
        name = getSearchName.searchName()
        data = requests.get(f"https://api.hypixel.net/player?key={API_KEY}&name={name}").json()
        if data['success'] == True:
            return data
        else:
            print("You have recently searched for this name, please wait before searching again.")