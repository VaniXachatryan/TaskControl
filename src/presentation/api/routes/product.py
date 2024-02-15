from fastapi import APIRouter, status, Response
from returns.result import Success, Failure

from src.application.common.results.product_result import ProductResult
from src.domain.common.errors.batch_errors import BatchErrors
from src.domain.common.errors.product_errors import ProductErrors
from src.presentation.api.common.models.error_response import ErrorResponse
from src.presentation.api.depends import ProductServiceDepend
from src.presentation.api.mapper.product_mapper import product_result_to_product_scheme
from src.presentation.api.schemas.product_scheme import ProductSchemeAdd

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/create", status_code=200)
async def create(product_service: ProductServiceDepend, scheme: ProductSchemeAdd, response: Response):
    result: ProductResult = await product_service.add(code=scheme.code,
                                                      batch_number=scheme.batch_number,
                                                      batch_date=scheme.batch_date)

    match result:
        case Success(value):
            return product_result_to_product_scheme(value)
        case Failure(ProductErrors.is_exist):
            response.status_code = status.HTTP_409_CONFLICT
            return ErrorResponse(status_code=409, detail="Продукт с таким кодом уже существует.")
        case Failure(BatchErrors.not_found):
            response.status_code = status.HTTP_404_NOT_FOUND
            return ErrorResponse(status_code=404, detail="Партии с такими параметрами не существует.")


@router.patch("/aggregate", status_code=200)
async def add(product_service: ProductServiceDepend, batch_id: int, product_code: str, response: Response):
    result: ProductResult = await product_service.aggregate(code=product_code, batch_id=batch_id)

    match result:
        case Success(value):
            return "Aggregated!"
        case Failure([ProductErrors.not_found]):
            response.status_code = status.HTTP_404_NOT_FOUND
            return ErrorResponse(status_code=404, detail="Код продукта не найден.")
        case Failure([ProductErrors.code_attached_to_another_batch]):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return ErrorResponse(status_code=400, detail="unique code is attached to another batch")
        case Failure([ProductErrors.is_aggregated, value]):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return ErrorResponse(status_code=400, detail=f"unique code already used at {value}")
