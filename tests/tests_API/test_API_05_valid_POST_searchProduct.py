from api_clients.product_client import ProductClient


def test_post_to_search_product(product_client: ProductClient):
    search_product_res = product_client.search_product("top")

    search_product_data = search_product_res.json()

    assert search_product_data["responseCode"] == 200
    assert "products" in search_product_data

    assert len(search_product_data["products"]) > 0

    first_product_name = search_product_data["products"][0]["name"].lower()
    assert "top" in first_product_name
