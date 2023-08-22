#!/usr/bin/python3
"""
In this Module we're exporting to a JSON using API's
"""
import json
import requests
import sys


def export_employee_todo_to_json(employee_id):
    """
    Gets and displays Employee's progress
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    todo_response = requests.get("f{base_url}/todos?userId={employee_id}")

    if user_response.status_code != 200 or todo_response.status_code != 200:
        print("Error: Unable to fetch data form the API")
        return
    user_data = user_response.json()
    todo_data = user_response.json()

    employee_name = user_data["name"]
    todo_list = []
    for task in todo_data:
        todo_list.append([
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        ])

    result = {"USER_ID": todo_list}

    print(json.dumps(result, indent=4))

    json_filename = f"{employee_id}.json"
    with open(json_filename, "w") as json_file:
        json.dump(result, json_file, indent=4)

    print(f"JSON file '{json_filename}' created successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]
    export_employee_todo_to_json(employee_id)
