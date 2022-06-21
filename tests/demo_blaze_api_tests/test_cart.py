import json
import uuid

from client.api.demo_blaze import DemoBlaze
from tests.demo_blaze_api_tests import BaseApiTests
import logging as logger
from enum import Enum


class Device(Enum):
    NEXUS6 = 3


class TestCart(BaseApiTests):
    def add_device_to_cart(self, device):
        json_data = {
            "id": str(uuid.uuid1()),
            "cookie": self.token,
            "prod_id": device,
            "flag": "true"
        }
        DemoBlaze().add_to_cart(json_data)

    def view_cart(self):
        json_data = {"cookie": self.token, "flag": "true"}
        response = DemoBlaze().view_cart(json_data)
        response_content = json.loads(response.content)
        return response_content

    def test_cart_has_1_item(self, sign_in_and_get_token):
        logger.info("TEST: Only 1 item exists in the cart after choosing nexus6 device")
        self.token = sign_in_and_get_token
        self.add_device_to_cart(Device.NEXUS6.value)
        response_content = self.view_cart()
        assert len(response_content['Items']) == 1

    def test_price_of_nexus_is_650(self, sign_in_and_get_token):
        logger.info("TEST: Add nexus6 to the cart and verify that price is 650")
        self.token = sign_in_and_get_token
        self.add_device_to_cart(Device.NEXUS6.value)
        response_content = self.view_cart()
        prod_id = response_content['Items'][0]["prod_id"]
        json_data = {"id": prod_id}
        response = DemoBlaze().view_item(json_data)
        response_content = json.loads(response.content)
        assert response_content["price"] == 650

    def test_title_of_nexus6_phone_is_nexus6(self, sign_in_and_get_token):
        logger.info("TEST: Add nexus6 to the cart and verify that title is nexus6")
        self.token = sign_in_and_get_token
        self.add_device_to_cart(Device.NEXUS6.value)
        response_content = self.view_cart()
        prod_id = response_content['Items'][0]["prod_id"]
        json_data = {"id": prod_id}
        response = DemoBlaze().view_item(json_data)
        response_content = json.loads(response.content)
        assert response_content["title"] == "Nexus 6"

    def test_item_id_of_nexus6_phone_id_3(self, sign_in_and_get_token):
        logger.info("TEST: Add nexus6 to the cart and verify that phone id is 3")
        self.token = sign_in_and_get_token
        self.add_device_to_cart(Device.NEXUS6.value)
        response_content = self.view_cart()
        prod_id = response_content['Items'][0]["prod_id"]
        json_data = {"id": prod_id}
        response = DemoBlaze().view_item(json_data)
        response_content = json.loads(response.content)
        assert response_content["id"] == 3
