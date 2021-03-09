import requests

API_KEY = "c1e412b1-5131-49f9-b7a2-bdfda4371684"
SEARCH_NAME = input('What name would you like to search for? ')

data = requests.get(f"https://api.hypixel.net/player?key={API_KEY}&name={SEARCH_NAME}").json()
print(data)
# skywarsWins = data["player"]["stats"]["SkyWars"]["coins"]
# print(skywarsWins)