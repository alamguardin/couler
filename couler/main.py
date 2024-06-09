# core modules
# from couler.core.addCoreFolder import checkExistCoulerFolder
# from couler.core.fileManagement import readContent
# from couler.utils.commandsList import COMMANDS_LIST
# from couler.commands.init import init
# from couler.commands.add import add
# from couler.commands.log import log
# from couler.commands.check import check
# from couler.commands.delete import delete

from .core import checkExistCoulerFolder
from .core import readContent
from .utils import COMMANDS_LIST
from .commands import init
from .commands import add
from .commands import log
from .commands import check
from .commands import delete

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
