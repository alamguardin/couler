import sys
import json

tasks = []
projects = []

def createProject(name:str):
    newProject = {
        'name': name,
        'id': len(projects) + 1
    }

    projects.append(newProject)
    

if __name__ == '__main__':
    file = open('projects.json', 'r+')
    projects = json.loads(file.read())

    arguments = sys.argv

    # Create a new project
    if (arguments[1] == 'create' and arguments[2] == 'project'):
        createProject(arguments[3])
        file.truncate(0)
        file.seek(0)
        file.write(json.dumps(projects))

    print(projects)