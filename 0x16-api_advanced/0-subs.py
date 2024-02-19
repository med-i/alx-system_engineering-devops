#!/usr/bin/python3
"""
This module defines the number_of_subscribers method.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a subreddit."""
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        "User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/med-i)"
    }

    try:
        response = requests.get(
            api_url, headers=headers, allow_redirects=False
        )

        if response.status_code == 200:
            data = response.json()
            print(data)
            return data["data"]["subscribers"]
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
