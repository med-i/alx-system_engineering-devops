#!/usr/bin/python3
"""
This module exports to CSV
"""

import csv
import requests
from sys import argv


def export_todos_to_csv(id):
    """Exports data in the CSV format"""
    api_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{api_url}/users/{id}"
    todos_url = f"{user_url}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    user_name = user["name"]
    file_name = f"{id}.csv"

    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                [id, user_name, task.get("completed"), task.get("title")]
            )


if __name__ == "__main__":
    if len(argv) >= 2:
        export_todos_to_csv(argv[1])
