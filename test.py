import requests
import time
r = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v0002/?format=json')

response = r.json()
gamelist = response['applist']['apps']

with open ("allPrograms.txt", "a+") as f: 
    for game in gamelist:
        f.write(str(game['appid']) + " = " + game['name'] + '\n' )
    f.close()

time.sleep(5)
print("done")