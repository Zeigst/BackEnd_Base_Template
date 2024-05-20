from app.common.statics.error_codes import ErrorCodesScheme


class BaseException(Exception):
    status_code: int

    def __init__(
        self,
        message: str = "Unknown Error!",
        error_code: str = ErrorCodesScheme.UNKNOWN.value,
        status_code: int = 400,
    ):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code


class UnauthorizedException(BaseException):
    status_code = 401

    def __init__(self, message: str = "Unauthorized!"):
        error_code = ErrorCodesScheme.UNAUTHORIZE.value
        super().__init__(message, error_code, self.status_code)


class ForbiddenException(BaseException):
    status_code = 403

    def __init__(self, message: str = "Forbidden!"):
        error_code = ErrorCodesScheme.FORBIDDEN.value
        super().__init__(message, error_code, self.status_code)


class NotFoundException(BaseException):
    status_code = 404

    def __init__(self, message: str = "Not Found!"):
        error_code = ErrorCodesScheme.NOT_FOUND.value
        super().__init__(message, error_code, self.status_code)


class InvalidInputException(BaseException):
    status_code = 422

    def __init__(self, message: str = "Invalid Input!"):
        error_code = ErrorCodesScheme.INVALID_INPUT.value
        super().__init__(message, error_code)
