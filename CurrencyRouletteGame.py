# Importing our parent class and the needed python modules
from Parent_Class import Game
import random
import requests

# Defining our variables
currency_game_difficulty = 4
currency_num = 3


# Defining our child class where CurrencyRouletteGame class inherits the constructor from Parent_Class
# Initializing the object - child class. The method takes the object as its first argument (self), followed by any additional arguments that need to be
# passed to it. It will be used to call this child class with the equivalent game number.
# Equivaling the parent object's attributes from the _init_ method with the child class methods
class CurrencyRouletteGame(Game):
    def __init__(self, number):
        self.random_generated = self.get_money_interval()
        self.user_generated = self.get_guess_from_user()
        self.game_type = number
        # Calling the constructor (methods) of the parent class
        super().__init__(self.random_generated, self.user_generated, self.game_type)

    # The method will generate a random number and get the response from the API in json format
    # It iterates through the API object and append each element to a list x
    # Extracts the ILS currency, calculate what ILS currency has the generated number
    # Generates from it an interval of what the currency can be
    # Appends that interval to a list of integers v.
    def get_money_interval(self):
        self.random_generated = random.randint(1, 100)
        print(f'The computer generated numbers: {self.random_generated}')
        url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_mrpYwmr4g2hFdV5WNRQAN81P1Dcq3bPF9Tv4PchX'

        response = requests.get(url)
        res_json = response.json()
        r = res_json
        print(f'The response json response: {r}')
        for i in r.items():
            v = []
            x = list(i)
            print(f'Json to list: {x}')
            b = x[1]['ILS']
            print(f'The extracted ILS currency: {b}')
            t = b * self.random_generated
            print(f'Calculated generated number * ILS currency: {t}')
            interval = (t - (5 - currency_game_difficulty), t + (5 - currency_game_difficulty))
            for j in interval:
                v.append(int(j))
            print(f'The calculated interval: {v}')
            return v

    # The method asks the user for an input and checks if the input provided is a digit or not
    def get_guess_from_user(self):
        while True:
            self.user_generated = input("What do you think is the value of the currency from USD to ILS? :")
            if not self.user_generated.isdigit():
                print("Try again. Please enter an integer number!!")
                self.user_generated = input("What do you think is the value of the currency from USD to ILS? :")
                continue
            elif self.user_generated.isdigit():
                print({self.user_generated})
                return int(self.user_generated)
            break

    # The method calls the parent play() method
    def play(self):
        return super().play()


# This is our main function that will be executed very first in our code
if __name__ == '__main__':
    roulette_game = CurrencyRouletteGame(currency_num)
    roulette_game.play()
