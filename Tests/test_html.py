
from ProductionCode.core import Core
import unittest

from app import app

class TestHTMLForm(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Pokemon", response.data)

    def test_display_row(self):
        response = self.app.get('/displayrow?rowchoice=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Your pokemon: 1", response.data)
