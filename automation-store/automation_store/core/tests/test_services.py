from decimal import Decimal

import pytest

from ..domain import Shirt
from ..exceptions import ServiceResourceNotFoundException
from ..services import ShirtService


def test_list_all_shirt():
    service = ShirtService()
    shirts = service.list()

    assert len(shirts) == 2


def test_get_shirt_by_id():
    service = ShirtService()
    shirt = service.get(pk=1)

    assert shirt != None


def test_fail_get_shirt_not_found():
    service = ShirtService()
    with pytest.raises(ServiceResourceNotFoundException):
        service.get(pk=123)


def test_create_a_shirt():
    shirt = Shirt(
        id=3,
        size="M",
        color="black",
        brand="ZaraMF",
        price=Decimal(50),
    )

    service = ShirtService()
    result = service.create(shirt)

    assert result == shirt


def test_remove_a_shirt():

    service = ShirtService()
    result = service.delete(2)

    assert result == None


def test_fail_remove_shirt_not_found():
    service = ShirtService()
    with pytest.raises(ServiceResourceNotFoundException):
        service.delete(123)


def test_update_a_shirt():
    shirt = {
        "size": "M",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": Decimal(130),
    }

    service = ShirtService()
    result = service.update(1, shirt)

    assert shirt["size"] == result.size
    assert shirt["color"] == result.color
    assert shirt["brand"] == result.brand
    assert shirt["price"] == result.price


def test_update_a_shirt_not_found():
    shirt = {
        "size": "M",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": Decimal(130),
    }

    service = ShirtService()

    with pytest.raises(ServiceResourceNotFoundException):
        service.update(123, shirt)


def test_partially_update_a_shirt():
    service = ShirtService()
    original = service.get(pk=1)
    shirt = {
        "color": "Yellow",
        "brand": "ZaraMF",
    }

    result = service.update(1, shirt)

    assert original.size == result.size
    assert original.price == result.price

    assert shirt["color"] == result.color
    assert shirt["brand"] == result.brand
