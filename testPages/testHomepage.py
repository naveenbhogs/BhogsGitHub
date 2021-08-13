from selenium import  webdriver
from pages.loginPageNew import LoginPage
from pages.homePage import HomePage
from testPages.baseTest import BaseTest
import unittest
class TestLogout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = BaseTest ( )
        cls.driver = cls.base.start_browser ("chrome", r"B:\softwares\Strongerme\driver\chromedriver.exe")
    def test_Login(self):
        logout = HomePage()

    @classmethod
    def tearDownClass(cls):
        cls.base.stop_browser()
#base = BasePage()
#driver = base.start_browser("chrome",r"B:\sel\Selenium notes\yogesh sel\simplePomFramework\drivers\chromedriver.exe")

#login =LoginPage(driver)
#login.EnterAdminName(admin123)
#login.EnterPassword(admin123)
#login.clickLogin()

#logout = HomePage(driver)
#logout.clickLogoutlink()

if __name__=="__main__":
    unittest.main()
