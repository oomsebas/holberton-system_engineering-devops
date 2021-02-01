#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

Attributes:
    argv[1](int): The employee ID.

"""
import requests
from sys import argv

# querys to bring the data of the tasks and employee name
todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
employee = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1])

# convert the text response to json format
employee_dict = employee.json()
todos_dict = todos.json()

# get the nedded data
userName = employee_dict['name']
body = [items["title"] for items in todos_dict
        if items["userId"] == int(argv[1]) and
        items["completed"] is True]
ready = [items["completed"] for items in todos_dict
         if items["userId"] == int(argv[1])]

# print the results
print('Employee {} is done with tasks({}/{})'
      .format(userName, sum(ready), len(ready)))
for message in body:
    print('\t {}'.format(message))
