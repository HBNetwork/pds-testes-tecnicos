from decimal import Decimal

import pytest

from automation_store.core.domain import Shirt
from automation_store.core.exceptions import ServiceResourceDoesNotExistException
from automation_store.core.services import ShirtService


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
    with pytest.raises(ServiceResourceDoesNotExistException):
        service.get(pk=123)


def test_create_a_shirt():
    shirt = Shirt(
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

    assert service.delete(2) is None


def test_fail_remove_shirt_not_found():
    service = ShirtService()
    with pytest.raises(ServiceResourceDoesNotExistException):
        service.delete(123)


def test_update_a_shirt():
    service = ShirtService()
    result = service.update(
        id=1,
        size="M",
        color="Yellow",
        brand="ZaraMF",
        price=Decimal(130),
    )

    assert result.size == "M"
    assert result.color == "Yellow"
    assert result.brand == "ZaraMF"
    assert result.price == Decimal(130)


def test_update_a_shirt_not_found():
    service = ShirtService()

    with pytest.raises(ServiceResourceDoesNotExistException):
        service.update(
            id=123,
            size="M",
            color="Yellow",
            brand="ZaraMF",
            price=Decimal(130),
        )


def test_partially_update_a_shirt():
    service = ShirtService()
    original = service.get(pk=1)
    shirt = {
        "id": 1,
        "color": "Yellow",
        "brand": "ZaraMF",
    }

    result = service.update(
        id=1,
        color="Yellow",
        brand="ZaraMF",
    )

    assert original.size == result.size
    assert original.price == result.price

    assert result.color == "Yellow"
    assert result.brand == "ZaraMF"
