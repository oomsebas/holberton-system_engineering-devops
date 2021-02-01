#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
 data in the CSV format.
"""
import csv
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
    for items in todos_dict:
        res.append([items.get('userId'), employee_dict.get('username'),
                    items.get('completed'), items.get('title')])
    with open(argv[1]+".csv", "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(res)
