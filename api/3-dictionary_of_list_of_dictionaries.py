#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress and
export the data in the JSON format.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/users/{}/todos"
    user_id = sys.argv[1]
    response = requests.get(url.format(user_id)).json()
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()

    tasks = []
    for task in response:
        new_task = {}
        new_task["task"] = task["title"]
        new_task["completed"] = task["completed"]
        new_task["username"] = user["username"]
        tasks.append(new_task)

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: tasks}, jsonfile)
