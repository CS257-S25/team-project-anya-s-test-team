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

##open the data file Data/Pokemon.csv
with open("Data/Pokemon.csv", "r", encoding="utf-8") as data_file:
    column_names = data_file.readline().strip().split(",")
    data = data_file.readlines()


def get_column_names():
    '''
    Returns the column names for the data
    :return: The column names
    '''
    return column_names

def get_pokemon_by_stat(desired_stat, count):
    '''
    Returns the top number of Pokemon by the given stat
    :param stat: The stat to use
    :param count: The number of Pokemon to display
    :return: A list of Pokemon
    '''

    #sort the data by the given stat
    stat_index = column_names.index(desired_stat)
    data.sort(key=lambda x: int(x.split(",")[stat_index]), reverse=True)

    #return the top number of Pokemon
    return data[:count]

def get_pokemon_by_name(name):
    '''
    Returns the Pokemon with the given name
    :param name: The name of the Pokemon
    :return: The Pokemon
    '''

    #find the Pokemon with the given name
    for a_pokemon in data:
        pokemon_data = a_pokemon.strip().split(",")
        if pokemon_data[1] == name:
            return a_pokemon

    return None
