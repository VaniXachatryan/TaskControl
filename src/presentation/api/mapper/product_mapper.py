from src.application.common.results.product_result import ProductResult
from src.presentation.api.schemas.product_scheme import ProductScheme


def product_result_to_product_scheme(result: ProductResult) -> ProductScheme:
    return ProductScheme(
        code=result.code,
        batch_number=result.batch_number,
        batch_date=result.batch_date,
    )
