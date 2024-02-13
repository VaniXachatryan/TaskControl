from dataclasses import dataclass
from typing import List, Optional

from src.application.common.results.batch_result import BatchResult
from src.application.common.results.brigade_result import BrigadeResult
from src.application.common.results.line_result import LineResult
from src.application.common.results.shift_result import ShiftResult
from src.application.common.results.work_center_result import WorkCenterResult


@dataclass
class TaskResult:
    id: int
    is_closed: bool
    title: str
    line: LineResult
    shift: ShiftResult
    brigade: BrigadeResult
    batch: BatchResult
    nomenclature: str
    ekn_code: str
    work_center: WorkCenterResult


@dataclass
class TaskResultWithProductIdsResult:
    id: int
    is_closed: bool
    title: str
    line: LineResult
    shift: ShiftResult
    brigade: BrigadeResult
    batch: BatchResult
    nomenclature: str
    ekn_code: str
    work_center: WorkCenterResult
    products: List[int]
