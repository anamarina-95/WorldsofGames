# Defining our parent class and initialize it with the arguments needed
class Game:
    def __init__(self, random_generated, user_generated, game_type):
        self.random_generated = random_generated
        self.user_generated = user_generated
        self.game_type = game_type

    # The compare() method compares the two arguments results and returns True or False
    def compare(self):
        if self.random_generated == self.user_generated:
            print("You won!")
            return True
        else:
            print("You lost!")
            return False

    # The check_interval() method checks if the user_generated argument result is in the range of the random_generated argument result
    def check_interval(self):
        if self.user_generated in range(*self.random_generated):
            print("You won!")
            return True
        else:
            print("You lost!")
            return False

    # The play() method calls the above needed method based on the type of game number.
    def play(self):
        if self.game_type == 1 or self.game_type == 2:
            return self.compare()
        elif self.game_type == 3:
            return self.check_interval()
