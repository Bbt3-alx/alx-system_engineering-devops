#!/usr/bin/python3
"""Retrieve employee TODO list progress and export to CSV"""


import csv
import requests
import sys


def get_employee_name(employee_id):
    """Get employee name"""
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('name'), user_data.get('username')
    else:
        return None, None


def get_todo_list(employee_id):
    """Get employee TODO list"""
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def main(employee_id):
    """main function"""
    employee_name, employee_username = get_employee_name(employee_id)
    if not employee_name:
        return

    todo_list = get_todo_list(employee_id)

    # Write to csv file
    file_name = f"{employee_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            emp_id = employee_id
            emp_u = employee_username
            writer.writerow([emp_id, emp_u, task["completed"], task["title"]])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            main(employee_id)
        except ValueError:
            print("Please provide a valid integer as the employee ID.")
