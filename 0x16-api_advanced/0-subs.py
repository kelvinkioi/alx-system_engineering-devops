#!/usr/bin/python3
'''
function that queries the Reddit API
'''
import requests


def number_of_subscribers(subreddit):
    '''
    function that queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers) for a given
    subreddit.
    If an invalid subreddit is given, the function should return 0
    '''
    endpoint = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(endpoint, headers=headers)

    if response.status_code != 200:
        return 0
    return response.json()['data']['subscribers']
