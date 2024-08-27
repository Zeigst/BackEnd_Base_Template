from typing import Any, Dict
from fastapi import HTTPException, status
from app.common.statics.status_codes import StatusCodesScheme


class HTTPExceptionBadRequest(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_400_BAD_REQUEST, 
        detail: Any = StatusCodesScheme.HTTP_400_BAD_REQUEST.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionUnauthorized(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_401_UNAUTHORIZED, 
        detail: Any = StatusCodesScheme.HTTP_401_UNAUTHORIZED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionPaymentRequired(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_402_PAYMENT_REQUIRED, 
        detail: Any = StatusCodesScheme.HTTP_402_PAYMENT_REQUIRED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionForbidden(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_403_FORBIDDEN, 
        detail: Any = StatusCodesScheme.HTTP_403_FORBIDDEN.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionNotFound(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_404_NOT_FOUND, 
        detail: Any = StatusCodesScheme.HTTP_404_NOT_FOUND.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionMethodNotAllowed(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_405_METHOD_NOT_ALLOWED, 
        detail: Any = StatusCodesScheme.HTTP_405_METHOD_NOT_ALLOWED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionNotAcceptable(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_406_NOT_ACCEPTABLE, 
        detail: Any = StatusCodesScheme.HTTP_406_NOT_ACCEPTABLE.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionProxyAuthenticationRequired(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED, 
        detail: Any = StatusCodesScheme.HTTP_407_PROXY_AUTHENTICATION_REQUIRED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionRequestTimeout(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_408_REQUEST_TIMEOUT, 
        detail: Any = StatusCodesScheme.HTTP_408_REQUEST_TIMEOUT.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionConflict(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_409_CONFLICT, 
        detail: Any = StatusCodesScheme.HTTP_409_CONFLICT.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionGone(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_410_GONE, 
        detail: Any = StatusCodesScheme.HTTP_410_GONE.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionLengthRequired(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_411_LENGTH_REQUIRED, 
        detail: Any = StatusCodesScheme.HTTP_411_LENGTH_REQUIRED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionPreconditionFailed(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_412_PRECONDITION_FAILED, 
        detail: Any = StatusCodesScheme.HTTP_412_PRECONDITION_FAILED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionRequestEntityTooLarge(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, 
        detail: Any = StatusCodesScheme.HTTP_413_REQUEST_ENTITY_TOO_LARGE.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionRequestURITooLong(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_414_REQUEST_URI_TOO_LONG, 
        detail: Any = StatusCodesScheme.HTTP_414_REQUEST_URI_TOO_LONG.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionUnsupportedMediaType(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, 
        detail: Any = StatusCodesScheme.HTTP_415_UNSUPPORTED_MEDIA_TYPE.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionRequestedRangeNotSatisfiable(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE, 
        detail: Any = StatusCodesScheme.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionExpectationFailed(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_417_EXPECTATION_FAILED, 
        detail: Any = StatusCodesScheme.HTTP_417_EXPECTATION_FAILED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionImATeapot(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_418_IM_A_TEAPOT, 
        detail: Any = StatusCodesScheme.HTTP_418_IM_A_TEAPOT.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionMisdirectedRequest(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_421_MISDIRECTED_REQUEST, 
        detail: Any = StatusCodesScheme.HTTP_421_MISDIRECTED_REQUEST.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionUnprocessableEntity(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY, 
        detail: Any = StatusCodesScheme.HTTP_422_UNPROCESSABLE_ENTITY.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionLocked(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_423_LOCKED, 
        detail: Any = StatusCodesScheme.HTTP_423_LOCKED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionFailedDependency(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_424_FAILED_DEPENDENCY, 
        detail: Any = StatusCodesScheme.HTTP_424_FAILED_DEPENDENCY.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionTooEarly(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_425_TOO_EARLY, 
        detail: Any = StatusCodesScheme.HTTP_425_TOO_EARLY.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionUpgradeRequired(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_426_UPGRADE_REQUIRED, 
        detail: Any = StatusCodesScheme.HTTP_426_UPGRADE_REQUIRED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionPreconditionRequired(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_428_PRECONDITION_REQUIRED, 
        detail: Any = StatusCodesScheme.HTTP_428_PRECONDITION_REQUIRED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionTooManyRequests(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_429_TOO_MANY_REQUESTS, 
        detail: Any = StatusCodesScheme.HTTP_429_TOO_MANY_REQUESTS.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionRequestHeaderFieldsTooLarge(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE, 
        detail: Any = StatusCodesScheme.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionUnavailableForLegalReasons(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, 
        detail: Any = StatusCodesScheme.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionInternalServerError(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR, 
        detail: Any = StatusCodesScheme.HTTP_500_INTERNAL_SERVER_ERROR.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionNotImplemented(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_501_NOT_IMPLEMENTED, 
        detail: Any = StatusCodesScheme.HTTP_501_NOT_IMPLEMENTED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionBadGateway(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_502_BAD_GATEWAY, 
        detail: Any = StatusCodesScheme.HTTP_502_BAD_GATEWAY.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionServiceUnavailable(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_503_SERVICE_UNAVAILABLE, 
        detail: Any = StatusCodesScheme.HTTP_503_SERVICE_UNAVAILABLE.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionGatewayTimeout(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_504_GATEWAY_TIMEOUT, 
        detail: Any = StatusCodesScheme.HTTP_504_GATEWAY_TIMEOUT.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionVersionNotSupported(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED, 
        detail: Any = StatusCodesScheme.HTTP_505_HTTP_VERSION_NOT_SUPPORTED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionVariantAlsoNegotiates(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_506_VARIANT_ALSO_NEGOTIATES, 
        detail: Any = StatusCodesScheme.HTTP_506_VARIANT_ALSO_NEGOTIATES.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionInsufficientStorage(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_507_INSUFFICIENT_STORAGE, 
        detail: Any = StatusCodesScheme.HTTP_507_INSUFFICIENT_STORAGE.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionLoopDetected(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_508_LOOP_DETECTED, 
        detail: Any = StatusCodesScheme.HTTP_508_LOOP_DETECTED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionNotExtended(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_510_NOT_EXTENDED, 
        detail: Any = StatusCodesScheme.HTTP_510_NOT_EXTENDED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class HTTPExceptionNetworkAuthenticationRequired(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED, 
        detail: Any = StatusCodesScheme.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED.value, 
        headers: Dict[str, str] | None = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)
