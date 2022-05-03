from django.urls import reverse


def test_index_not_found(client):
    response = client.get("/")
    assert response.status_code == 404


def test_create_new_tshirt(client):
    url = reverse("tshirt-list")
    data = {
        'size': 'M',
        'color': 'black',
        'brand': 'ZaraMF',
        'price': 50,
    }
    response = client.post(url, data=data)
    print(response.json())
    assert response.status_code == 201
