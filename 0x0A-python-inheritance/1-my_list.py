#!/usr/bin/python3
"""MyList that inherits from list"""


class MyList(list):
    """print sorted list"""

    def print_sorted(self):
        """print list, asceding order"""
        print(sorted(self))
