import base64
import json
import logging

from _pytest.fixtures import fixture

from client.api.demo_blaze import DemoBlaze
from config import Configuration

logger = logging.getLogger(__name__)


class BaseApiTests:
    token = None

    @staticmethod
    def set_login_payload():
        user_name = Configuration.user_name
        password = Configuration.password
        logger.info(f"sign in with user {user_name} and password {password} and set cookies")

        password_bytes = password.encode('ascii')
        base64_bytes = base64.b64encode(password_bytes)
        base64_password = base64_bytes.decode('ascii')

        payload = {"username": user_name, "password": base64_password}
        return payload

    @fixture(scope="class")
    def sign_in_and_get_token(self):
        data = self.set_login_payload()
        sign_in_response = DemoBlaze().login(json_body=data)
        assert sign_in_response.status_code == 200
        self.token = str(sign_in_response.content).split(':')[1].split('"')[0].strip()
        return self.token

    @fixture(autouse=True)
    def clear_cart(self):
        yield
        json_data = {"cookie": self.token, "flag": "true"}
        response = DemoBlaze().view_cart(json_data)
        response_content = json.loads(response.content)
        for item in response_content['Items']:
            json_data = {"id": item['id']}
            DemoBlaze().remove_from_cart(json_body=json_data)
