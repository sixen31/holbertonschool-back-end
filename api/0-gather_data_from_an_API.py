#!/usr/bin/python3
"""ID d'employé donné renvoie toutes ses tâches à faire"""

import requests
import sys

if __name__ == "__main__":
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                         sys.argv[1], timeout=5)
    names = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         sys.argv[1], timeout=5)

    json_todo = to_do.json()
    json_names = names.json()

    all_tasks = 0
    tasks_completed = 0

    titles_completed = []
    for task in json_todo:
        all_tasks += 1
        if task["completed"]:
            tasks_completed += 1
            titles_completed.append(task["title"])

    employee_name = json_names['name']
    employee_id = sys.argv[1]

    # Formatting the first line correctly
    first_line = "Employee {} is done with tasks({}/{}):".format(
        employee_name, tasks_completed, all_tasks)
    formatted_first_line = first_line[:26] + "OK" if len(first_line) == 26 else "Incorrect"

    print(formatted_first_line)

    for title_task in titles_completed:
        print('\t{}'.format(title_task))
