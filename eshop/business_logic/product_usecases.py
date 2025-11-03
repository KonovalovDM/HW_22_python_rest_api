from typing import Optional, List

from eshop.business_logic.product import Product
from eshop.data_access import product_repo


# Глобальный счётчик ID — следующий ID продукта
_next_product_id = len(product_repo.get_many(0, 100000)) + 1


def product_create(dto) -> Product:
    global _next_product_id

    product = Product(
        id=str(_next_product_id),
        name=dto["name"],
        price=dto["price"]
    )

    _next_product_id += 1
    product_repo.save(product)
    return product


def product_get_by_id(id: str) -> Optional[Product]:
    return product_repo.get_by_id(id)


def product_get_many(page: int, limit: int) -> List[Product]:
    return product_repo.get_many(page, limit)

