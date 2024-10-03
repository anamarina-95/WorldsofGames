# Importing the files and their variables
# Importing the python module
from Utils import SCORES_FILE_NAME
import os

# Setting the path of the score file and checking if the file exists on the path
cwd = os.getcwd()
path_score = os.path.expanduser(f"{cwd}/{SCORES_FILE_NAME}")
isFile = os.path.isfile(path_score)
# print(isFile)

# The function get_sum will open the score file and will read all the scores from it, then will sum up all the values
def get_sum():
    SCORES_FILE = open(f"{path_score}", "r")
    something = SCORES_FILE.readlines()
    sum = 0
    for l in something:
        sum += int(l)
    return sum


# The function write_num is used for working with the score file. The function creates or opens the score file depending on the open_type argument provided and
# then is calculating the points of winning and appending it to the file.
def write_num(difficulty_number, open_type):
    SCORES_FILE = open(f"{path_score}", f"{open_type}")
    POINTS_OF_WINNING = str((int(difficulty_number) * 3) + 5)
    SCORES_FILE.write(POINTS_OF_WINNING + "\n")
    SCORES_FILE.close()


# The function add_score will check if the score file exists and if it doesn't exist it will create it and append the first score to the new file
# or in case the score file already exists it will append to the exiting file each score every time
def add_score(difficulty_number):
    if not isFile:
        write_num(difficulty_number, "w")
        SCORES_FILE = open(f"{path_score}", "r")
        something = SCORES_FILE.readline()
        return something
        # SCORES_FILE = open(f"{path_score}", "w")
        # POINTS_OF_WINNING = str((int(difficulty_number) * 3) + 5)
        # SCORES_FILE.write(POINTS_OF_WINNING + "\n")
        # SCORES_FILE.close()
    elif isFile:
        write_num(difficulty_number, "a")
        get_sum()
        # SCORES_FILE = open(f"{path_score}", "a")
        # POINTS_OF_WINNING = str((int(difficulty_number) * 3) + 5)
        # SCORES_FILE.write(POINTS_OF_WINNING + "\n")
        # SCORES_FILE.close()
