from typing import Optional, List
import uuid

from eshop.business_logic.product import Product
from eshop.data_access import product_repo


def product_create(dto) -> Product:
    product = Product(
        id=str(uuid.uuid4()),
        name=dto["name"],
        price=dto["price"]
    )
    product_repo.save(product)
    return product


def product_get_by_id(id: str) -> Optional[Product]:
    return product_repo.get_by_id(id)


def product_get_many(page: int, limit: int) -> List[Product]:
    return product_repo.get_many(page, limit)
