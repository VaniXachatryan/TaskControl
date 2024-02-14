from sqlalchemy.orm import Mapped

from src.domain.common.base_model import BaseModel


class WorkCenter(BaseModel):
    __tablename__ = "work_centers"

    code: Mapped[str]

    def to_read_model(self):
        return WorkCenter(
            id=self.id,
            code=self.code
        )