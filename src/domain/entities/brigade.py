from sqlalchemy.orm import Mapped, mapped_column

from src.domain.common.base_model import BaseModel


class Brigade(BaseModel):
    __tablename__ = "brigades"

    title: Mapped[str] = mapped_column(nullable=False)

    def to_read_model(self):
        return Brigade(
            id=self.id,
            title=self.title
        )
