#!/usr/bin/python3
"""Defines a text-indentation function."""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indent = False
    for c in text:
        if c in ".?:":
            print(c)
            print()
            indent = True
        elif c == " " and indent:
            continue
        else:
            print(c, end="")
            indent = False

