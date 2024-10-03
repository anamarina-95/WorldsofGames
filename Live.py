# Importing the child classes files with their child class object and variables
from CurrencyRouletteGame import CurrencyRouletteGame, currency_game_difficulty, currency_num
from GuessGame import GuessGame, guess_game_difficulty, guess_num
from MemoryGame import MemoryGame, memory_game_difficulty, memory_num
from Scores import add_score


# The welcome() function ask for user input in case none is provided
def welcome(name):
    while True:
        if name == '':
            name = input("Please enter your name:")
            continue
        else:
            print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
            break


# The get_type_and_difficulty() function checks if the user input is digit and if is in the specified range
def get_type_and_difficulty(input_placeholder, range_placeholder):
    while True:
        if not input_placeholder.isdigit() or int(input_placeholder) not in range_placeholder:
            input_placeholder = input("Try again:")
            continue
        elif input_placeholder.isdigit() and int(input_placeholder) in range_placeholder:
            return input_placeholder
        break


# The function load_game() asks the user for a game number and difficulty input and starts the related game.
# If the users guess is correct then the function add_score is activated and the score is saved in the Scores.txt file
def load_game():
    print("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    defined_range_game = range(1, 4)
    defined_range_difficulty = range(1, 6)
    game_number = get_type_and_difficulty(input("Type the game number:"), defined_range_game)
    user_number = get_type_and_difficulty(input("Please choose game difficulty from 1 to 5:"), defined_range_difficulty)
    if int(game_number) == memory_num and int(user_number) == memory_game_difficulty:
        f = MemoryGame(memory_num)
        print(f.play())
        if f.compare():
            add_score(user_number)
    elif int(game_number) == guess_num and int(user_number) == guess_game_difficulty:
        g = GuessGame(guess_num)
        print(g.play())
        if g.compare():
            add_score(user_number)
    elif int(game_number) == currency_num and int(user_number) == currency_game_difficulty:
        h = CurrencyRouletteGame(currency_num)
        print(h.play())
        if h.check_interval():
            add_score(user_number)
    else:
        print("No game available for the selection type and difficulty! Restart the game!")
