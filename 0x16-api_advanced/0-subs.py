#!/usr/bin/python3
"""
This module defines the number_of_subscribers method.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a subreddit."""
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "linux:alx:v1.0.0 (by /u/I-Med)"}

    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
