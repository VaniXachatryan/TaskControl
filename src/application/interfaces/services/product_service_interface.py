from abc import ABC, abstractmethod

from returns.result import Result


class IProductService(ABC):
    @abstractmethod
    async def add(self, code: str, batch_number: int, batch_date) -> Result:
        pass

    @abstractmethod
    async def aggregate(self) -> Result:
        pass
