# Importing our parent class and the needed python modules
from Parent_Class import Game
from Utils import screen_cleaner
import random
import time

# Defining our variables
memory_game_difficulty = 3
memory_num = 1


# Defining our child class where MemoryGame class inherits the constructor from Parent_Class
# Initializing the object - child class. The method takes the object as its first argument (self), followed by any additional arguments that need to be
# passed to it. It will be used to call this child class with the equivalent game number.
# Equivaling the parent object's attributes from the _init_ method with the child class methods
class MemoryGame(Game):
    def __init__(self, number):
        self.random_generated = self.generate_sequence()
        self.user_generated = self.get_list_from_user()
        self.game_type = number
        super().__init__(self.random_generated, self.user_generated, self.game_type)

    # The method generates a series of numbers between a specified range and it displays it for 0.7 seconds
    def generate_sequence(self):
        self.random_generated = random.sample(range(1, 101), memory_game_difficulty)
        #The function will show the random generated number for only 0.7 seconds and then will clear the screen
        def temp_print(val):
            print(val)
            time.sleep(0.7)
            screen_cleaner()
        temp_print(self.random_generated)
        return self.random_generated


    # The method asks the user for an input, checks if the input is digit or not and if is separated by comma.
    # If the input is valid then gets every string user input and splits it at the comma.
    # Then creates a list of integers of the user input and checks if the length of the list is equal to the game difficulty.
    def get_list_from_user(self):
        self.user_generated = input(f"Please enter a list of {memory_game_difficulty} numbers:")
        while True:
            for i in self.user_generated:
                if not i.isdigit():
                    print("Try again. Input is not a digit separated by comma!")
                    self.user_generated = input(f"Please enter a list of {memory_game_difficulty} numbers:")
                    break
                elif i.isdigit():
                    str_list = self.user_generated.split(",")
                    try:
                        new_list = list(map(int, str_list))
                        if not len(new_list) == memory_game_difficulty:
                            print('Please try again, with only numbers separated by commas (e.g. "1, 5, 3")')
                            self.user_generated = input(f"Please enter a list of {memory_game_difficulty} numbers:")
                        else:
                            return new_list
                        break
                    except ValueError:
                        print("Try again. Only integers accepted. Input is not a digit separated by comma!")
                        self.user_generated = input(f"Please enter a list of {memory_game_difficulty} numbers:")
                break

    # The method the parent play() method
    def play(self):
        return super().play()


# This is our main function that will be executed very first in our code
if __name__ == '__main__':
    memory_game = MemoryGame(memory_num)
    memory_game.play()
