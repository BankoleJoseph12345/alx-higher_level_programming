#!/usr/bin/python3
"""Save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Object to txt file using JSON"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
