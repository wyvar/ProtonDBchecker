import requests 
import configparser

config= configparser.ConfigParser()
config.read('app.ini')

##Lists
programsIdList=[]
gamesIDList=[]



def ammountInfo():
    url = config['Links']['linkGamesProtonDBCount']
    r = requests.get(url)
    response = r.json()
    ammountOfGames = response['uniqueGames']
    print("Current Amount of Games on ProtonDB is: %s" %ammountOfGames )



def getProgramList():
    with open ("allPrograms.txt", "w+") as f: 
        try:
            r = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v0002/?format=json')
            response = r.json()
            programlist = response['applist']['apps']
            for game in programlist:
                programsIdList.append(game['appid'])
                f.write(str(game['appid']) + " = " + game['name'] + '\n' )
            f.close()
        except:
            pass
        f.close()


def checkIfProtonDBGame():
    for i in gamesIDList:
        try:
            strid = str(i)
            url = config['Links']['linkGameInfo'] + strid
            r=requests.get(url)
            response = r.json()
            succesBool = response[strid]['success']
            if not succesBool:
                gamesIDList.remove(i)
        except Exception as e:
            print('Error during checking games List. If value is 0 ignore: ' )
            print(e)

    return gamesIDList

ammountInfo()
getProgramList()
gamesIDList = programsIdList[1:20]


import time

start = time.perf_counter()

checkIfProtonDBGame()




with open("GamesID.txt", 'w+' ) as f:
    for item in gamesIDList:
        f.write(str(item) + '\n')
    f.close()

end = time.perf_counter()
print(end - start)