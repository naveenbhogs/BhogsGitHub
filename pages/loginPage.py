import time
from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from settings import driver, url

driver.get(url)
driver.maximize_window()
driver.implicitly_wait(1)

class First():

    def display():
        # driver.get(url)
        # driver.maximize_window()
        # driver.minimize_window()
        # driver.fullscreen_window()
        print("the current URL of the page", driver.current_url)
        print("The tittle is ", driver.title)
        # driver.close()

    #display()



    def login():
        usernamestr = "admin123"
        passwordstr = "admin123"
        usr = driver.find_element_by_xpath("//input[@name='user_id']")
        usr.send_keys(usernamestr)
        pwd = driver.find_element_by_xpath("//input[@type='password']")
        pwd.send_keys(usernamestr)
        butn = driver.find_element_by_xpath("//button[@class='button-style']")
        butn.click()
        #print("login succsessfully by ", usernamestr)
        # driver.close()

    #login()

    def users():
        users = driver.find_element_by_xpath("//span[contains(text(),'Users')]")
        users.click()
        print("Clicked")

    #users()

    def Coaches():
        users = driver.find_element_by_xpath("//span[contains(text(),'Coaches')]")
        users.click()
        print("Clicked")

    #Coaches()

    def logout():
        logoutbtn = driver.find_element_by_xpath("//button[text()='Logout']")
        logoutbtn.click()
        print("logout")

    #logout()
    @classmethod
    def navigateToHomePage(self):
        self.EnterUsername(un)
        self.EnterPassword(pwd)
        self.clickLogin()
        return logout()