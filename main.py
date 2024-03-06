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
    
    def __check_exist_project(self, id):
        index = 0
        for project in self.projects:
            if project['id'] == id:
                return index, True
            index += 1
        
        return -1, False
    
    def __check_exits_task(self, id):
        index = 0
        for task in self.tasks:
            if task['id'] == id:
                return index, True
            index += 1
        
        return -1, False
    

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
    
    def exist_project(self, id):
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
    
    def get_projects_list(self):
        return self.projects
    
    def get_tasks_list(self):
        return self.tasks
    
    def update_task_status(self, id_task):
        index, is_found = self.__check_exits_task(id_task)
        if is_found:
            self.tasks[index]['status'] = not self.tasks[index]['status']
            print('Task updated successfully')
        else:
            print('This task does not exist, make sure you enter an existing ID')
        
        self.__writeFile(self.tasks_file, json.dumps(self.tasks))
    
    def delete_project(self, id):
        index, is_found = self.__check_exist_project(id)
        if is_found:
            self.projects.pop(index)
            
            tasks = []
            for task in self.tasks:
                if task['reference'] != id:
                    tasks.append(task)
            
            self.tasks = tasks

            print('Successful project deletion')
        else:
            print('This project does not exist, make sure to enter an existing ID')
        
        self.__writeFile(self.projects_file, json.dumps(self.projects))
        self.__writeFile(self.tasks_file, json.dumps(self.tasks))
    
    def delete_task(self, id):
        index, is_found = self.__check_exits_task(id)
        if is_found:
            self.tasks.pop(index)
            print('Successful task deletion')
        else:
            print('This task does not exist, make sure you enter an existing ID')
        
        self.__writeFile(self.tasks_file, json.dumps(self.tasks))

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
            if cli.exist_project(id_project):
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
    
    if commands[1] == 'list' and commands[2] == 'project':
        list_projects = cli.get_projects_list()
        for project in list_projects:
            print(project['id'] + '     ' + project['name'] + '     ' + project['create-at'].split()[0])
    
    if commands[1] == 'list' and commands[2] == 'task':
        list_tasks = cli.get_tasks_list()
        for task in list_tasks:
            print(task['id'] + '      ' + task['description'] + '       ' + str(task['status']))
    
    if commands[1] == 'update' and commands[2] == 'task':
        try:
            id_task = commands[3]
            cli.update_task_status(id_task)
        except IndexError:
             print('You must add the task id to change its status')
    
    if commands[1] == 'delete' and commands[2] == 'project':
        try:
            id_project = commands[3]
            cli.delete_project(id_project)
        except IndexError:
            print('You must add an id to delete a project')
    
    if commands[1] == 'delete' and commands[2] == 'task':
        try:
            id_task = commands[3]
            cli.delete_task(id_task)
        except IndexError:
            print('You must add an id to delete a task')
