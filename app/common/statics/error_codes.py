import enum


class ErrorCodesScheme(enum.Enum):
    """
    Enum representing the error codes of API.
    """
    TIMEOUT = "TIMEOUT"
    UNKNOWN = "UNKNOWN"
    UNAUTHORIZE = "UNAUTHORIZED"
    NOT_FOUND = "NOT_FOUND"
    FORBIDDEN = "FORBIDDEN"
    EXISTED = "EXISTED"
    BAD_REQUEST = "BAD_REQUEST"
    UNPROCESSABLE = "UNPROCESSABLE_CONTENT"
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    INVALID_INPUT = "INVALID_INPUT"
    REQUEST_TIMEOUT = "REQUEST_TIMEOUT"
