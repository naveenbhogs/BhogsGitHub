from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class TaskPage(BasePage):
    __newTask=(By.XPATH,"//button[contains(@class,'button-style')]")
    __users=(By.XPATH,"//span[@class='title-0-2-7 title-d7-0-2-15']")

    def clickOnNewTask(self):
        self.Find_element(*self.__newTask).click()
        self.Find_element(*self.__users).click
