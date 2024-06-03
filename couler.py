import argparse
import json
import os
import secrets
from datetime import datetime

def readContentInDataFile():
    try:
        return json.loads(open('.couler/data.json', 'r').read())
    except:
        return []

def writeInDataFile(data:list):
    dataFile = open('.couler/data.json', 'w')
    dataFile.write(json.dumps(data))

def createCoreFolder():
    os.mkdir('.couler')
    dataFile = open('.couler/data.json', 'w')
    dataFile.write('[]')

def findByString(str:str, arr:list):
    try: 
        arr.index(str)
        return True
    except ValueError:
        return False

def checkExistCoulerFolder():
    path = os.getcwd()
    dirs = os.listdir(path)
    existCoulerFolder = findByString('.couler', dirs)

    return existCoulerFolder

def initParser():
    existCoulerFolder = checkExistCoulerFolder()

    if not existCoulerFolder:
        createCoreFolder()
    else:
        print('Couler was previously initiated')

def addParser(task:str, data:list):
    taskTemplate = {
        'id': secrets.token_hex(4),
        'description': task,
        'status': False,
        'create-at': str(datetime.now()).split(' ')[0]
    }

    data.append(taskTemplate)
    writeInDataFile(data)

def logParser(data:list):
    headerTable = '\nStatus\tDescription\tID\n'

    if data:
        print(headerTable)

        for item in data:
            statusItem = ('\033[92m' + '✔' + '\033[0m') if item['status'] else ('\033[91m' + '𐄂' + '\033[0m')
            print(
                statusItem + '\t' +
                '\033[97m' + item['description'] + '\033[0m' '\t' +
                item['id'] + '\t'
            )
    else:
        print('\033[97m' + '\nThere are no pending tasks' + '\033[0m')

def checkParser(id:str, data:list):
    for item in data:
        if item['id'] == id:
            item['status'] = True
    
    writeInDataFile(data)

def deleteParser(id:str, data:list):
    global count
    global existTask 

    count = 0
    existTask = False

    for item in data:
        if item['id'] == id:
            existTask = True
            break
        count += 1

    if existTask:
        data.pop(count)
        writeInDataFile(data)

def main():
    parser = argparse.ArgumentParser(
        description = 'Couler, a CLI to manage tasks'
    )

    sub_parsers = parser.add_subparsers(dest='command')

    sub_parsers.add_parser('init')

    add_parser = sub_parsers.add_parser('add')
    add_parser.add_argument('task', metavar='task')

    sub_parsers.add_parser('list')

    update_parser = sub_parsers.add_parser('check')
    update_parser.add_argument('id', metavar='check')

    delete_parser = sub_parsers.add_parser('delete')
    delete_parser.add_argument('id', metavar='delete')

    args = parser.parse_args()
    data = readContentInDataFile()

    if args.command == 'init': initParser()
    if args.command == 'add': addParser(args.task, data)
    if args.command == 'list': logParser(data)
    if args.command == 'check': checkParser(args.id, data)
    if args.command == 'delete': deleteParser(args.id, data)

if __name__ == '__main__':
    main()