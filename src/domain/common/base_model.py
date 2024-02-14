from abc import abstractmethod

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class BaseModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @abstractmethod
    def to_read_model(self):
        pass
