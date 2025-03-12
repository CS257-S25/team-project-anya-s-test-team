'''
Tests for command_line.py
'''

import unittest
from unittest.mock import patch
from ProductionCode.cl import get_pokemon_by_name, get_pokemon_by_stat, print_pokemon, print_pokemon_list, parse_args
import io
import sys

class TestCommandLine(unittest.TestCase):
    
        @patch('ProductionCode.cl.data_file')
        def test_get_pokemon_by_name(self, mock_data_file):
            '''
            Test get_pokemon_by_name
            '''
            mock_data_file.readlines.return_value = ["1,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,False"]
            self.assertEqual(get_pokemon_by_name("Bulbasaur"), "1,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,False")
    
        @patch('ProductionCode.cl.data_file')
        def test_get_pokemon_by_stat(self, mock_data_file):
            mock_data_file.readlines.return_value = ["1,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,False", "2,Ivysaur,Grass,Poison,60,62,63,80,80,60,1,False"]
            self.assertEqual(get_pokemon_by_stat("HP", 1), ["2,Ivysaur,Grass,Poison,60,62,63,80,80,60,1,False"])
    
        @patch('ProductionCode.cl.data_file')
        @patch('ProductionCode.cl.column_names', 
               ["Pokedex Number", "Name", "Type 1", "Type 2", "HP", 
                "Attack", "Defense", "Special Attack", "Special Defense", "Speed", "Generation", "Legendary"])
        def test_print_pokemon(self, mock_data_file):
            mock_data_file.readlines.return_value = ["1,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,False"]
            captured_output = io.StringIO()
            sys.stdout = captured_output
            print_pokemon("1,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,False")
           
            sys.stdout = sys.__stdout__
            self.assertEqual(captured_output.getvalue(), "Pokedex Number: 1\nName: Bulbasaur\nType 1: Grass\nType 2: Poison\nHP: 45\nAttack: 49\nDefense: 49\nSpecial Attack: 65\nSpecial Defense: 65\nSpeed: 45\nGeneration: 1\nLegendary: False\n")
