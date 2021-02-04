#!/usr/bin/python3
""" bring all the suscriber form reddit"""

def number_of_subscribers(subreddit):
    """Querie returns the number of subscribers
    to the subreddit"""
    import requests
    
    subs = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if subs.status_code >= 300:
        return 0

    return subs.json().get("data").get("subscribers")
