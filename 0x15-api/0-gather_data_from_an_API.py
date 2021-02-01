#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

Attributes:
    argv[1](int): The employee ID.

"""
import requests
from sys import argv

if __name__ == '__main__':
    # querys to bring the data of the tasks and employee name
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    employee = requests.get('https://jsonplaceholder.typicode.com/users/' +
                            argv[1])

    # convert the text response to json format
    employee_dict = employee.json()
    todos_dict = todos.json()

    # get the nedded data
    userName = employee_dict.get('name')
    body = [items.get("title") for items in todos_dict
            if items.get("userId") == int(argv[1]) and
            items.get("completed") is True]
    ready = [items.get("completed") for items in todos_dict
             if items.get("userId") == int(argv[1])]

    # print the results
    print('Employee {} is done with tasks({}/{}):'
          .format(userName, sum(ready), len(ready)))
    for message in body:
        print('\t {}'.format(message))
