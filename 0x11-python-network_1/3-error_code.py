#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""

import urllib.request

url = input("Enter a URL: ")

with urllib.request.urlopen(url) as response:
    print(response.read().decode("utf-8"))
    
