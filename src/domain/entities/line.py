from sqlalchemy.orm import mapped_column, Mapped

from src.infrastructure.configurations.database import BaseModel


class Line(BaseModel):
    __tablename__ = "lines"

    code: Mapped[str] = mapped_column(nullable=False)

    def to_read_model(self):
        return {
            "id": self.id,
            "code": self.code
        }
