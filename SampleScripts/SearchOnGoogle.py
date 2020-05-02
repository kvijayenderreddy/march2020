from selenium import webdriver

class TestGoogleSearch():

    def test(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\PycharmProjects\\March2020\\drivers\\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        print(self.driver.title)
        self.driver.close()


tgs = TestGoogleSearch()
tgs.test()