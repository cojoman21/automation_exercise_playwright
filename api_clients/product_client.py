from api_clients.base_client import BaseClient


class ProductClient(BaseClient):
    def search_product(self, product_name: str):
        form = {"search_product": "top"}

        return self.session.post(f"{self.base_url}/searchProduct", form=form)

    def get_all_products(self):
        return self.session.get(f"{self.base_url}/productsList")
