#!/usr/bin/python3
"""
module to get employees to do progress
"""
import csv
import requests


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
    employee_id = 'EMPLOYEE_ID'
    get_employee_todo_progress(employee_id)
