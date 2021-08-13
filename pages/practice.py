import time
from selenium.webdriver.common.by import By
from settings import driver, url
from loc import locators
from selenium.common.exceptions import NoSuchElementException

driver.get(url)
driver.maximize_window()
driver.implicitly_wait(1)

class Login():

    def find_element(self,locator_type,locator_value):
        try:
            webeleref = driver.find_element(locator_type, locator_value)
            return webeleref
        except NoSuchElementException:
            print("no ele", NoSuchElementException)
