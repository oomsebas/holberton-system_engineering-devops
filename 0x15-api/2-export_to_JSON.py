#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    # querys to bring the data of the tasks and employee name
    todos = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         argv[1] + '/todos/')
    employee = requests.get('https://jsonplaceholder.typicode.com/users/' +
                            argv[1])
    # convert the text response to json format
    employee_dict = employee.json()
    todos_dict = todos.json()
    res = []
    # create the first part of the dictionary
    for items in todos_dict:
        res.append({'task': items.get('title'),
                    'completed': items.get('completed'),
                    "username": employee_dict.get("username")})
    to_json = {argv[1]: res}
    # write to a file
    with open(argv[1] + '.json', 'w') as f:
        json.dump(to_json, f)
