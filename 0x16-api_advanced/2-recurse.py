#!/usr/bin/python3
"""Module for Task 2"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    A recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given
    subreddit, the function should return None.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
            "User-Agent: "Custom"
    }
