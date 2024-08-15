#!/usr/bin/python3
"""Module for Task 0"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number
    of subscribers to the subreddit.
    """
    req = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers={"User-Agent": "subreddit.subscriber.count:v1.0"},
            allow_redirects=False,
    )

    if req.status_code == 200:
        data = req.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
