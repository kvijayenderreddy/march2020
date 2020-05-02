# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

class GoogleSearch:

    def test(self):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("http://www.google.co.in")


gs = GoogleSearch()
gs.test()


