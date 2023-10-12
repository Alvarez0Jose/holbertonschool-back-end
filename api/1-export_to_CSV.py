#!/usr/bin/python3
"""Script that export data in CSV format"""
from sys import argv
import requests
import csv


def employee_info():
    """function that return info of employee"""
    USER_ID = int(argv[1])
    EMPLOYEE_NAME = ""
    task_obj = []

    url_users = requests.get('https://jsonplaceholder.typicode.com/users')
    url_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    if url_users.status_code == 200 and url_todos.status_code == 200:
        users_info = url_users.json()
        todos_info = url_todos.json()

        for user in users_info:
            if user['id'] == USER_ID:
                EMPLOYEE_NAME = user['username']

                for todo in todos_info:
                    if todo['userId'] == USER_ID:
                        task_obj.append(todo)

        csv_export(USER_ID, EMPLOYEE_NAME, task_obj)


def csv_export(USER_ID, EMPLOYEE_NAME, task_obj):
    """Exports the employee info to csv"""
    filename = "{}.csv".format(USER_ID)

    with open(filename, mode='w', newline='') as csvfile:
        csv_wrt = csv.writer(csvfile, delimiter=',',
                             quotechar='"', quoting=csv.QUOTE_ALL)

        for info in task_obj:
            csv_wrt.writerow(
                [USER_ID, EMPLOYEE_NAME, info['completed'], info['title']])


if __name__ == '__main__':
    employee_info()
