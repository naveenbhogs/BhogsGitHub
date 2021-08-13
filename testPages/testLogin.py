from pages.loginPageNew import LoginPage
from testPages.baseTest import BaseTest
import unittest


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = BaseTest()
        cls.driver = cls.base.start_browser("chrome", "http://13.126.93.28/#/")

    def test_login(self):
        login = LoginPage(self.driver)
        home = login.navigateToHomePage("admin123","admin123")
        home.clickLogoutlink()

    @classmethod
    def tearDownClass(cls):
        cls.base.stop_browser()


if __name__ == "__main__":
    unittest.main()
