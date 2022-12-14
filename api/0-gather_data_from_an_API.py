#!/usr/bin/python3
"api"

import requests
from sys import argv


if __name__ == "__main__":
    completed = 0
    totalTasks = 0

    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    name = user.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
