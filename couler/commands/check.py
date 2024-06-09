from ..core import writeFile

def check(id:str, data:list):
    for item in data:
        if item['id'] == id:
            item['status'] = True
    
    writeFile(data)
    print('\n' + '\033[97m' + 'Task completed successfully 🌝' + '\033[0m')