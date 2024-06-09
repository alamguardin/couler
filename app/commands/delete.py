from core.fileManagement import writeFile

def delete(id:str, data:list):
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
        writeFile(data)
    
    print('\n' + '\033[97m' + 'Task deleted successfully 🔥' + '\033[0m')