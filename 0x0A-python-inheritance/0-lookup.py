!#/usr/bin/python3


# Function that returns the list of available attributes and methods of an object.

def lookup(obj):
    """ Returns a list of available attributes and methods of an object."""
    attrs = dir(obj)
