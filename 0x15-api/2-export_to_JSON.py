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
    user_response = requests.get(url + '/users/' + argv[1]).json()['username']
    todos_response = requests.get(url + '/todos?userId=' + argv[1]).json()

    record = {}
    data = {}
    grp = []
    for todo in todos_response:
        record['task'] = todo['title']
        record['completed'] = todo['completed']
        record['username'] = user_response
        grp.append(record)
        record = {}

    data[argv[1]] = grp
    with open('{}.json'.format(argv[1]), 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    my_request()
