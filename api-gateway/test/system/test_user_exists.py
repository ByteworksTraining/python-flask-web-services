import json
from unittest.mock import MagicMock

from flask import jsonify

from base_test import BaseTest
from gateway_api.services.user_client import UserClient
from gateway_api import routes
from mock import patch


class TestUserExists(BaseTest):

    def test_post_user_exists_405(self):
        with self.app() as c:
            resp = c.post('/api/user/my_user/exists')
            self.assertEqual(resp.status_code, 405)

    @patch('gateway_api.services.user_client.UserClient.does_exist')
    def test_user_exist_true_mocked(self, does_exist_mock):
        with self.app() as c:
            does_exist_mock.return_value = "{'result': True}"
            resp = c.get('/api/user/my_user/exists')
            self.assertEqual(resp.status_code, 200)