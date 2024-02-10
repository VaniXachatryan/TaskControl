from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: int
    line_id:int
    name: str
    is_closed: bool
    closed_at: datetime
    work_center_id: int
    shift_id: int
    brigade_id: int
    batch_id: int
    nomenclature: str
    ekn_code: str


class TaskSchemaAdd(BaseModel):
    is_closed: bool
    title: str
    work_center: str
    shift: str
    brigade: str
    batch_number: int
    batch_date: datetime
    nomenclature: str
    ekn_code: str
    work_center_id: int
    shift_start_date: datetime
    shift_end_date: Optional[datetime] = None
