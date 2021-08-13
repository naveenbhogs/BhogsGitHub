from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self,driver):
        self.driver = driver
        print("in base page")
    #def __logoutbutton(self):
        #return self.find_element(By.XPATH,"//button[text()='Logout']")

    def find_element(self,locator_type,locator_value):
        try:
            webeleref = self.driver.find_element(locator_type,locator_value)
            return webeleref
        except NoSuchElementException:
            print("no ele",NoSuchElementException)

    def click_on_logoutbutton(self):
        self.__logoutbutton().click()
