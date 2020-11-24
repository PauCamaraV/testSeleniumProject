#first selenium test
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SearchHS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"Drivers/chromedriver.exe") #cambiar direccion de donde esta el webdriver ""

    def testSearchHS(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("Harry Styles")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.find_element_by_xpath("//*[@id='hdtb-msb-vis']/div[2]/a").click()
        picHS = driver.find_element_by_xpath('//*[@id="ECu7WDohszAjYM:"]')
        ActionChains(driver).move_to_element(picHS).perform()
        picHS.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='irc_cc']/div[2]/div[3]/div[1]/div/table[1]/tbody/tr/td[1]/a")))
        driver.find_element_by_xpath("//*[@id='irc_cc']/div[2]/div[3]/div[1]/div/table[1]/tbody/tr/td[1]/a").click()
        time.sleep(2)
        # close the tab
        driver.close()
        time.sleep(2)
        # switch to the main window
        driver.switch_to.window(driver.window_handles[0])


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
