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
    users = requests.get('https://jsonplaceholder.typicode.com/users/')

    # convert the text response to json format
    users_dict = users.json()
    res_lst = []
    res_dict = {}
    for user in users_dict:
        todo = requests.get('https://jsonplaceholder.typicode.com/users/' +
                            str(user.get("id")) + '/todos')
        todo_dict = todo.json()
        for todo in todo_dict:
            res_lst.append({"username": user.get('username'),
                            'task': todo.get('title'),
                            'completed': todo.get('completed')})
        res_dict[str(user.get('id'))] = res_lst
        res_lst = []
    # write to a file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(res_dict, f)
