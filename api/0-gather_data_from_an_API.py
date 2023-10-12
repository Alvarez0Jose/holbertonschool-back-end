#!/usr/bin/python3
"""Script that return info from an API"""
import requests
from sys import argv


if __name__ == '__main__':
    """script that count amount of task completed"""
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    users_api = requests.get(url_users)
    todos_api = requests.get(url_todos)
    task_title = []
    number_of_done_task = 0
    total_number_of_tasks = 0
    employee_name = ""
    id_employee = int(argv[1])

    if users_api.status_code == 200 and todos_api.status_code == 200:
        users = users_api.json()
        todos = todos_api.json()

        for user in users:
            if user['id'] == id_employee:
                employee_name = user['name']

                for task in todos:
                    if task['userId'] == id_employee:
                        total_number_of_tasks += 1
                        if task['completed'] is True:
                            number_of_done_task += 1
                            task_title.append(task['title'])

        print("Employee {} is done with task({}/{}):"
              .format(employee_name, number_of_done_task,
                      total_number_of_tasks))

        for task_printed in task_title:
            print(f"\t {task_printed}")
