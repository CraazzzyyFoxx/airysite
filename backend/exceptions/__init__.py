class APIError(Exception):
    """Base API error"""


class UnauthorizedError(APIError):
    """Raises when user not authorized"""
    pass

