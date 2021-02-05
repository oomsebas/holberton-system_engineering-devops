#!/usr/bin/python3
""" hat queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""


def top_ten(subreddit):
    """
    query the 10 hot post from reddit according to argv
    """
    import requests

    hot_pst = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                           .format(subreddit),
                           headers={"User-Agent": "My-User-Agent"},
                           allow_redirects=False)
    hot_pst_json = hot_pst.json()
    if hot_pst.status_code >= 300:
        print('None')
    else:
        [print(post.get("data").get("title"))
         for post in hot_pst_json.get("data").get("children")]
