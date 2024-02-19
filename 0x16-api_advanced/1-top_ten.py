#!/usr/bin/python3
"""
This module defines top_ten method.
"""

import requests


def top_ten(subreddit):
    """Prints the 10 first titles of hot posts listed for a given subreddit."""
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "linux:alx:v1.0.0 (by /u/I-Med)"}

    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
    else:
        data = response.json().get("data").get("children")
        for post in data[:10]:
            print(post.get("data").get("title"))
