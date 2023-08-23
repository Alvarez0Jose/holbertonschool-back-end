#!/usr/bin/python3
"""
This Module gets all the employees progress
"""
import json
import requests
import sys


def get_all_employees_todo_progress():
    """
    Funtion to get progress per employee
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(base_url)

    if users_response.status_code != 200:
        print("Error: Unable to fetch user data from the API.")
        return

    all_employee_data = {}

    user_data = users_response.json()

    for user in users_data:
        user_id = user["id"]
        username = user["username"]

        todo_response = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")

        if todo_response.status_code != 200:
            print(
                f"Error: Unable to fetch TODO data for user {username} from the API.")
            continue

        todo_data = todo_response.json()

        user_task = []
        for task in todo_data:
            user_tasks.append({
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            })

            all_employee_data[user_id] = user_tasks

        return all_employee_data

    if __name__ == "__main__":
        all_employee_tasks = get_all_employees_todo_progress()

        if not all_employee_tasks:
            sys.exit(1)

        json_filename = "todo_all_employees.json"
        with open(json_filename, "w") as json_file:
            json.dump(all_employee_tasks, json_file, indent=4)

        print(f"JSON file '{json_filename}' created successfully.")
