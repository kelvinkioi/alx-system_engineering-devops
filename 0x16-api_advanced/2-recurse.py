#!/usr/bin/python3
"""
 recursive function that queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    recursive function that queries the Reddit API andreturns
    alist containing the titles of all hot articles for a subreddit
    """
    endpoint = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after}
    header = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(endpoint, headers=header, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    res = response.json()
    after = res.get('data').get("after")
    for child in res.get('data').get("children"):
        hot_list.append(child.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
