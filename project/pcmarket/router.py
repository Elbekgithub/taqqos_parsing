from fastapi import APIRouter

from pcmarket.category import parse_category
from pcmarket.product import parse_product
from services import get_all_categories

router = APIRouter()


@router.get('/category')
def parse_category_pcmarket():
    parse_category.delay()
    return {"detail": "Ok"}


@router.get('/product')
def parse_product_pcmarket():
    data = [category.url for category in get_all_categories(website="pcmarket")]
    parse_product.delay(data)
    return {"detail": "Ok"}
