from typing import Any
from fastapi import status
from app.common.statics.status_codes import StatusCodesScheme


class Failure(Exception):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail: str = "UNKNOWN"
    headers: dict = None

    def __init__(self, status_code: int = None, detail: Any = None, headers: dict = None) -> None:
        if status_code:
            self.status_code = status_code 
        if detail:
            self.detail = detail
        if headers:
            self.headers = headers


class BadRequest(Failure):
    status_code = 400
    detail = StatusCodesScheme.HTTP_400_BAD_REQUEST.value

class Unauthorized(Failure):
    status_code = 401
    detail = StatusCodesScheme.HTTP_401_UNAUTHORIZED.value

class PaymentRequired(Failure):
    status_code = 402
    detail = StatusCodesScheme.HTTP_402_PAYMENT_REQUIRED.value

class Forbidden(Failure):
    status_code = 403
    detail = StatusCodesScheme.HTTP_403_FORBIDDEN.value

class NotFound(Failure):
    status_code = 404
    detail = StatusCodesScheme.HTTP_404_NOT_FOUND.value

class MethodNotAllowed(Failure):
    status_code = 405
    detail = StatusCodesScheme.HTTP_405_METHOD_NOT_ALLOWED.value

class NotAcceptable(Failure):
    status_code = 406
    detail = StatusCodesScheme.HTTP_406_NOT_ACCEPTABLE.value

class ProxyAuthenticationRequired(Failure):
    status_code = 407
    detail = StatusCodesScheme.HTTP_407_PROXY_AUTHENTICATION_REQUIRED.value

class RequestTimeout(Failure):
    status_code = 408
    detail = StatusCodesScheme.HTTP_408_REQUEST_TIMEOUT.value

class Conflict(Failure):
    status_code = 409
    detail = StatusCodesScheme.HTTP_409_CONFLICT.value

class Gone(Failure):
    status_code = 410
    detail = StatusCodesScheme.HTTP_410_GONE.value

class LengthRequired(Failure):
    status_code = 411
    detail = StatusCodesScheme.HTTP_411_LENGTH_REQUIRED.value

class PreconditionFailed(Failure):
    status_code = 412
    detail = StatusCodesScheme.HTTP_412_PRECONDITION_FAILED.value

class RequestEntityTooLarge(Failure):
    status_code = 413
    detail = StatusCodesScheme.HTTP_413_REQUEST_ENTITY_TOO_LARGE.value

class RequestUriTooLong(Failure):
    status_code = 414
    detail = StatusCodesScheme.HTTP_414_REQUEST_URI_TOO_LONG.value

class UnsupportedMediaType(Failure):
    status_code = 415
    detail = StatusCodesScheme.HTTP_415_UNSUPPORTED_MEDIA_TYPE.value

class RequestedRangeNotSatisfiable(Failure):
    status_code = 416
    detail = StatusCodesScheme.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE.value

class ExpectationFailed(Failure):
    status_code = 417
    detail = StatusCodesScheme.HTTP_417_EXPECTATION_FAILED.value

class ImATeapot(Failure):
    status_code = 418
    detail = StatusCodesScheme.HTTP_418_IM_A_TEAPOT.value

class MisdirectedRequest(Failure):
    status_code = 421
    detail = StatusCodesScheme.HTTP_421_MISDIRECTED_REQUEST.value

class UnprocessableEntity(Failure):
    status_code = 422
    detail = StatusCodesScheme.HTTP_422_UNPROCESSABLE_ENTITY.value

class Locked(Failure):
    status_code = 423
    detail = StatusCodesScheme.HTTP_423_LOCKED.value

class FailedDependency(Failure):
    status_code = 424
    detail = StatusCodesScheme.HTTP_424_FAILED_DEPENDENCY.value

class TooEarly(Failure):
    status_code = 425
    detail = StatusCodesScheme.HTTP_425_TOO_EARLY.value

class UpgradeRequired(Failure):
    status_code = 426
    detail = StatusCodesScheme.HTTP_426_UPGRADE_REQUIRED.value

class PreconditionRequired(Failure):
    status_code = 428
    detail = StatusCodesScheme.HTTP_428_PRECONDITION_REQUIRED.value

class TooManyRequests(Failure):
    status_code = 429
    detail = StatusCodesScheme.HTTP_429_TOO_MANY_REQUESTS.value

class RequestHeaderFieldsTooLarge(Failure):
    status_code = 431
    detail = StatusCodesScheme.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE.value

class UnavailableForLegalReasons(Failure):
    status_code = 451
    detail = StatusCodesScheme.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS.value

class InternalServerError(Failure):
    status_code = 500
    detail = StatusCodesScheme.HTTP_500_INTERNAL_SERVER_ERROR.value

class NotImplemented(Failure):
    status_code = 501
    detail = StatusCodesScheme.HTTP_501_NOT_IMPLEMENTED.value

class BadGateway(Failure):
    status_code = 502
    detail = StatusCodesScheme.HTTP_502_BAD_GATEWAY.value

class ServiceUnavailable(Failure):
    status_code = 503
    detail = StatusCodesScheme.HTTP_503_SERVICE_UNAVAILABLE.value

class GatewayTimeout(Failure):
    status_code = 504
    detail = StatusCodesScheme.HTTP_504_GATEWAY_TIMEOUT.value

class HttpVersionNotSupported(Failure):
    status_code = 505
    detail = StatusCodesScheme.HTTP_505_HTTP_VERSION_NOT_SUPPORTED.value

class VariantAlsoNegotiates(Failure):
    status_code = 506
    detail = StatusCodesScheme.HTTP_506_VARIANT_ALSO_NEGOTIATES.value

class InsufficientStorage(Failure):
    status_code = 507
    detail = StatusCodesScheme.HTTP_507_INSUFFICIENT_STORAGE.value

class LoopDetected(Failure):
    status_code = 508
    detail = StatusCodesScheme.HTTP_508_LOOP_DETECTED.value

class NotExtended(Failure):
    status_code = 510
    detail = StatusCodesScheme.HTTP_510_NOT_EXTENDED.value

class NetworkAuthenticationRequired(Failure):
    status_code = 511
    detail = StatusCodesScheme.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED.value
