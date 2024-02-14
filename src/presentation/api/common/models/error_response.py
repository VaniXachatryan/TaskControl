from dataclasses import dataclass


@dataclass
class ErrorResponse:
    status_code: int
    detail: str
