from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.common.utils.converters.datetime_converter import DatetimeConverter


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
