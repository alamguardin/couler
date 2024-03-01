import array
from ast import arg
from operator import ne
import sys
import json
import secrets
import datetime

COMMANDS_LIST = ['create', 'delete', 'update', 'list']
OPTIONS_LIST = ['project', 'task']

class Cli:
    def __init__(self):
        self.commands = []
        self.options = []
        self.projects = []
        self.tasks = []
        self.projects_file = None
        self.tasks_file = None
    # Private Methods
    def __writeFile(self, file, content):
        file.truncate(0)
        file.seek(0)
        file.write(content)
    
    def __readFile(self, file, saveIn):
        content = json.loads(file.read())
        if saveIn == 'Projects': self.projects = content
        if saveIn == 'Tasks': self.tasks = content

    # Public Methods
    def add_command(self, command):
        if len(command) > 0:
            self.commands.append(command)
        else:
            print('cannot add empty text string as command')
    
    def add_projects_file(self, file):
        self.projects_file = file
        self.__readFile(file, 'Projects')
    
    def add_tasks_file(self, file):
        self.tasks_file = file
        self.__readFile(file, 'Tasks')
    
    def check_exist_project(self, id):
        for project in self.projects:
            if project['id'] == id:
                return True
        
        return False

    def create_project(self, name):
        if len(name) > 0:
            new_project = {
                'create-at': str(datetime.datetime.now()),
                'id': secrets.token_hex(4),
                'name': name
            }

            self.projects.append(new_project)
            self.__writeFile(self.projects_file, json.dumps(self.projects))
        else:
            print('Can\'t add empty string as project name')

    def create_task(self, description, id_reference):
        if len(description) > 0:
            new_task = {
                'create-at': str(datetime.datetime.now()),
                'reference': id_reference,
                'id': secrets.token_hex(4),
                'description': description,
                'status': False
            }
            self.tasks.append(new_task)
            self.__writeFile(self.tasks_file, json.dumps(self.tasks))
        else:
            print('Can\'t add empty string as task description')

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

def showProjects():
    print('Id' + '  ' + 'Name')
    print('--' + '  ' + '----')
    for project in projects:
        print(project['id'] + ' ' + project['name'])
 

def showTasks():
    print('Id' + '  ' + 'Description' + '   ' + 'Status' + '    ' + 'Reference')
    print('----' + '    ' + '-----------' + '   ' + '------' + '    ' + '---------')
    for task in tasks:
        print(task['id'] + '    ' + task['description'] + ' ' + str(task['status']) + '  ' + task['reference'])

if __name__ == '__main__':
    cli = Cli()

    # Add commands to Cli
    for command in COMMANDS_LIST:
        cli.add_command(command)
    
    # Set files to Cli
    cli.add_projects_file(open('projects.json', 'r+'))
    cli.add_tasks_file(open('tasks.json', 'r+'))
    
    # Get commands from cmd
    commands = sys.argv

    if commands[1] == 'create' and commands[2] == 'project':
        while(True):
            project_name = input('Choose a name for your project -> ')
            if len(project_name) > 0:
                cli.create_project(project_name)
                print('\nCongratulations! You have created a new project ✨')
                break 
            else:
                print('Please write something in the text field')
                continue
    
    if commands[1] == 'create' and commands[2]  == 'task':
        try:
            id_project = commands[3]
            if cli.check_exist_project(id_project):
                while(True):
                    task_description = input('Write a description for your task -> ')
                    if len(task_description) > 0:
                        cli.create_task(task_description, id_project)
                        print('\nTask created successfully ✨')
                        break 
                    else:
                        print('Please write something in the text field')
                        continue
        except IndexError:
            print('You must add the project id to assign a task')
    # projectsFile = open('projects.json', 'r+')
    # tasksFile = open('tasks.json', 'r+')

    # projects = json.loads(projectsFile.read())
    # tasks = json.loads(tasksFile.read())

    # arguments = sys.argv

    # # Create new project or task
    # if (arguments[1] == 'create'):
    #     if (arguments[2] == 'project'):
    #         try:
    #             createProject(arguments[3])
    #             resetFile(projectsFile)
    #             projectsFile.write(json.dumps(projects))
    #             print('Proyecto creado con exito')
    #         except:
    #             print('Ohh, algo salio mal...')
    #     elif (arguments[2] == 'task'):
    #         try:
    #             createTask(arguments[3], arguments[4])
    #             resetFile(tasksFile)
    #             tasksFile.write(json.dumps(tasks))
    #             print('Tarea creada con exito')
    #         except:
    #             print('Ohh, algo salio mal...')
    
    # # Remove project or task
    # if (arguments[1] == 'remove'):
    #     if (arguments[2] == 'project'):
    #         deleteProject(arguments[3])
    #         resetFile(projectsFile)
    #         resetFile(tasksFile)
    #         projectsFile.write(json.dumps(projects))
    #         tasksFile.write(json.dumps(tasks))
    #     elif (arguments[2] == 'task'):
    #         deleteTask(arguments[3], arguments[4])
    #         resetFile(tasksFile)
    #         tasksFile.write(json.dumps(tasks))

    # # Update project name o status class
    # if (arguments[1] == 'update'):
    #     if (arguments[2] == 'project'):
    #         updateProjectName(arguments[3], arguments[4])
    #         resetFile(projectsFile)
    #         resetFile(tasksFile)
    #         projectsFile.write(json.dumps(projects))
    #         tasksFile.write(json.dumps(tasks))
    #     if (arguments[2] == 'task'):
    #         updateTaskStatus(arguments[3], arguments[4])
    #         resetFile(tasksFile)
    #         tasksFile.write(json.dumps(tasks))
    
    # # Show projects or tasks list
    # if (arguments[1] == 'show'):
    #     if (arguments[2] == 'projects'):
    #         showProjects()
    #     if (arguments[2] == 'tasks'):
    #         showTasks()