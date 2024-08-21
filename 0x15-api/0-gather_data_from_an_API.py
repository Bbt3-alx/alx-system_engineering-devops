#!/usr/bin/python3
"""Retrieve employee TODO list progresi"""


import requests
import sys


def get_employee_name(employee_id):
    """Get employee name"""
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('name')
    else:
        return None

def get_todo_list(employee_id):
    """Get employee TODO list"""
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    if response.status_code == 200:
        return response.json()
    else:
        return []

def main(employee_id):
    """Main function"""
    employee_name = get_employee_name(employee_id)
    if not employee_name:
        print(f"Employee with ID {employee_id} not found.")
        return

    todo_list = get_todo_list(employee_id)
    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task["completed"]]

    completed = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks ({completed}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            main(employee_id)
        except ValueError:
           print("Please provide a valide integer as the employee ID.")
