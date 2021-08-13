from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from pages.taskPage import TaskPage

class HomePage(BasePage):

    def __logoutbutton(self):
        return self.find_element(By.XPATH,"//button[text()='Logout']")

    __newTask=(By.XPATH,"//button[contains(@class,'button-style')]")

    def navigateToTask(self):
        self.find_element(*self.__newTask).click()
        self.find_element(*self.__users).click()
        return TaskPage(self.driver)

    def clickLogoutlink(self):
        self.__logoutbutton().click()