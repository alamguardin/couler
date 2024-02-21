from ast import arg
from operator import ne
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
        'id': secrets.token_hex(4)
    }

    projects.append(newProject)

def createTask(projectReference:str, description:str):
    newTask = {
        'description': description,
        'reference': projectReference,
        'id': secrets.token_hex(4),
        'index': len(tasks) + 1,
        'status': False
    }

    tasks.append(newTask)

def deleteProject(id:str):
    index = 0
    newTasks = []
    for project in projects:
        if (project['id'] == id):

            indexTask = 0
            for task in tasks:
                if (task['reference'] != project['name']):
                    newTasks.append(task)
                indexTask += 1

            break
        index += 1
    
    projects.pop(index)
    tasks.clear()
    tasks.extend(newTasks)

def deleteTask(projectReference:str, id:str):
    index = 0
    for task in tasks:
        if (task['reference'] == projectReference and task['id'] == id):
            tasks.pop(index)
            break

        index += 1

def updateProjectName(id:str, name:str):
    index = 0
    previusName = ''
    for project in projects:
        if (project['id'] == id):
            previusName = projects[index]['name']
            projects[index]['name'] = name

            indexTask = 0
            for task in tasks:
                if (task['reference'] == previusName):
                    tasks[index]['reference'] = name
            
            indexTask += 1

            break

        index += 1

def updateTaskStatus(projectReference:str, id:str):
    index = 0
    for task in tasks:
        if (task['reference'] == projectReference and task['id'] == id):
            tasks[index]['status'] = not tasks[index]['status']
            break

        index += 1
 
if __name__ == '__main__':
    projectsFile = open('projects.json', 'r+')
    tasksFile = open('tasks.json', 'r+')

    projects = json.loads(projectsFile.read())
    tasks = json.loads(tasksFile.read())

    arguments = sys.argv

    # Create new project or task
    if (arguments[1] == 'create'):
        if (arguments[2] == 'project'):
            try:
                createProject(arguments[3])
                resetFile(projectsFile)
                projectsFile.write(json.dumps(projects))
                print('Proyecto creado con exito')
            except:
                print('Ohh, algo salio mal...')
        elif (arguments[2] == 'task'):
            try:
                createTask(arguments[3], arguments[4])
                resetFile(tasksFile)
                tasksFile.write(json.dumps(tasks))
                print('Tarea creada con exito')
            except:
                print('Ohh, algo salio mal...')
    
    # Remove project or task
    if (arguments[1] == 'remove'):
        if (arguments[2] == 'project'):
            deleteProject(arguments[3])
            resetFile(projectsFile)
            resetFile(tasksFile)
            projectsFile.write(json.dumps(projects))
            tasksFile.write(json.dumps(tasks))
        elif (arguments[2] == 'task'):
            deleteTask(arguments[3], arguments[4])
            resetFile(tasksFile)
            tasksFile.write(json.dumps(tasks))

    # Update project name o status class
    if (arguments[1] == 'update'):
        if (arguments[2] == 'project'):
            updateProjectName(arguments[3], arguments[4])
            resetFile(projectsFile)
            resetFile(tasksFile)
            projectsFile.write(json.dumps(projects))
            tasksFile.write(json.dumps(tasks))
        if (arguments[2] == 'task'):
            updateTaskStatus(arguments[3], arguments[4])
            resetFile(tasksFile)
            tasksFile.write(json.dumps(tasks))
