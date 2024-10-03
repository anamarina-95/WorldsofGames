# Importing our parent class and the needed python modules
from Parent_Class import Game
import random

# Defining our variables
guess_game_difficulty = 5
guess_num = 2


# Defining our child class where GuessGame class inherits the constructor from Parent_Class
# Initializing the object - child class. The method takes the object as its first argument (self), followed by any additional arguments that need to be
# passed to it. It will be used to call this child class with the equivalent game number.
# Equivaling the parent object's attributes from the _init_ method with the child class methods
class GuessGame(Game):
    def __init__(self, number):
        self.random_generated = self.generate_number()
        self.user_generated = self.get_guess_from_user()
        self.game_type = number
        super().__init__(self.random_generated, self.user_generated, self.game_type)

    # The method generates a number between a specified range
    def generate_number(self):
        rand = random.randint(1, guess_game_difficulty)
        print(rand)
        return rand

    # The method ask the user for input and checks if the input is a digit and if it is between the specified range
    def get_guess_from_user(self):
        while True:
            self.user_generated = input(f"Choose a number between 1 to {guess_game_difficulty}:")
            if not self.user_generated.isdigit() or int(self.user_generated) not in range(1, 8):
                continue
            elif self.user_generated.isdigit() and int(self.user_generated) in range(1, 8):
                return int(self.user_generated)
            break

    # The method calls the parent play() method
    def play(self):
        return super().play()


# This is our main function that will be executed very first in our code
if __name__ == '__main__':
    guess_game = GuessGame(guess_num)
    guess_game.play()
