# core modules
from core.addCoreFolder import checkExistCoulerFolder
from core.fileManagement import readContent
from utils.commandsList import COMMANDS_LIST
from commands.init import init
from commands.add import add
from commands.log import log
from commands.check import check
from commands.delete import delete

# Third party modules
import argparse

def main():
    client = argparse.ArgumentParser(
        prog = 'Couler',
        description = 'A list of tasks in your terminal'
    )

    clientParser = client.add_subparsers(dest='command')

    # parsers without arguments
    clientParser.add_parser(COMMANDS_LIST['INIT'])
    clientParser.add_parser(COMMANDS_LIST['LOG'])

    #parsers with arguments
    addParser = clientParser.add_parser(COMMANDS_LIST['ADD'])
    checkParser = clientParser.add_parser(COMMANDS_LIST['CHECK'])
    deleteParser = clientParser.add_parser(COMMANDS_LIST['DELETE'])

    # Add arguments to parsers
    addParser.add_argument('description')
    checkParser.add_argument('id')
    deleteParser.add_argument('id')

    args = client.parse_args()

    data = None

    if checkExistCoulerFolder():
        data = readContent()
    else:
        data = []

    if args.command == COMMANDS_LIST['INIT']: init()
    if args.command == COMMANDS_LIST['ADD']: add(args.description, data)
    if args.command == COMMANDS_LIST['LOG']: log(data)
    if args.command == COMMANDS_LIST['CHECK']: check(args.id, data)
    if args.command == COMMANDS_LIST['DELETE']: delete(args.id, data)
