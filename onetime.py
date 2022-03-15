import requests 
import configparser
import sys
import os
import time
import threading


config= configparser.ConfigParser()


listSize=int(sys.argv[1])
listMax=int(sys.argv[2])

DIR_PATH = os.path.dirname(__file__)
configName='app.ini'
configPath= os.path.join(DIR_PATH,'config',configName)
config.read(configPath)
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
    data_path = os.path.join(DIR_PATH, 'data', 'allPrograms.txt')
    with open (data_path, "w+") as f: 
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
        


def checkIfProtonDBGame(*args):
    for i in args:
        try:
            strid = str(i)
            url = config['Links']['linkGameInfo'] + strid
            r=requests.get(url)
            response = r.json()
            succesBool = response[strid]['success']
            if succesBool:
                obtype = response[strid]['data']['type']
                if obtype == 'game':
                    gamesIDList.append(i)
        except Exception as e:
            print(strid)
            print(e)


ammountInfo()
getProgramList()


start = time.perf_counter()

lbeg =int((listMax - listSize)+1)
lend = int((listMax/5)*1)
thread1= threading.Thread(target=checkIfProtonDBGame, args=programsIdList[lbeg:lend])

lbeg =int((listMax/5)*1+1)
lend =int( (listMax/5)*2)
thread2 = threading.Thread(target=checkIfProtonDBGame, args=programsIdList[lbeg:lend])

lbeg =int((listMax/5)*2+1)
lend =int( (listMax/5)*3)
thread3= threading.Thread(target=checkIfProtonDBGame, args=programsIdList[lbeg:lend])

lbeg =int((listMax/5)*3+1)
lend =int( (listMax/5)*4)
thread4 = threading.Thread(target=checkIfProtonDBGame, args=programsIdList[lbeg:lend])

lbeg =int((listMax/5)*4+1)
lend =int(listMax)
thread5 = threading.Thread(target=checkIfProtonDBGame, args=programsIdList[lbeg:lend])

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()



name = "GamesID"+str(listSize)+"_"+str(listMax)+".txt"

try:
    data_path = os.path.join(DIR_PATH, 'data', name)
    with open(data_path, 'w+' ) as f:
        for item in gamesIDList:
            f.write(str(item) + '\n')
        f.close()
except Exception as e:
    print(e)

end = time.perf_counter()
print(gamesIDList)
print(end - start)
