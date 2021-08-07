class Error(Exception):
    """Base class for other exceptions"""
    pass

class ArraySizeError(Error):
    pass

class VoidReturnError(Error):
    pass

class ReturnEmpty(Error):
    pass

class ReturnNotEmpty(Error):
    pass