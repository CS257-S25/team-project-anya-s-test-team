'''
Tests for command_line.py
'''

import io
import sys
import unittest
from unittest.mock import patch, MagicMock
from ProductionCode.core import Core
from cl import CL
import records
from ProductionCode.datasource import DataSource

class TestDataSource(unittest.TestCase):
    '''Test class for datasource.py'''

    # @patch('ProductionCode.datasource.psycopg2.connect')
    # def setUp(self, mock_connect):
    #     '''
    #     Set up the test case
    #     '''
    #     #create a mock connection and cursor
    #     self.mock_conn = MagicMock()
    #     self.mock_cursor = self.mock_conn.cursor.return_value
    #     mock_connect.return_value = self.mock_conn
    #     self.ds = DataSource()

    @patch('ProductionCode.datasource.records.Database')
    def test_get_pokemon_by_name(self, mock_db_class):
        # Setup the mock database instance
        mock_db_instance = mock_db_class.return_value
        
        # Setup the mock record
        mock_record = MagicMock()
        expected_csv = "1,Bulbasaur,Fake"
        mock_record.export.return_value = expected_csv
        
        # Mock the query result (a list containing our record)
        mock_db_instance.query.return_value = [mock_record]
        
        # Initialize a fresh DataSource for this test
        ds = DataSource()
        
        # Act
        result = ds.get_pokemon_by_name("Bulbasaur")
        
        # Assert
        self.assertEqual(result, expected_csv)
        # Verify the query was called with the correct parameter
        mock_db_instance.query.assert_called_once_with(
            "SELECT * FROM pokemon WHERE name = :name", 
            name="Bulbasaur"
        )

    @patch('ProductionCode.datasource.records.Database')
    def test_get_pokemon_by_name_returns_csv(self, mock_db_class):
        # 1. Setup the Mocks
        # mock_db_class is the mocked 'records.Database' class
        # mock_db_instance is what is returned when 'records.Database()' is called
        mock_db_instance = mock_db_class.return_value
        
        # Create a mock for the individual row, MagicMock makes an object with all the normal built-in methods
        # and lets you add additional things to it
        mock_row = MagicMock()

        # When export is called on the mock_row, regardless of parameter, this string is returned
        # this works because all functions/methods are actually objects in Python
        mock_row.export.return_value = "1,Pikachu,Electric"
        
        # Mock the .query() method to return a list containing our mock_row
        mock_db_instance.query.return_value = [mock_row]

        # 2. Initialize a fresh DataSource for this test
        ds = DataSource()

        # Run the code we are testing
        result = ds.get_pokemon_by_name("Pikachu")

        # 3. Assertions
        # Verify the database was queried with the correct parameters
        mock_db_instance.query.assert_called_once_with(
            "SELECT * FROM pokemon WHERE name = :name", 
            name="Pikachu"
        )
        
        # Verify the row's export method was called
        mock_row.export.assert_called_with('csv')
        
        # Verify the final output
        self.assertEqual(result, "1,Pikachu,Electric")

    @patch('ProductionCode.datasource.records.Database')
    def test_get_pokemon_by_name_not_found(self, mock_db_class):
        # Setup query to return an empty list
        mock_db_class.return_value.query.return_value = []
        
        ds = DataSource()
        result = ds.get_pokemon_by_name("MissingNo")
        
        self.assertIsNone(result)