#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv


def my_request():
    url = 'https://jsonplaceholder.typicode.com'
    user_response = requests.get(url + '/users/' + argv[1]).json()
    todos_response = requests.get(url + '/todos?userId=' + argv[1]).json()
    tasks_done = [todo['title'] for todo in todos_response if todo['completed']]
    print('Employee {} is done with tasks({}/{}):'
          .format(user_response['name'], len(tasks_done), len(todos_response)))
    [print('\t {}'.format(title)) for title in tasks_done]


if __name__ == '__main__':
    my_request()
