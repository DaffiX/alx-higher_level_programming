#!/usr/bin/python3
"""Sends a Request then.
Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    meg = requests.get(url)
    if meg.status_code >= 400:
        print("Error code: {}".format(meg.status_code))
    else:
        print(meg.text)
