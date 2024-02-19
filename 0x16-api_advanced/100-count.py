#!/usr/bin/python3
"""
This module defines count_words method.
"""

import re
import requests


def count_words(subreddit, word_list, after="", word_counts=None):
    """Count words in hot articles of a subreddit."""
    if word_counts is None:
        word_counts = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {"User-Agent": "linux:alx:v1.0.0 (by /u/I-Med)"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        title = post["data"]["title"].lower()
        for word in word_list:
            word = word.lower()
            word_counts[word] += len(
                re.findall(r"\b" + re.escape(word) + r"\b", title)
            )

    after = data["data"]["after"]
    if after is not None:
        count_words(subreddit, word_list, after, word_counts)
    else:
        sorted_words = sorted(
            [word for word in word_counts if word_counts[word] > 0],
            key=lambda w: (-word_counts[w], w),
        )
        for word in sorted_words:
            print(f"{word}: {word_counts[word]}")
