#!/usr/bin/python3
"""
This module exports to JSON
"""

import json
import requests


def export_all_todos_to_json():
    """Exports data in the JSON format"""
    api_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{api_url}/users"

    users = requests.get(users_url).json()
    all_todos = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos_url = f"{api_url}/todos?userId={user_id}"
        todos = requests.get(todos_url).json()
        user_todos = []
        for task in todos:
            user_todos.append(
                {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                }
            )
        all_todos[user_id] = user_todos

    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(all_todos, file)


if __name__ == "__main__":
    export_all_todos_to_json()
