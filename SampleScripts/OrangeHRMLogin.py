from selenium import webdriver
import time

class OHRM():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\PycharmProjects\\March2020\\drivers\\chromedriver.exe")

    def loginToApplication(self, username, password):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys(username)
        self.driver.find_element_by_name("txtPassword").send_keys(password)
        self.driver.find_element_by_name("Submit").click()
        if(self.driver.find_element_by_id("welcome").is_displayed()):
            print("User Logged in Successfully")
            return True
        else:
            print("User Could not login to the application")
            return False


    def logout(self):
        self.driver.find_element_by_id("welcome").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Logout").click()
        if(self.driver.find_element_by_name("txtUsername").is_displayed()):
            print("User LOGGED OUT Successfully")
            return True
        else:
            print("User Could NOT LOGOUT of the application")
            return False

'''
selenium assignment :1
login
click on Assign Leave > get the page heading > Go back to Dashboard
click on Leave List > get the page heading > Go back to Dashboard
click on Timesheet > get the page heading > Go back to Dashboard
logout

selenium assignment :2
Login with Invalid Credentials and capture the login failure message

'''


o = OHRM()
if (o.loginToApplication("ad", "admin123")):
    o.logout()
else:
    print(">>> Login Unsuccessful")

# o.loginToApplication()
# o.logout()

'''
identifiers:
id
class
name
cssselector
xpath
linktext
partiallinktext
'''
