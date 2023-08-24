#!/usr/bin/python3
"""ID d'employé donné renvoie toutes ses tâches à faire et les exporte au format JSON"""

import json
import requests
import sys


if __name__ == "__main__":
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                         sys.argv[1], timeout=5)
    names = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         sys.argv[1], timeout=5)

    json_todo = to_do.json()
    json_names = names.json()

    tasks = []
    for task in json_todo:
        task_dict = {}
        task_dict["task"] = task["title"]
        task_dict["completed"] = task["completed"]
        task_dict["username"] = json_names["username"]
        tasks.append(task_dict)

    json_dict = {}
    json_dict[sys.argv[1]] = tasks

    with open('{}.json'.format(sys.argv[1]), mode='w') as f:
        json.dump(json_dict, f)
