from selenium.webdriver.common.by import By
class LoginPageLoc:
    _adminID_tb = (By.XPATH,"//input[@name='user_id']")
    _password_tb = (By.XPATH,"//input[@type='password']")
    _login_Button = (By.XPATH,"//button[@class='button-style']")


class HomePageLoc:
    _logout_button = (By.XPATH,"//button[text()='Logout']")
