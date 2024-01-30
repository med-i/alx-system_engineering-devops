#!/usr/bin/python3
"""
This module gather data from an API
"""

import sys
import requests


def get_employee_todos(id):
    """Returns information about employee TODO list progress"""
    api_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{api_url}/users/{id}"
    todos_url = f"{user_url}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    user_name = user["name"]
    completed = [
        task.get("title") for task in todos if task.get("completed") is True
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_name, len(completed), len(todos)
        )
    )

    for task in completed:
        print(f"\t{task}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_employee_todos(sys.argv[1])
