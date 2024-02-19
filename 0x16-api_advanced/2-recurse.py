#!/usr/bin/python3
"""
This module defines recurse method.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list of titles of all hot articles for a given subreddit."""
    headers = {"User-Agent": "linux:alx:v1.0.0 (by /u/I-Med)"}
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        api_url += f"&after={after}"

    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        hot_list.append(post["data"]["title"])
    after = data["data"]["after"]
    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
