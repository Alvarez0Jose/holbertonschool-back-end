#!/usr/bin/python3
"""
module to get employees to do progress
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    function to obtain employee information
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")

    if user_response.status_code != 200 or todo_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        return

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data["name"]
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])
    completed_tasks_titles = [task["title"]
                              for task in todo_data if task["completed"]]

    print(
        f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for title in completed_tasks_titles:
        print(f"\t{title}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./employee_todo_progress.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
