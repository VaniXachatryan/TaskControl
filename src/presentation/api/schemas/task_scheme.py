from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

from src.presentation.api.schemas.batch_scheme import BatchScheme
from src.presentation.api.schemas.brigade_scheme import BrigadeScheme
from src.presentation.api.schemas.line_scheme import LineScheme
from src.presentation.api.schemas.shift_scheme import ShiftScheme
from src.presentation.api.schemas.work_center_scheme import WorkCenterScheme


class TaskScheme(BaseModel):
    id: int
    is_closed: bool
    title: str
    line: str
    shift: str
    brigade: str
    batch: int
    nomenclature: str
    ekn_code: str
    work_center: str


class TaskWithProductIdsScheme(TaskScheme):
    products: List[int]


class TaskSchemeAdd(BaseModel):
    is_closed: bool = Field(False, alias="СтатусЗакрытия")
    title: str = Field(alias="ПредставлениеЗаданияНаСмену")
    line_code: str = Field(alias="Линия")
    shift: str = Field(alias="Смена")
    brigade: str = Field(alias="Бригада")
    batch_number: int = Field(alias="НомерПартии")
    batch_date: datetime = Field(alias="ДатаПартии")
    nomenclature: str = Field(alias="Номенклатура")
    ekn_code: str = Field(alias="КодЕКН")
    work_center_code: str = Field(alias="ИдентификаторРЦ")
    shift_start_date: datetime = Field(alias="ДатаВремяНачалаСмены")
    shift_end_date: Optional[datetime] = Field(alias="ДатаВремяОкончанияСмены")


class TaskSchemeUpdate(BaseModel):
    is_closed: Optional[bool] = Field(default=None)
    title: Optional[str] = Field(default=None)
    line_code: Optional[str] = Field(default=None)
    shift: Optional[str] = Field(default=None)
    brigade: Optional[str] = Field(default=None)
    batch_number: Optional[int] = Field(default=None)
    batch_date: Optional[datetime] = Field(default=None)
    nomenclature: Optional[str] = Field(default=None)
    ekn_code: Optional[str] = Field(default=None)
    work_center_code: Optional[str] = Field(default=None)
    shift_start_date: Optional[datetime] = Field(default=None)
    shift_end_date: Optional[datetime] = Field(default=None)
