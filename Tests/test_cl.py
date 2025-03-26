'''
Tests for command_line.py
'''

import io
import sys
import unittest
from unittest.mock import patch
from ProductionCode.core import get_pokemon_by_name, \
    get_pokemon_by_stat
from cl import print_pokemon


class TestCommandLine(unittest.TestCase):
    '''
    Test class for command_line.py
    This class contains unit tests for the functions in command_line.py
    '''
    @patch('ProductionCode.core.data', [\
            "1,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,False"])
    def test_get_pokemon_by_name(self):
        '''
        Test get_pokemon_by_name
        '''
        self.assertEqual(get_pokemon_by_name("Bulbasaur"), \
                         "1,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,False")

    @patch('ProductionCode.core.data', [\
            "1,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,False",\
                  "2,Ivysaur,Grass,Poison,60,62,63,80,80,60,1,False"])
    def test_get_pokemon_by_stat(self):
        '''
        Test get_pokemon_by_stat
        '''
        self.assertEqual(get_pokemon_by_stat("HP", 1), \
                         ["2,Ivysaur,Grass,Poison,60,62,63,80,80,60,1,False"])

    @patch('ProductionCode.core.data', ["1,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,False"])
    @patch('ProductionCode.core.column_names',
            ["Pokedex Number", "Name", "Type 1", "Type 2", "HP",
            "Attack", "Defense", "Special Attack", "Special Defense", \
                "Speed", "Generation", "Legendary"])

    def test_print_pokemon(self):
        '''
        Test print_pokemon
        '''
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_pokemon("1,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,False")

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), \
                         "Pokedex Number: 1\nName: Bulbasaur\nType 1: Grass\nType 2: "+\
                            "Poison\nHP: 45\nAttack: 49\nDefense: 49\nSpecial Attack: 65\n"+\
                                "Special Defense: 65\nSpeed: 45\nGeneration: 1\nLegendary: False\n")
