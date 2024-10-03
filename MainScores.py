# Importing the files and they variables/functions
# Importing the libraries and their methods
# Importing the python modules
from Scores import get_sum, cwd
from Utils import BAD_RETURN_CODE
from flask import Flask, render_template
import os

# Setting the variables that get the current working directory and the path for the index.html file
path = f'{cwd}/templates'
app = Flask(__name__)

# Storing the results fo the score calculation in the SCORE variable
SCORE = get_sum()


# Setting the url for our score to show on /score_server . The function will check if the templates folder exists, in case it doesn't then it will create it.
# It will create then the index.html file used to show the score
@app.route("/score_server", methods=['GET', 'POST'])
def score_server():
    if not os.path.exists(path):
        os.makedirs(path)
    h = open(f"{cwd}/templates/index.html", "w")
    h.writelines("<html>\n"
                "\n<head>"
                "\n<title>Scores Game</title>"
                "\n<head>"
                "\n<body>"
                f"\n<h1 style='text-align:center'>The score is<div id='score' style='color:blue ; text-align:center'>{SCORE}</div></h1>"
                "\n</body>"
                "\n</html>")
    h.close()
    return render_template("index.html")

# In case there is any issue the handle_error function will get the error and will overwrite it in a way readable for the user
@app.errorhandler(Exception)
def handle_error(error):
    error = BAD_RETURN_CODE
    h = open(f"{cwd}/templates/index.html", "w")
    h.writelines("<html>\n"
                "\n<head>"
                "\n<title>Scores Game</title>"
                "\n<head>"
                "\n<body>"
                f"\n<h1><div id='score' style='color:red ; text-align: center;'>Error : {BAD_RETURN_CODE}</div></h1>"
                "\n</body>"
                "\n</html>")
    h.close()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=30000, debug=True)
