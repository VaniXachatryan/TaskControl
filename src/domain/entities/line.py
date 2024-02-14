from sqlalchemy.orm import mapped_column, Mapped

from src.domain.common.base_model import BaseModel


class Line(BaseModel):
    __tablename__ = "lines"

    code: Mapped[str] = mapped_column(nullable=False)

    def to_read_model(self):
        return Line(
            id=self.id,
            code=self.code
        )
