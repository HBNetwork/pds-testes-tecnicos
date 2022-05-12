
class ServiceResourceNotFoundException(Exception):
    """Raised when the input value is too small"""

    def __init__(self, resource_name) -> None:
        self.message = f"{resource_name} not found."
        super().__init__(self.message)
