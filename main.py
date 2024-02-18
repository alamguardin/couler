import sys
import json
import secrets

tasks = []
projects = []

def resetFile(file):
    file.truncate(0)
    file.seek(0)

def createProject(name:str):
    newProject = {
        'name': name,
        'id': len(projects) + 1
    }

    projects.append(newProject)

def createTask(projectReference:str, description:str):
    newTask = {
        'description': description,
        'reference': projectReference,
        'id': secrets.token_hex(16),
        'index': len(tasks) + 1 
    }

    tasks.append(newTask)
    

if __name__ == '__main__':
    projectsFile = open('projects.json', 'r+')
    tasksFile = open('tasks.json', 'r+')

    projects = json.loads(projectsFile.read())
    tasks = json.loads(tasksFile.read())

    arguments = sys.argv

    # Create new project or task
    if (arguments[1] == 'create'):
        if (arguments[2] == 'project'):
            createProject(arguments[3])
            resetFile(projectsFile)
            projectsFile.write(json.dumps(projects))
        elif (arguments[2] == 'task'):
            createTask(arguments[3], arguments[4])
            resetFile(tasksFile)
            tasksFile.write(json.dumps(tasks))
