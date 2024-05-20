import typing
from app.common.statics.error_codes import ErrorCodesScheme


class Failure(Exception):
    code: int = 500
    error_code: str = ErrorCodesScheme.UNKNOWN.value
    message: typing.Any = "Server Failure. If you see this, it's backend's fault!"

    def __init__(self, message: typing.Any, error_code: str = None) -> None:
        self.message = message
        if error_code:
            self.error_code = error_code


class BadRequest(Failure):
    code = 400
    error_code = ErrorCodesScheme.BAD_REQUEST.value


class Unauthorized(Failure):
    code = 401
    error_code = ErrorCodesScheme.UNAUTHORIZE.value


class NotFound(Failure):
    code = 404
    error_code = ErrorCodesScheme.NOT_FOUND.value


class Forbidden(Failure):
    code = 403
    error_code = ErrorCodesScheme.FORBIDDEN.value


class RequestTimeout(Failure):
    code = 408
    error_code = ErrorCodesScheme.REQUEST_TIMEOUT.value


class Conflict(Failure):
    code = 409
    error_code = ErrorCodesScheme.EXISTED.value


class Unprocessable(Failure):
    code = 422
    error_code = ErrorCodesScheme.UNPROCESSABLE.value


class InternalServerError(Failure):
    code = 500
    error_code = ErrorCodesScheme.INTERNAL_SERVER_ERROR.value
