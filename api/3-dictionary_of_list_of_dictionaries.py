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

    try:
        response = requests.get(url.format(user_id)).json()
        user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(user_id)).json()
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

    if not response:
        print("No tasks found for the user.")
        sys.exit(0)

    tasks = []
    for task in response:
        new_task = {}
        new_task["task"] = task["title"]
        new_task["completed"] = task["completed"]
        new_task["username"] = user["username"]
        tasks.append(new_task)

    try:
        with open("{}.json".format(user_id), "w") as jsonfile:
            json.dump({user_id: tasks}, jsonfile, default=str)
    except IOError:
        print("Error writing to the file.")
        sys.exit(1)
