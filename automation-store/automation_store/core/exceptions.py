
class ServiceResourceDoesNotExistException(Exception):
    """Raised when a resource does not exist."""

    def __init__(self, resource_name) -> None:
        self.message = f"{resource_name} not found."
        super().__init__(self.message)
