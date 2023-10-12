#!/usr/bin/python3
"""script that export data to json"""
from sys import argv
import requests
import json


if __name__ == '__main__':

    user_id = int(argv[1])
    users_response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    todos_response = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))
    employee_name = ''

    if users_response.status_code == 200 and todos_response.status_code == 200:
        users = users_response.json()
        todos = todos_response.json()

        if users['id'] == user_id:
            employee_name = users['username']

        filename = f'{user_id}.json'
        user_dict = {user_id: []}

        for info in todos:
            dict = {
                'task': info['title'], 'completed': info['completed'],
                'username': employee_name}
            user_dict.get(user_id).append(dict)

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(user_dict, f)
