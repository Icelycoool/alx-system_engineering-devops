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
        headers={"User-Agent": "Custom"},
        allow_redirects=False
    )

    if req.status_code == 200:
        return req.json().get("data", {}).get("subscribers", 0)
    else:
        return 0
