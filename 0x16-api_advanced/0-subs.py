#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number
    of subscribers.

    Args:
        subreddit: The subreddit to be fetched
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data'].get('subscribers', 0)
        print(subscribers)
    else:
        return 0
