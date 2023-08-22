#!/usr/bin/python3
"""
module to get employees to do progress
"""
import csv
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

    employee_id = user_data["id"]
    employee_name = user_data["name"]
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])
    completed_tasks_titles = [task["titile"]
                              for task in todo_data if task["completed"]]

    print(
        f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):"
    )
    for title in completed_tasks_titles:
        print(f"\t{title}")

    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                            "TASK_TITLE"])

        for task in todo_data:
            task_completed_status = "Completed" if task["completed"]else "Not Completed"
            csv_writer.writerow(
                [employee_id, employee_name, task_completed_status, task["title"]])

    print(f"CSV file '{csv_filename}' created successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./employee_todo_progress.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
