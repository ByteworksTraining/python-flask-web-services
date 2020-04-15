import json
from unittest.mock import MagicMock

from flask import jsonify

from base_test import BaseTest
from gateway_api.services.user_client import UserClient
from gateway_api import routes
from mock import patch


class TestLogin(BaseTest):

    def test_get_login_405(self):
        with self.app() as c:
            resp = c.get('/api/login')
            self.assertEqual(resp.status_code, 405)

    def test_post_login_no_payload(self):
        with self.app() as c:
            resp = c.post('/api/login')
            self.assertEqual(resp.status_code, 400)
            self.assertEqual(resp.data.decode('utf-8'), 'Login must contain JSON')

    def test_post_login_no_username(self):
        with self.app() as c:
            resp = c.post('/api/login',
                          data=json.dumps(dict(password='secret')),
                          follow_redirects=True,
                          content_type='application/json'
                          )
            self.assertEqual(resp.status_code, 400)
            self.assertEqual(resp.data.decode('utf-8'), 'Username parameter is missing')

    def test_post_login_no_password(self):
        with self.app() as c:
            resp = c.post('/api/login',
                          data=json.dumps(dict(username='my-name')),
                          follow_redirects=True,
                          content_type='application/json'
                          )
            self.assertEqual(resp.status_code, 400)
            self.assertEqual(resp.data.decode('utf-8'), 'Password parameter is missing')

    @patch('gateway_api.services.user_client.UserClient.post_login')
    def test_post_login_mocked(self, post_login_mock):
        with self.app() as c:
            post_login_mock.return_value = 'abcdefg'
            user_client = UserClient()
            user_client.post_login = MagicMock(return_value='abcedef')
            routes.user_client = user_client
            resp = c.post('/api/login',
                          data=json.dumps(dict(username='my-name', password='secret')),
                          follow_redirects=True,
                          content_type='application/json'
                          )
            self.assertEqual(resp.status_code, 200)
