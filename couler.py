import argparse
import json
import os

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

    if not existCoulerFolder:
        os.mkdir('.couler')
    

def main():
    parser = argparse.ArgumentParser(
        description = 'Couler, a CLI to manage tasks'
    )

    sub_parsers = parser.add_subparsers(dest='command')

    sub_parsers.add_parser('init')

    add_parser = sub_parsers.add_parser('add')
    add_parser.add_argument('task', metavar='task')

    log_parser = sub_parsers.add_parser('log')
    log_parser.add_argument('log', metavar='log')

    update_parser = sub_parsers.add_parser('update')
    update_parser.add_argument('id_task', metavar='update')

    delete_parser = sub_parsers.add_parser('delete')
    delete_parser.add_argument('tasK_id', metavar='delete')

    args = parser.parse_args()

    if args.command == 'add':
        print('Is add')
    elif args.command == 'log':
        print('Is log')
    elif args.command == 'update':
        print('Is update')
    elif args.command == 'delete':
        print('Is delete')
    elif args.command == 'init':
        checkExistCoulerFolder()

if __name__ == '__main__':
    main()