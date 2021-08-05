class Error(Exception):
    """Base class for other exceptions"""
    pass

class ArraySizeError(Error):
    print("Error")

class VoidReturnError(Error):
    print("asdf")