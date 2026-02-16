import unittest
from unittest.mock import patch


db_patcher = patch('ProductionCode.datasource.records.Database')
mock_db_class = db_patcher.start()
from app import app

class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        # Creates a test client so we can make requests without running a server
        self.client = app.test_client()
        self.client.testing = True

    @patch('app.ds.get_pokemon_by_name')
    def test_display_route_success(self, mock_get_pokemon):
        # 1. Setup the Mock response
        # We simulate what the Datasource would return (the CSV string)

        mock_get_pokemon.return_value = "25,Pikachu,Electric"

        # 2. Simulate a GET request to the route
        response = self.client.get('/pokemon/Pikachu/')

        # 3. Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "25,Pikachu,Electric")
        
        # Verify the mock was called with the right argument from the URL
        mock_get_pokemon.assert_called_once_with("Pikachu")

    @patch('app.ds.get_pokemon_by_name')
    def test_display_route_not_found(self, mock_get_pokemon):
        # Setup the mock to return None (simulating a missing database record)
        mock_get_pokemon.return_value = None

        response = self.client.get('/pokemon/MissingNo/')

        self.assertEqual(response.status_code, 200)
        self.assertIn("No pokemon!", response.data.decode('utf-8'))