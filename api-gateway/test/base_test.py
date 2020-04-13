from src.app import app
from unittest import TestCase


class BaseTest(TestCase):
    def setUp(self):
        app.testing - True
        self.app = app.test_client
