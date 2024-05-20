from abc import abstractmethod
from typing import Tuple, Any
from app.common.responses.failures import Failure


class BaseUseCase:
    @abstractmethod
    async def execute(self, *args, **kwargs) -> Tuple[Any, Failure]:
        raise NotImplementedError()
