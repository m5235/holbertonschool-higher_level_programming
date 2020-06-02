#!/usr/bin/python3
"""
MyInt
"""


class MyInt(int):
    """
    subsclass of my int
    """
    def __eq__(self, other):
        """
        return not equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """

        """
        return super().__eq__(other)
