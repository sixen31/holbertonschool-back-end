#!/usr/bin/python3
""" renvoie ses tâches à faire et les exporte au format CSV"""

import csv
import requests
import sys

if __name__ == "__main__":
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                         sys.argv[1], timeout=5)
    names = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         sys.argv[1], timeout=5)

    json_todo = to_do.json()
    json_names = names.json()

    with open('{}.csv'.format(sys.argv[1]), mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in json_todo:
            writer.writerow([sys.argv[1], json_names['username'],
                             task['completed'], task['title']])
