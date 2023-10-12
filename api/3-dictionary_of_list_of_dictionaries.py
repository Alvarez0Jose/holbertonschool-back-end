#!/usr/bin/python3
"""Script that exports data to JSON"""
import requests
import json


if __name__ == '__main__':
    todo_dict = {}

    # Fetch user data
    users_api = requests.get('https://jsonplaceholder.typicode.com/users/')
    if users_api.status_code == 200:
        users = users_api.json()

        for user in users:
            user_id = user['id']
            user_todo_query = {'userId': user_id}
            todos_api = requests.get(
                'https://jsonplaceholder.typicode.com/todos',
                params=user_todo_query)

            if todos_api.status_code == 200:
                todo_list = todos_api.json()

                employee_name = user['username']
                tasks = []

                for todo in todo_list:
                    task = {'username': employee_name, 'task': todo['title'],
                            'completed': todo['completed']}
                    tasks.append(task)

                todo_dict[user_id] = tasks

        # Serializing to JSON
        json_object = json.dumps(todo_dict)

        # Writing to JSON file
        with open('todo-all_employees.json', 'w') as jsonfile:
            jsonfile.write(json_object)
