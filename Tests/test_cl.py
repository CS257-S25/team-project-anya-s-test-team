'''
Tests for command_line.py
'''

import io
import sys
import unittest
from unittest.mock import patch, MagicMock
from ProductionCode.core import Core
from cl import CL
import psycopg2
from ProductionCode.datasource import DataSource

class TestDataSource(unittest.TestCase):
    '''Test class for datasource.py'''

    #a test that make a mock database and tests the get_pokemon_by_name function
    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_get_pokemon_by_name(self, mock_connect):
        '''
        Test get_pokemon_by_name
        '''
        #create a mock connection and cursor
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchone.return_value = (1, "Bulbasaur", "Grass", "Poison", 45, 49, 49, 65, 65, 45, 1, False)
        data_source = DataSource()
        result = data_source.get_pokemon_by_name("Bulbasaur")
        self.assertEqual(result, (1, "Bulbasaur", "Grass", "Poison", 45, 49, 49, 65, 65, 45, 1, False))
        mock_cursor.execute.assert_called_once_with("SELECT * FROM pokemon WHERE name = %s", ("Bulbasaur",))

        


class TestCommandLine(unittest.TestCase):
    '''
    Test class for command_line.py
    This class contains unit tests for the functions in command_line.py
    '''

    def setUp(self):
        '''
        Set up the test case
        '''
        #create a mock connection and cursor
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_get_pokemon_by_name(self, mock_connect):
        '''
        Test get_pokemon_by_name
        '''
        #create a mock connection and cursor
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = (1, "Bulbasaur", "Grass", "Poison", 45, 49, 49, 65, 65, 45, 1, False)
        
        test_core = Core()
        self.assertEqual(test_core.get_pokemon_by_name("Bulbasaur"), \
                         "1,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,False")

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_get_pokemon_by_stat(self, mock_connect):
        '''
        Test get_pokemon_by_stat
        '''
        #create a mock connection and cursor
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.fetchall.return_value = [
            (2, "Ivysaur", "Grass", "Poison", 60, 62, 63, 80, 80, 60, 1, False)
        ]

        test_core = Core()
        self.assertEqual(test_core.get_pokemon_by_stat("HP", 1), \
                         ["2,Ivysaur,Grass,Poison,60,62,63,80,80,60,1,False"])

    @patch('ProductionCode.datasource.psycopg2.connect')
    @patch('ProductionCode.core.Core.get_column_names')
    def test_print_pokemon(self, mock_get_column_names, mock_connect):
        '''
        Test print_pokemon
        '''
        #create a mock connection and cursor
        mock_connect.return_value = self.mock_conn
        mock_get_column_names.return_value = ["#", "Name", "Type 1", "Type 2"]
        test_cl = CL()
        sys.stdout = io.StringIO()
        test_cl.print_pokemon("1,Bulbasaur,Grass,Poison")
        expected_output = (
            "#: 1\n"
            "Name: Bulbasaur\n"
            "Type 1: Grass\n"
            "Type 2: Poison\n"
        )
        self.assertEqual(sys.stdout.getvalue(), expected_output)