import argparse
import json
import os
import secrets
from datetime import datetime
from terminaltables import AsciiTable

def readContentInDataFile():
    return json.loads(open('.couler/data.json', 'r').read())

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
    tableData = [
        ['\033[36m' + 'ID' + '\033[0m', 
         '\033[36m' + 'Description' + '\033[0m', 
         '\033[36m' + 'Status' + '\033[0m', 
         '\033[36m' + 'Date' + '\033[0m'
        ]
    ]

    for item in data:
        tableData.append(
            ['\033[32m' + item['id'] + '\033[0m', 
             '\033[97m' + item['description'] + '\033[0m', 
             '\033[33m' + str(item['status']) + '\033[0m', 
             '\033[36m' + item['create-at'] + '\033[0m'
            ]
        )

    table = AsciiTable(tableData)
    print(table.table)

def updateParser(id:str, data:list):
    for item in data:
        if item['id'] == id:
            item['status'] = not item['status']
    
    writeInDataFile(data)

def main():
    parser = argparse.ArgumentParser(
        description = 'Couler, a CLI to manage tasks'
    )

    sub_parsers = parser.add_subparsers(dest='command')

    sub_parsers.add_parser('init')

    add_parser = sub_parsers.add_parser('add')
    add_parser.add_argument('task', metavar='task')

    sub_parsers.add_parser('log')

    update_parser = sub_parsers.add_parser('update')
    update_parser.add_argument('id_task', metavar='update')

    delete_parser = sub_parsers.add_parser('delete')
    delete_parser.add_argument('tasK_id', metavar='delete')

    args = parser.parse_args()
    storage = readContentInDataFile()

    if args.command == 'add':
        addParser(args.task, storage)
    elif args.command == 'log':
        logParser(storage)
    elif args.command == 'update':
        updateParser(args.id_task, storage)
    elif args.command == 'delete':
        print('Is delete')
    elif args.command == 'init':
        initParser()

if __name__ == '__main__':
    main()