# core modules
from utils.findByString import findByString

# third party modules
import os

def checkExistCoulerFolder():
    path = os.getcwd()
    dirs = os.listdir(path)
    existCoulerFolder = findByString('.couler', dirs)

    return existCoulerFolder

def createCoreFolder():
    existCoreFolder = checkExistCoulerFolder()

    if not existCoreFolder:
        os.mkdir('.couler')
        dataFile = open('.couler/data.json', 'w')
        dataFile.write('[]')
    else:
        print('\nA project has already been previously started')