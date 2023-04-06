#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])

    try:
        m = requests.get(url)
        m.raise_for_status()
        commits = m.json()
        for commit in commits[:10]:
            print("{}: {}".format(
                commit.get("sha"),
                commit.get("commit").get("author").get("name")))
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
    except (KeyError, IndexError):
        print("Error: Invalid response from API")
