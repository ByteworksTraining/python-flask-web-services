import json

from base_test import BaseTest


class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/api/gateway/docs.json')
            self.assertEqual(resp.status_code, 200)
