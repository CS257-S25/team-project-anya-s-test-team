'''
The goal of this component of your project is to create a minimal app 
to allow a user to interact with your data via the command line. 
Your app should also include an automated test suite.

The learning objectives for this subcomponent of your project are to 
be able to 1) create an automated test suite, 2) create an app with 
a command line interface, and 3) create code that follows the principles 
of good function design.

Supports at least two independent features; each of these features should
 enable the user to get information from your dataset(s) via the command line interface
Has a usage statement
Has an automated test suite with reasonable coverage (probably 10-20 tests)
Follows the function design principles and has generally good style
Has documentation through docstrings and in-line comments where appropriate
Follows the recommended Python style'''


from ProductionCode.datasource import DataSource

class Core:
    '''
    Core class for the project
    This class contains the functions that will be used by the command line interface
    '''
    def __init__(self):
        '''
        Initializes the core class
        '''

        #initialize the column names
        self.column_names = "#,Name,Type 1,Type 2,Total,HP,Attack,\
    Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary".split(",")
        self.data_source = DataSource()


    def get_column_names(self):
        '''
        Returns the column names for the data
        :return: The column names
        '''
        return self.column_names

    def get_pokemon_by_stat(self,desired_stat, count):
        '''
        Returns the top number of Pokemon by the given stat
        :param stat: The stat to use
        :param count: The number of Pokemon to display
        :return: A list of Pokemon
        more docs
        ''' 

        result = self.data_source.get_pokemon_by_stat(desired_stat, count)
        if result:
            return [",".join(map(str, pokemon)) for pokemon in result]
        else:
            return []
        # #sort the data by the given stat
        # stat_index = column_names.index(desired_stat)
        # data.sort(key=lambda x: int(x.split(",")[stat_index]), reverse=True)

        # #return the top number of Pokemon
        # return data[:count]

    def get_pokemon_by_name(self,name):
        '''
        Returns the Pokemon with the given name
        :param name: The name of the Pokemon
        :return: The Pokemon
        '''
        result = self.data_source.get_pokemon_by_name(name)
        if result:
            return ",".join(map(str, result))
        else:
            return None
