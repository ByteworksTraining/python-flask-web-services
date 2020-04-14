import json
from base_test import BaseTest


class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/api/gateway/version')
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), {'version': "1.0.0"})

    def test_get_not_found_404(self):
        "Test getting a non existent request"
        with self.app() as c:
            resp = c.get('/api/nowhere')
            self.assertEqual(resp.status_code, 404)
