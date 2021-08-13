from loc.locators import LoginPageLoc
from pages.basePage import BasePage
from pages.homePage import HomePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    _adminID_tb = (By.XPATH, "//input[@name='user_id']")
    _password_tb = (By.XPATH, "//input[@type='password']")
    _login_Button = (By.XPATH, "//button[@class='button-style']")

    def __adminID_Tb(self):
        return self.find_element(*self._adminID_tb)
    def __password_Tb(self):
        return self.find_element(*self._password_tb)
    def __login(self):
        return self.find_element(*self._login_Button)

    def EnterAdminName(self,admin123):
        self.__adminID_Tb().send_keys(admin123)

    def EnterPassword(self,admin123):
        self.__password_Tb().send_keys(admin123)

    def clickLogin(self):
        self.__login().click()

    def navigateToHomePage(self,adminname,pwd):
        self.EnterAdminName(adminname)
        self.EnterPassword(pwd)
        self.clickLogin()
        return HomePage(self.driver)



