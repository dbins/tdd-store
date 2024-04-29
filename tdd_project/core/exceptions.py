from typing import Optional
class BaseException(Exception):
    message: str = "Internal Server Error"

    def __init__(self, message: Optional[str] = None) -> None:
        if message:
            self.message = message


class NotFoundException(BaseException):
    message = "Not Found"