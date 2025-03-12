'''
The goal of this component of your project is to create a minimal app to allow a user to interact with your data via the command line. Your app should also include an automated test suite.

The learning objectives for this subcomponent of your project are to be able to 1) create an automated test suite, 2) create an app with a command line interface, and 3) create code that follows the principles of good function design.

Supports at least two independent features; each of these features should enable the user to get information from your dataset(s) via the command line interface
Has a usage statement
Has an automated test suite with reasonable coverage (probably 10-20 tests)
Follows the function design principles and has generally good style
Has documentation through docstrings and in-line comments where appropriate
Follows the recommended Python style'''


import argparse

##open the data file Data/Pokemon.csv
data_file = open("Data/Pokemon.csv", "r")
column_names = data_file.readline().strip().split(",")


def get_pokemon_by_stat(stat, number):
    '''
    Returns the top number of Pokemon by the given stat
    :param stat: The stat to use
    :param number: The number of Pokemon to display
    :return: A list of Pokemon
    '''
    #read the data file
    data = data_file.readlines()
    data_file.close()

    #sort the data by the given stat
    stat_index = column_names.index(stat)
    data.sort(key=lambda x: int(x.split(",")[stat_index]), reverse=True)

    #return the top number of Pokemon
    return data[:number]

def get_pokemon_by_name(name):
    '''
    Returns the Pokemon with the given name
    :param name: The name of the Pokemon
    :return: The Pokemon
    '''
    #read the data file
    data = data_file.readlines()
    data_file.close()

    #find the Pokemon with the given name
    for pokemon in data:
        pokemon_data = pokemon.strip().split(",")
        if pokemon_data[1] == name:
            return pokemon

    return None

def print_pokemon(pokemon):
    '''
    Prints the Pokemon nicely
    :param pokemon: The Pokemon
    '''
    if pokemon is None:
        print("Pokemon not found")
    else:
        pokemon_data = pokemon.strip().split(",")
        for i in range(len(column_names)):
            print(f"{column_names[i]}: {pokemon_data[i]}")

def print_pokemon_list(pokemon_list, stat):
    '''
    Prints the list of Pokemon with the requested stat, formatted nicely
    :param pokemon_list: The list of Pokemon
    '''
    for pokemon in pokemon_list:
        pokemon_data = pokemon.strip().split(",")
        print(f"{pokemon_data[1]}: {pokemon_data[column_names.index(stat)]}")


def parse_args():
    '''
    Parses the command line arguments
    :return: The stat, number, or name of Pokemon to display
    '''
    parser = argparse.ArgumentParser(description="Command line interface for the Pokemon")

    
    parser.add_argument("--stat", type=str, help="Stat to use")
    parser.add_argument("--number", type=str, help="Number of Pokemon to display")
    parser.add_argument("--name", type=str, help="Name of the Pokemon")
    args = parser.parse_args()

    #check if name argument provided and if so, return it
    if args.name:
        return args.name, None

    
    #check if stat is valid (i.e. within column_names)
    if args.stat not in column_names:
        print("Invalid stat")
        exit(1)

    #check if number is valid
    try:
        number = int(args.number)
    except ValueError:
        print("Invalid number")
        exit(1)

    return args.stat, number


if __name__ == "__main__":
    stat, number = parse_args()
    if number == None:
        #print pokemon name and its stats nicely
        pokemon = get_pokemon_by_name(stat)
        print_pokemon(pokemon)
    else:
        pokemon_list = get_pokemon_by_stat(stat, number)
        print_pokemon_list(pokemon_list, stat)
    