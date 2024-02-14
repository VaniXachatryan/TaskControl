from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.domain.common.base_model import BaseModel
from src.domain.entities.batch import Batch


class Product(BaseModel):
    __tablename__ = 'products'

    code: Mapped[str] = mapped_column(unique=True)
    batch_id: Mapped[int] = mapped_column(ForeignKey(Batch.id))

    batch: Mapped[Batch] = relationship(Batch, lazy="joined")

    def to_read_model(self):
        return Product(
            id=self.id,
            code=self.code,
            batch=self.batch)
