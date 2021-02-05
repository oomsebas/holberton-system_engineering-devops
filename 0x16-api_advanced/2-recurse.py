#!/usr/bin/python3
"""Task 2 recursion function"""


def recurse(subreddit, hot_lst=[], count=0, after=None):
    """Returns all hot posts
    of the subreddit"""
    import requests

    hot_art = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subreddit),
                           params={"count": count, "after": after},
                           headers={"User-Agent": "My-User-Agent"},
                           allow_redirects=False)
    if hot_art.status_code >= 400:
        return None

    res_lst = hot_lst + [art.get("data").get("title")
                         for art in hot_art.json()
                         .get("data")
                         .get("children")]

    mssg = hot_art.json()
    if not mssg.get("data").get("after"):
        return res_lst

    return recurse(subreddit, res_lst, mssg.get("data").get("count"),
                   mssg.get("data").get("after"))
