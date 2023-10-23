#!/usr/bin/python3
"""
using task 0, extending the Python script to export data
in the CSV format
"""
import csv
import requests
from sys import argv


def my_request():
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + '/users/' + argv[1]).json()['username']
    todos_response = requests.get(url + '/todos?userId=' + argv[1]).json()
    with open('{}.csv'.format(argv[1]), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_response:
            writer.writerow([argv[1], user, todo['completed'], todo['title']])


if __name__ == '__main__':
    my_request()
