#!/usr/bin/python3
"""
A module Prints the titles of the first 10 hot posts listed
for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """

    # Set up the URL and headers
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the list of posts
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print(None)
            else:
                # Print the titles of the first 10 hot posts
                for post in posts:
                    print(post.get('data', {}).get('title'))
        else:
            # If the subreddit is invalid or another error occurred
            print(None)
    except requests.RequestException:
        # In case of a network or other request-related error
        print(None)
