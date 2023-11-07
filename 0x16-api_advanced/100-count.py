#!/usr/bin/python3
"""
recursive function that queries the Reddit API
"""
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    """
    ecursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a sorted
    count of given keywords (case-insensitive, delimited byspaces
    Javascript should count as javascript, but java should not)
    """
    user_agent = {'User-agent': '6k'}
    res = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                       .format(subreddit, after), headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if res.status_code == 200:
        res = res.json()['data']
        aft = res['after']
        res = res['children']
        for r in res:
            title = r['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
