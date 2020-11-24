""""
Test case of a user login and tweet
"""

#import libraries and assets to use
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#test class
class TwitterLogin(unittest.TestCase):

#Setup webdriver (Google Chrome)
    def setUp(self):
        self.driver = webdriver.Chrome(r"Drivers/chromedriver.exe") #cambiar direccion de donde esta el webdriver ""

#test function
    def testTwitterLogin(self):
    #define the webpage to use (twitter)
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.get("https://twitter.com/login?lang=en")
    #assert that it open the correct webpage
        try:
            wait.until(EC.url_contains("twitter"))
            loadTwitter = True
        except:
            loadTwitter = False
        assert loadTwitter

    #insert username
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")))
        driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input").send_keys("*")#insert twitter username in "*"
    #Insert password
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")))
        driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input").send_keys("*") #insert password instead "*"
    #Click on log In button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='page-container']/div/div[1]/form/div[2]/button")))
        driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button").click()

    #assert that Log In is correct
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-container"]/div[1]/div[1]/div/div[1]/span/a/span/b[contains(text(), "*")]'))) #insert username without @ in "*"
            correctLogin = True
        except:
            correctLogin = False
        assert correctLogin

#Quit driver
    def tearDown(self):
        self.driver.close()


#test call
if __name__ == "__main__":
        unittest.main()


