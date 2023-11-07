#!/usr/bin/python3
'''prints titles of first 10 hot posts listed for a given subreddit'''
import requests


def top_ten(subreddit):
    '''
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
    '''
    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(endpoint,
                            headers={'User-Agent': 'My User Agent 1.0'},
                            allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    response = response.json()['data']['children']
    if len(response) == 0:
        print("None")
        return
    for r in response:
        print(r['data']['title'])
