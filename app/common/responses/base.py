from typing import Any, Optional
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.common.responses.failures import Failure
from app.common.utils.converters.datetime_converter import DatetimeConverter
from fastapi.responses import JSONResponse
from fastapi import BackgroundTasks, Query, status, HTTPException


def to_camel(string: str) -> str:
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])

json_encoders = {datetime: DatetimeConverter.format_utc_str, UUID: lambda x: str(x)}

class BaseSchema(BaseModel):
    class Config:
        from_attributes = True
        ignore_extra = True
        populate_by_name = True
        alias_generator = to_camel
        json_encoders = json_encoders


class BaseResponseModel(BaseSchema):
    status_code: int = status.HTTP_200_OK
    detail: str = "OK"
    data: Any | None = None

    class Config:
        use_enum_values = True


class BaseResponse(JSONResponse):
    def __init__(
        self,
        content: Any,
        status_code: int = status.HTTP_200_OK,
        headers: Optional[dict] = None,
        cookies: Optional[dict] = None,
        cookie_domain: Optional[str] = None,
        media_type: Optional[str] = None,
        background: Optional[BackgroundTasks] = None,
    ) -> None:
        if isinstance(content, BaseResponseModel):
            status_code = content.status_code
            content = content.model_dump(exclude_none=True, by_alias=True)
        elif isinstance(content, Failure):
            raise HTTPException(
                status_code=content.status_code,
                detail=content.detail,
                headers=content.headers
            )

        super().__init__(content, status_code, headers, media_type, background)
        if cookies:
            for k, v in cookies.items():
                self.set_cookie(key=k, value=v, domain=cookie_domain, secure=True, httponly=False)
