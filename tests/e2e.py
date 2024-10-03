# Import the module for selenium and the module for sys so we can customize the exit code
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-search-engine-choice-screen")

cwd = os.getcwd()

# Set the url of the application in the variable
app_url = "http://localhost:30000/score_server"

# The function purpose is to test our web service. It gets the application url, open a browser, select the score element,
# check if it is a number between 1 to 1000 and return boolean if true or not
def test_scores_service(app_url):
    driver = webdriver.Chrome(options=options, service=Service(f"{cwd}/WorldofGames/chromedriver.exe"))
    driver.get(app_url)
    query = driver.find_element(By.ID, "score")
    text = query.get_attribute('innerHTML')
    # print(text)
    if int(text) >= 1 and int(text) <= 1000:
        # print("ok")
        return True
    else:
        # print("not ok")
        return False


# The function calls the test function and return -1 as an OS exit code if the test failed or 0 if it passed
def main_function():
    if test_scores_service(app_url):
        sys.exit(0)
    else:
        sys.exit(-1)


main_function()
