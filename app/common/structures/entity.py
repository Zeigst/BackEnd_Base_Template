from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Union, Optional


@dataclass(init=False, kw_only=True)
class BaseEntity(object):
    def to_json(self, keys=None) -> Dict:
        return {
            k: v
            for k, v in self.__dict__.items()
            if "__" not in k and (keys is None or k in keys)
        }
