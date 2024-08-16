#!/usr/bin/python3
"""Api advanced """


import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Recursively counts keywords in the titles
    of all hot articles in a subreddit
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
                title = post.get('data', {}).get('title', '').lower().split()
                for w in word_list:
                    c = title.count(w.lower())
                    if c > 0:
                        word_count[w.lower()] = word_count.get(w.lower(), 0) + c

            # Check if there is another page of results
            after = data.get('data', {}).get('after')
            if after:
                # Recursive call to get the next page of results
                return count_words(subreddit, word_list, word_count, after)
            else:
                # Sort and print the results
                sorted_w_c = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_w_c:
                    print(f"{word}: {count}")
        else:
            # If the subreddit is invalid or another error occurred
            return
    except requests.RequestException:
        # In case of a network or other request-related error
        return
