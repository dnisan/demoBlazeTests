from config import Configuration
import requests


class DemoBlaze:
    base_url = Configuration.base_uri

    def login(self, json_body):
        url = "{}/login".format(self.base_url)
        response = requests.post(url=url, json=json_body)
        assert response.status_code == 200
        return response

    def view_cart(self, json_body):
        url = "{}/viewcart".format(self.base_url)
        response = requests.post(url=url, json=json_body)
        assert response.status_code == 200
        return response

    def add_to_cart(self, json_body):
        url = "{}/addtocart".format(self.base_url)
        response = requests.post(url=url, json=json_body)
        assert response.status_code == 200
        return response

    def view_item(self, json_body):
        url = "{}/view".format(self.base_url)
        response = requests.post(url=url, json=json_body)
        assert response.status_code == 200
        return response

    def remove_from_cart(self, json_body):
        url = "{}/deleteitem".format(self.base_url)
        response = requests.post(url=url, json=json_body)
        assert response.status_code == 200
        return response
