#!/usr/bin/python3
"""Module for Task 0"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number
    of subscribers to the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "My-User-Agent"}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()

    if response.status_code >= 300:
        return 0

    return data.get("data").get("subscribers")
   
