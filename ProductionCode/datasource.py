import records
import ProductionCode.psql_config as config
#from ProductionCode.single_meta import SingletonMeta

class DataSource:
    def __init__(self, db_url=None):
        # Allow passing a URL for easier testing, or default to config
        self.database_url = db_url or f"postgresql://{config.USER}:{config.PASSWORD}@{config.HOST}:5432/{config.DATABASE}"
        self.database = records.Database(self.database_url)

    def get_pokemon_by_name(self, name):
        # Use parameterized query (:name) instead of .format()
        query = "SELECT * FROM pokemon WHERE name = :name"
        rows = self.database.query(query, name=name).all() #print, checking length, etc uses up the results, 
            # so we need to store it in a variable before trying to access it multiple times
        print("in get pokemon rows:", rows)
        if rows and len(rows) > 0:
            print(rows)
            return rows[0].export('csv')
        return None
        
    def get_pokemon_by_stat(self, stat, count):
        '''
        Returns the top number of Pokemon by the given stat
        :param stat: The stat to use
        :param count: The number of Pokemon to display
        :return: A list of Pokemon
        '''
        #sort the data by the given stat
        rows = self.database.query(f"SELECT * FROM pokemon ORDER BY {stat} DESC LIMIT {count}")
        return rows.export('csv')