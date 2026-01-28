import io
import sys
import unittest
from unittest.mock import patch, MagicMock
from ProductionCode.core import Core
from cl import CL
import psycopg2
from ProductionCode.datasource import DataSource

from app import app

class TestFlaskApp(unittest.TestCase):
    '''Test class for the Flask app '''

    def setUp(self):
        '''
        Set up the test case
        '''
        self.app = app.test_client()
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value
        
        #self.app.testing = True

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_index(self, mock_connect):
        '''
        Test the index route
        '''
        # Create a mock connection and cursor 
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = (1, "Bulbasaur", "Grass", "Poison", 45, 49, 49, 65, 65, 45, 1, False)
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Pokemon API!", response.data)