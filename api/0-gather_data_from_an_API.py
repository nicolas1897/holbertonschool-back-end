#!/usr/bin/python3
''' Return information about his/her TODO list progress from an REST API '''
from requests import get
from sys import argv


def api_rest():
    ''' Gather data from an API '''
    id_user = int(argv[1])
    name_employe = ''
    number_task = 0
    total_number_task = 0
    list_task = []

    url_users = get('https://jsonplaceholder.typicode.com/users').json()
    for user in url_users:
        if user['id'] == id_user:
            name_employe = user['name']
            break

    url_task = get('https://jsonplaceholder.typicode.com/todos').json()
    for task in url_task:
        if task['userId'] == id_user:
            if task['completed'] is True:
                list_task.append(task['title'])
                number_task += 1
            total_number_task += 1
    print('Employee {} is done with tasks({}/{}):'.format(name_employe,
                                                          number_task,
                                                          total_number_task))
    for title in list_task:
        print('\t {}'.format(title))


if __name__ == '__main__':
    api_rest()
