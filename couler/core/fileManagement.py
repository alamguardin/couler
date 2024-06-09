import json

def readContent():
    return json.loads(open('.couler/data.json', 'r').read())

def writeFile(data:list):
    file = open('.couler/data.json', 'w')
    file.write(json.dumps(data))