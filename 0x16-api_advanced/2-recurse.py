#!/usr/bin/python3
"""Module for Task 2"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    A recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given
    subreddit, the function should return None.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
            "User-Agent": "custom"
    }

    params = {
            "after": after,
            "count": count,
            "limit": 100
    }

    req = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)

    if req.status_code == 404:
        return None

    result = req.json().get("data")
    after = result.get("after")
    count += result.get("dist")

    for i in result.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
