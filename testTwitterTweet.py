""""
Test case of a user login and tweet
"""

#import libraries and assets to use
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#test class
class TwitterTweet(unittest.TestCase):

#Setup webdriver (Google Chrome)
    def setUp(self):
        self.driver = webdriver.Chrome(r"/home/rogerdavila/PycharmProjects/untitled/Drivers/chromedriver.exe") #change the webdriver direction depending in where is located ""

#test function
    def testTwitterTweet(self):
        #define the webpage to use (twitter)
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.get("https://twitter.com/login?lang=en")
        # assert that it open the correct webpage
        try:
            wait.until(EC.url_contains("twitter"))
            loadTwitter = True
        except:
            loadTwitter = False
        assert loadTwitter

        # insert username
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")))
        driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input").send_keys("*")  # insert twitter username in "*"
        # Insert password
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")))
        driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input").send_keys("*")  # insert password in "*"
        # Click on log In button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='page-container']/div/div[1]/form/div[2]/button")))
        driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button").click()

        # assert that Log In is correct
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="page-container"]/div[1]/div[1]/div/div[1]/span/a/span/b[contains(text(), "*")]')))  # insert username without @ in "*"
            correctLogin = True
        except:
            correctLogin = False
        assert correctLogin

        #click on tweet button (start tweet)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='global-new-tweet-button']")))
        driver.find_element_by_xpath("//*[@id='global-new-tweet-button']").click()

    #Insert tweet msg
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='Tweetstorm-tweet-box-0']/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]")))
        tweetBox = driver.find_element_by_xpath("//*[@id='Tweetstorm-tweet-box-0']/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]")
        tweetBox.send_keys("Tweet Trial from Selenium!!!") #input tweet msg instad of "Tweet Trial from Selenium"
        tweetBox.send_keys(Keys.RETURN)
    #click on tweet (send tweet)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='Tweetstorm-tweet-box-0']/div[2]/div[2]/div[2]/span/button[2]")))
        driver.find_element_by_xpath("//*[@id='Tweetstorm-tweet-box-0']/div[2]/div[2]/div[2]/span/button[2]").click()

    #wait to tweet to be sent
        try:
            wait.until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='message-drawer']/div"), "Tweet was sent."))
            sentTweet = True
        except:
            sentTweet = False
        assert sentTweet


    #Quit driver
    def tearDown(self):
        self.driver.close()


#llamada al test
if __name__ == "__main__":
    unittest.main()
