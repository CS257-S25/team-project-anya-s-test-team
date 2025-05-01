import psycopg2
import ProductionCode.psql_config as config
import sys

class DataSource:

    def __init__(self):
       self.connect()

    def connect(self):
        '''
        Connects to the database
        :return: None
        '''
        conn = None
        try:
            # Connect to the PostgreSQL database
            conn = psycopg2.connect(
                host=config.HOST,
                database=config.DATABASE,
                user=config.USER,
                password=config.PASSWORD
            )
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")
            sys.exit(1)
        # Create a cursor object
        self.connection = conn
        self.cursor = self.connection.cursor()

    def get_pokemon_by_name(self, name):
        self.cursor.execute("SELECT * FROM pokemon WHERE name = %s", (name,))

        result = self.cursor.fetchone()
        if result:
            return result
        else:
            return None
        
    def get_pokemon_by_stat(self, stat, count):
        '''
        Returns the top number of Pokemon by the given stat
        :param stat: The stat to use
        :param count: The number of Pokemon to display
        :return: A list of Pokemon
        '''
        #sort the data by the given stat
        self.cursor.execute(f"SELECT * FROM pokemon ORDER BY {stat} DESC LIMIT %s", (count,))
        return self.cursor.fetchall()