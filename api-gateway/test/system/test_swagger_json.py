import json

from base_test import BaseTest


class TestSwaggerJson(BaseTest):
    def test_swagger_json(self):
        with self.app() as c:
            resp = c.get('/api/gateway/docs.json')
            self.assertEqual(resp.status_code, 200)
