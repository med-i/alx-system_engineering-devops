#!/usr/bin/python3
"""
This module exports to JSON
"""

import json
import requests
from sys import argv


def export_todos_to_json(id):
    """Exports data in the JSON format"""
    api_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{api_url}/users/{id}"
    todos_url = f"{user_url}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user["username"]
    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        for task in todos
    ]

    tasks_json = {id: tasks}
    filename = f"{id}.json"

    with open(filename, "w") as file:
        json.dump(tasks_json, file)


if __name__ == "__main__":
    if len(argv) >= 2:
        export_todos_to_json(argv[1])
