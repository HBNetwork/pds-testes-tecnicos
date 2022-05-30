from decimal import Decimal

import pytest
from automation_store.core.domain import Shirt
from automation_store.core.exceptions import ServiceShirtDoesNotExistException
from automation_store.core.services import ShirtService


def test_list_all_shirt():
    shirts = ShirtService().list()

    assert len(shirts) == 2


def test_get_shirt_by_id():
    shirt = ShirtService().get(pk=1)

    assert shirt != None


def test_fail_get_shirt_not_found():
    with pytest.raises(ServiceShirtDoesNotExistException):
        ShirtService().get(pk=404)


def test_create_a_shirt():
    shirt = Shirt(
        size="M",
        color="black",
        brand="ZaraMF",
        price=Decimal(50),
    )

    result = ShirtService().create(shirt)

    assert result == shirt


def test_remove_a_shirt():
    assert ShirtService().delete(2) is None


def test_fail_remove_shirt_not_found():
    with pytest.raises(ServiceShirtDoesNotExistException):
        ShirtService().delete(123)


def test_update_a_shirt():
    result = ShirtService().update(
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
    with pytest.raises(ServiceShirtDoesNotExistException):
        ShirtService().update(
            id=404,
            size="M",
            color="Yellow",
            brand="ZaraMF",
            price=Decimal(130),
        )


def test_partially_update_a_shirt():
    service = ShirtService()
    original = service.get(pk=1)

    result = service.update(
        id=original.id,
        color="Yellow",
        brand="ZaraMF",
    )

    assert original.size == result.size
    assert original.price == result.price

    assert result.color == "Yellow"
    assert result.brand == "ZaraMF"
