from rest_framework.exceptions import APIException


class ApiShirtDoesNotExist(APIException):
    """Raised when a shirt does not exist."""

    status_code = 404
    default_detail = "Shirt does not exist."
    default_code = "shirt_does_not_exist"


class ServiceShirtDoesNotExistException(Exception):
    """Raised when a Shirt does not exist."""
    pass
