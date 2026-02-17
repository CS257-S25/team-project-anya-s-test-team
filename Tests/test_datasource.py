import unittest
import records
import os
from ProductionCode.datasource import DataSource

##TODO: works locally but not on GitHub, need to investigate
## As of 2/16/26 
class TestDataSourceIntegration(unittest.TestCase):
    def setUp(self):
        self.test_db_url = "sqlite:///:memory:"
        self.ds = DataSource(db_url=self.test_db_url)
        
        # Build the world
        self.ds.database.query("CREATE TABLE pokemon (id INT, name TEXT, type TEXT)")
        self.ds.database.query(
            "INSERT INTO pokemon (id, name, type) VALUES (:id, :name, :type)",
            id=25, name="Pikachu", type="Electric"
        )

    def test_get_pokemon_by_name_success(self):
        result = self.ds.get_pokemon_by_name("Pikachu")
        self.assertIsNotNone(result)
        self.assertIn("Pikachu", result)
        self.assertIn("Electric", result)

    def test_get_pokemon_by_name_missing(self):
        result = self.ds.get_pokemon_by_name("MissingNo")
        self.assertIsNone(result)
