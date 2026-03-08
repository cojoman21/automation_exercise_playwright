from api_clients.product_client import ProductClient


def test_GET_all_products_list(product_client: ProductClient):
    get_res = product_client.get_all_products()

    assert get_res.status == 200

    get_res_data = get_res.json()

    assert "products" in get_res_data
    assert len(get_res_data["products"]) > 0
    print(f"Found {len(get_res_data['products'])} products!")
