'''
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
'''
import sys
import argparse

from ProductionCode.core import get_pokemon_by_stat, get_pokemon_by_name,\
    get_column_names


def print_pokemon(pokemon_info):
    '''
    Prints the Pokemon nicely
    :param pokemon: The Pokemon
    '''
    if pokemon_info is None:
        print("Pokemon not found")
    else:
        pokemon_data = pokemon_info.strip().split(",")

        for i, column_data in enumerate(get_column_names()):
            print(f"{column_data}: {pokemon_data[i]}")

def print_pokemon_list(pokemon_list, stat):
    '''
    Prints the list of Pokemon with the requested stat, formatted nicely
    :param pokemon_list: The list of Pokemon
    '''
    for pokemon in pokemon_list:
        pokemon_data = pokemon.strip().split(",")
        print(f"{pokemon_data[1]}: {pokemon_data[get_column_names().index(stat)]}")


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
    if args.stat not in get_column_names():
        print("Invalid stat")
        sys.exit(1)

    #check if number is valid
    try:
        number = int(args.number)
    except ValueError:
        print("Invalid number")
        sys.exit(1)

    return args.stat, number

def main():
    '''
    Main function to run the command line interface
    '''
    stat, number = parse_args()
    if number is None:
        #print pokemon name and its stats nicely
        pokemon_info = get_pokemon_by_name(stat)
        print_pokemon(pokemon_info)
    else:
        pokemon_final_list = get_pokemon_by_stat(stat, number)
        print_pokemon_list(pokemon_final_list, stat)

if __name__ == "__main__":
    main()
