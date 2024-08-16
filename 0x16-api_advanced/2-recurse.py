#!/usr/bin/python3
"""Api advanced"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns
    a list of hot article titles.
    """
    # Set up the URL and headers
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    p = {'limit': 100}  # Maximum limit per request is 100

    # Add the 'after' parameter to handle pagination
    if after:
        p['after'] = after

    try:
        # Make the request to the Reddit API
        resp = requests.get(url, headers=headers, p=p, allow_redirects=False)

        # Check if the request was successful
        if resp.status_code == 200:
            # Parse the JSON response
            data = resp.json()
            # Extract the list of posts
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                # Append each post title to the hot_list
                hot_list.append(post.get('data', {}).get('title'))

            # Check if there is another page of results
            after = data.get('data', {}).get('after')
            if after:
                # Recursive call to get the next page of results
                return recurse(subreddit, hot_list, after)
            else:
                # Return the accumulated list of titles
                return hot_list if hot_list else None
        else:
            # If the subreddit is invalid or another error occurred
            return None
    except requests.RequestException:
        # In case of a network or other request-related error
        return None
