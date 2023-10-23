#!/usr/bin/python3
"""
Using task #0, extending the Python script to export
data in the JSON format
"""
import json
import requests
from sys import argv


def my_request():
    url = 'https://jsonplaceholder.typicode.com'
    user_response = requests.get(url + '/users/').json()
    todos_response = requests.get(url + '/todos/').json()

    i = 0
    record = []
    id = user_response[i]['id']
    user = user_response[i]['username']
    all = {}

    for todo in todos_response:
        if todo['userId'] != id:
            all[id] = record
            i += 1
            id, user = user_response[i]['id'], user_response[i]['username']
            record = []
        record.append(
                {'username': user, 'task': todo['title'],
                    'completed': todo['completed']})

    all[id] = record
    with open('todo_all_employees.json', 'w') as file:
        json.dump(all, file)


if __name__ == '__main__':
    my_request()
