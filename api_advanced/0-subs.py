#!/usr/bin/python3
"""Module for number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    Returns 0 if subreddit is invalid or if request fails.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'alu-scripting:v1.0 (by /u/yourusername)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get('data', {}).get('subscribers', 0)
        else:
            return 0
    except Exception:
        return 0
