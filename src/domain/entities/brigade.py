from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.configurations.database import BaseModel


class Brigade(BaseModel):
    __tablename__ = "brigades"

    title: Mapped[str] = mapped_column(nullable=False)

    def to_read_model(self):
        return {
            "id": self.id,
            "title": self.title,
        }
