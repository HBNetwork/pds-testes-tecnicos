import json
from decimal import Decimal

from automation_store.core.services import ShirtService
from django.urls import reverse as r


def test_index_not_found(api_client):
    response = api_client.get("/")

    assert response.status_code == 404


def test_create_new_shirt(api_client):
    data = {
        "size": "M",
        "color": "black",
        "brand": "ZaraMF",
        "price": Decimal(110),
    }
    response = api_client.post(r("shirt-list"), data=data)
    assert response.status_code == 201


def test_fail_to_create_new_shirt_without_required_fields(api_client, subtests):
    expect_keys = ("size", "color", "brand", "price")
    expect_message = ["This field is required."]

    response = api_client.post(r("shirt-list"), data={})
    data = response.json()

    assert response.status_code == 400

    for k in expect_keys:
        with subtests.test("custom message", i=k):
            assert k in data
            assert data[k] == expect_message


def test_create_new_shirt_with_string_in_price(api_client):
    url = r("shirt-list")
    data = {
        "size": "M",
        "color": "black",
        "brand": "ZaraMF",
        "price": "vish",
    }
    response = api_client.post(url, data=data)
    assert response.status_code == 400


def test_list_shirts(api_client):
    url = r("shirt-list")
    response = api_client.get(url)

    assert response.status_code == 200


def test_retrive_shirt_by_id(api_client):
    url = r("shirt-detail", kwargs={"pk": 1})
    response = api_client.get(url)

    assert response.status_code == 200


def test_retrive_shirt_by_not_found_id(api_client):
    url = r("shirt-detail", kwargs={"pk": 324})
    response = api_client.get(url)

    assert response.status_code == 404


def test_retrive_shirt_checking_expected_fields(api_client):
    expected_field = {
        "id": 1,
        "size": "M",
        "color": "Black",
        "brand": "Nike",
        "price": "100.00",
        "slug": "NikeM",
    }

    url = r("shirt-detail", kwargs={"pk": 1})
    response = api_client.get(url)
    data = response.json()

    assert data == expected_field


def test_update_shirt(api_client):
    data = {
        "size": "G",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": Decimal(110),
    }

    data_expected = {
        "id": 1,
        "size": "G",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": "110.00",
        "slug": "ZaraMFG",
    }

    url = r("shirt-detail", kwargs={"pk": 1})
    response = api_client.patch(
        url,
        data=data,
        format="json",
    )
    response_data = response.json()

    assert response.status_code == 200
    assert data_expected == response_data


def test_update_shirt_with_id_not_found(api_client):
    data = {
        "size": "G",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": Decimal(110),
    }
    data_expected = {"message": "Resource not found."}

    url = r("shirt-detail", kwargs={"pk": 10})
    response = api_client.patch(
        url,
        data=data,
        format="json",
    )
    response_data = response.json()

    assert response.status_code == 404
    assert data_expected == response_data


def test_update_shirt_with_invalid_price(api_client):
    data = {
        "size": "G",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": "ABC",
    }

    data_expected = {"price": ["A valid number is required."]}

    url = r("shirt-detail", kwargs={"pk": 1})
    response = api_client.patch(
        url,
        data=json.dumps(data),
        content_type="application/json",
    )

    response_data = response.json()

    assert response.status_code == 400
    assert data_expected == response_data


def test_partial_update_shirt(api_client):
    service = ShirtService()

    data = {
        "size": "G",
        "price": Decimal(195.00),
    }

    data_expected = {
        "id": 1,
        "size": data["size"],
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": "195.00",
        "slug": "ZaraMFG",
    }

    url = r("shirt-detail", kwargs={"pk": 1})
    response = api_client.patch(
        url,
        data=data,
        format="json",
    )

    response_data = response.json()

    assert response.status_code == 200
    assert data_expected == response_data


def test_partial_update_shirt_with_invalid_price(api_client):
    data = {
        "size": "G",
        "price": "ABC",
    }

    data_expected = {"price": ["A valid number is required."]}

    url = r("shirt-detail", kwargs={"pk": 1})
    response = api_client.patch(
        url,
        data=json.dumps(data),
        content_type="application/json",
    )

    response_data = response.json()

    assert response.status_code == 400
    assert data_expected == response_data


def test_update_shirt_with_field_unknown(api_client):
    data = {
        "size": "G",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": Decimal(110.00),
        "eita": "vish",
    }

    data_expected = {
        "id": 1,
        "size": "G",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": "110.00",
        "slug": "ZaraMFG",
    }

    url = r("shirt-detail", kwargs={"pk": 1})
    response = api_client.patch(
        url,
        data=data,
        format="json",
    )
    response_data = response.json()

    assert response.status_code == 200
    assert data_expected == response_data


def test_remove_shirt(api_client):
    url = r("shirt-detail", kwargs={"pk": 1})
    response = api_client.delete(
        url,
        content_type="application/json",
    )

    assert response.status_code == 200


def test_remove_shirt_with_id_not_found(api_client):
    url = r("shirt-detail", kwargs={"pk": 10})
    response = api_client.delete(
        url,
        content_type="application/json",
    )

    assert response.status_code == 404
