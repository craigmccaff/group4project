from functions import getSearchName
import requests


def getData():
    API_KEY = "c1e412b1-5131-49f9-b7a2-bdfda4371684"
    data = requests.get(f"https://api.hypixel.net/player?key={API_KEY}&name={getSearchName.searchName()}").json()
    print(data)
    return data
