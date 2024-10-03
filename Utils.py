import os
from sys import platform

#The SCORES_FILE_NAME variable is a string representing a file name and the BAD_RETURN_CODE variable is a number representing a bad return code for a function.
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 442

#The function is checking the system type and then accordingly will clear the console
def screen_cleaner():
    if platform == "linux" or platform == "linux2":
        print("Linux")
        os.system('clear')
    elif platform == "win32":
        print("Windows")
        os.system('cls')

