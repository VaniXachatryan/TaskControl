from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from src.presentation.api.schemas.batch_scheme import BatchScheme
from src.presentation.api.schemas.brigade_scheme import BrigadeScheme
from src.presentation.api.schemas.line_scheme import LineScheme
from src.presentation.api.schemas.shift_scheme import ShiftScheme
from src.presentation.api.schemas.work_center_scheme import WorkCenterScheme


class TaskScheme(BaseModel):
    is_closed: bool
    title: str
    line: LineScheme
    shift: ShiftScheme
    brigade: BrigadeScheme
    batch: BatchScheme
    nomenclature: str
    ekn_code: str
    work_center: WorkCenterScheme


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
