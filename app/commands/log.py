def log(data:list):
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