import json
from django.urls import reverse as r

# TODO: Criar um fixture para o client do DRF.
def test_index_not_found(client):
    response = client.get("/")
    assert response.status_code == 404


def test_create_new_shirt(client):
    data = {
        "size": "M",
        "color": "black",
        "brand": "ZaraMF",
        "price": 50,
    }
    response = client.post(r("shirt-list"), data=data)
    assert response.status_code == 201


def test_fail_to_create_new_shirt(client):
    response = client.post(r("shirt-list"), data={})
    d = response.json()

    # Usar subtests para não parar no 1º assert False.
    for k in ("campo1", "c2", "...", "cn"):
        assert "k está no dicionário de erros"

def test_create_new_shirt_without_size(client):
    url = r("shirt-list")
    data = {
        "color": "black",
        "brand": "ZaraMF",
        "price": 50,  #TODO: Usar Decimal para dinheiro. NUNCA FLOAT!
    }
    response = client.post(url, data=data)
    assert response.status_code == 400


def test_create_new_shirt_without_color(client):
    url = r("shirt-list")
    data = {
        "size": "M",
        "brand": "ZaraMF",
        "price": 50,
    }
    response = client.post(url, data=data)
    assert response.status_code == 400


def test_create_new_shirt_without_brand(client):
    url = r("shirt-list")
    data = {
        "size": "M",
        "color": "black",
        "price": 50,
    }
    response = client.post(url, data=data)
    assert response.status_code == 400


def test_create_new_shirt_without_brand(client):
    url = r("shirt-list")
    data = {
        "size": "M",
        "color": "black",
        "brand": "ZaraMF",
    }
    response = client.post(url, data=data)
    assert response.status_code == 400


def test_create_new_shirt_with_size_above_max_size(client):
    url = r("shirt-list")
    data = {
        "size": "M" * 15,
        "color": "black",
        "brand": "ZaraMF",
        "price": 50,
    }
    response = client.post(url, data=data)
    assert response.status_code == 400


def test_create_new_shirt_with_string_in_price(client):
    url = r("shirt-list")
    data = {
        "size": "M",
        "color": "black",
        "brand": "ZaraMF",
        "price": "vish",
    }
    response = client.post(url, data=data)
    assert response.status_code == 400


def test_list_shirts(client):
    url = r("shirt-list")
    response = client.get(url)

    assert response.status_code == 200


def test_retrive_shirt_by_id(client):
    url = r("shirt-detail", kwargs={"pk": 1})
    response = client.get(url)

    assert response.status_code == 200


def test_retrive_shirt_by_not_found_id(client):
    url = r("shirt-detail", kwargs={"pk": 3})
    response = client.get(url)

    assert response.status_code == 404


def test_retrive_shirt_checking_expected_fields(client):
    expected_field = {
        "id": 1,
        "size": "M",
        "color": "Black",
        "brand": "Nike",
        "price": 100,
        "slug": "NikeM",
    }

    url = r("shirt-detail", kwargs={"pk": 1})
    response = client.get(url)
    data = response.json()

    assert data == expected_field


def test_update_shirt(client):
    data = {
        "size": "G",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": 110,
    }

    data_expected = {
        "id": 1,
        "size": "G",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": 110.0,
        "slug": "ZaraMFG",
    }

    url = r("shirt-detail", kwargs={"pk": 1})
    response = client.patch(
        url,
        data=json.dumps(data),
        content_type="application/json",
    )
    response_data = response.json()

    assert response.status_code == 200
    assert data_expected == response_data


def test_update_shirt_with_id_not_found(client):
    data = {
        "size": "G",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": 110,
    }
    data_expected = {"message": "Resource not found."}

    url = r("shirt-detail", kwargs={"pk": 10})
    response = client.patch(
        url,
        data=json.dumps(data),
        content_type="application/json",
    )
    response_data = response.json()

    assert response.status_code == 404
    assert data_expected == response_data


def test_update_shirt_with_invalid_price(client):
    data = {
        "size": "G",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": "ABC",
    }

    data_expected = {"price": ["A valid number is required."]}

    url = r("shirt-detail", kwargs={"pk": 1})
    response = client.patch(
        url,
        data=json.dumps(data),
        content_type="application/json",
    )

    response_data = response.json()

    assert response.status_code == 400
    assert data_expected == response_data


def test_partial_update_shirt(client):
    data = {
        "size": "G",
        "price": 195,
    }

    data_expected = {
        "id": 1,
        "size": "G",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": 195.0,
        "slug": "ZaraMFG",
    }

    url = r("shirt-detail", kwargs={"pk": 1})
    response = client.patch(
        url,
        data=json.dumps(data),
        content_type="application/json",
    )

    response_data = response.json()

    assert response.status_code == 200
    assert data_expected == response_data


def test_partial_update_shirt_with_invalid_price(client):
    data = {
        "size": "G",
        "price": "ABC",
    }

    data_expected = {"price": ["A valid number is required."]}

    url = r("shirt-detail", kwargs={"pk": 1})
    response = client.patch(
        url,
        data=json.dumps(data),
        content_type="application/json",
    )

    response_data = response.json()

    assert response.status_code == 400
    assert data_expected == response_data


def test_update_shirt_with_field_unknown(client):
    data = {
        "size": "G",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": 110,
        "eita": "vish",
    }

    data_expected = {
        "id": 1,
        "size": "G",
        "color": "Yellow",
        "brand": "ZaraMF",
        "price": 110.0,
        "slug": "ZaraMFG",
    }

    url = r("shirt-detail", kwargs={"pk": 1})
    response = client.patch(
        url,
        data=json.dumps(data),
        content_type="application/json",
    )
    response_data = response.json()

    assert response.status_code == 200
    assert data_expected == response_data


def test_remove_shirt(client):
    url = r("shirt-detail", kwargs={"pk": 1})
    response = client.delete(
        url,
        content_type="application/json",
    )

    assert response.status_code == 200


def test_remove_shirt_with_id_not_found(client):
    url = r("shirt-detail", kwargs={"pk": 10})
    response = client.delete(
        url,
        content_type="application/json",
    )

    assert response.status_code == 404
