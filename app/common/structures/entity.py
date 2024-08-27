from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional


@dataclass(init=False, kw_only=True)
class BaseEntity(object):
    def to_json(self, keys=None) -> Dict:
        return {
            k: v
            for k, v in self.__dict__.items()
            if "__" not in k and (keys is None or k in keys)
        }


@dataclass(init=False, kw_only=True)
class CommonEntity(BaseEntity):
    id: Optional[int] = None
    is_deleted: bool = False
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
