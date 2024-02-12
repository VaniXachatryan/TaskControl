from sqlalchemy.orm import Mapped

from src.infrastructure.configurations.database import BaseModel


class WorkCenter(BaseModel):
    __tablename__ = "work_centers"

    code: Mapped[str]

    def to_read_model(self):
        return {
            "id": self.id,
            "title": self.title,
            "code": self.code
        }