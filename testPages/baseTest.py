from selenium import  webdriver
chromePath=r"B:\softwares\Strongerme\driver\chromedriver.exe"
ApplicationUrl="http://13.126.93.28/#/"
class BaseTest():
    def __init__(self):
        self.driver =None

    def start_browser(self,browserName,ApplicationUrl):
        if browserName.lower()=="chrome":
            self.driver = webdriver.Chrome(executable_path=chromePath)
        elif browserName.lower()=="firefox":
            self.driver = webdriver.Firefox(executable_path="")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(url=ApplicationUrl)
        return self.driver

    def stop_browser(self):
        self.driver.quit()
