import requests 
import configparser
import os
import json
import colormsg as cmsg

#Directories in Program
DIR_PATH = os.path.dirname(__file__)
CONFIG_PATH = os.path.join(DIR_PATH, 'config' )
DATA_PATH = os.path.join(DIR_PATH, 'data')

#config Files
configApp = os.path.join(CONFIG_PATH, 'app.ini')
config= configparser.ConfigParser()

config.read(configApp)

#data
programsJsonPath = os.path.join(DATA_PATH, 'programs.json')
##Lists
gamesIDList=[]


def ammountInfo():
    url = config['Links']['linkGamesProtonDBCount']
    r = requests.get(url)
    response = r.json()
    ammountOfGames = response['uniqueGames']
    return "Current Amount of Games on ProtonDB is: %s" %ammountOfGames 



def CreateProgramsJson():
    with open (programsJsonPath, "w+") as f: 
        try:
            r = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v0002/?format=json')
            response = r.json()
            programlist = response['applist']['apps']
            json.dump(programlist, f)
        except Exception as e:
            print(e)
        
def readJson(file):
    pass

def CreateProgramsList():
    programIdList=[]
    with open (programsJsonPath, "r") as f:
        temp = json.load(f)
        for program in temp:
            programIdList.append(temp['appid'])
    return programIdList    

def CheckProtonDBStatus(*args):
    for game in args:
        try:
            url = config['Links']['linkGameProtonDBStatus'] + str(game) + '.json'
            r = requests.get(url)
            response = r.json()
            temppath  = os.path.join( DATA_PATH , 'games-status',str(game)+'.json')
            with open(temppath, 'w+') as f:
                json.dump(response, f)
        except json.JSONDecodeError as e:
            with open("testlog.txt", 'w+') as f:
                str(e)
                f.write(str(e))
        except ValueError as e:
            print(cmsg.WarnningMsg(e))
        except NoneType as e:
            print(cmsg.WarrningMsg(e))
            print("There might be a problem with amount of requests")
        except TypeError as e:
            print(e)
        except Exception as e:
            print(e)

            

def CreateFile(path):
    with open(path , 'w+'):
        print("Path %s has been created" %path)


###################
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

el = cmsg.InfoMsg(ammountInfo())
CreateProgramsJson()
CheckProtonDBStatus(1303100)
print(el)

