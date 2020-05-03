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

    def QuickStartNavigation(self, subSectionText):
        self.driver.find_element_by_xpath("//span[text()='"+subSectionText+"']").click()
        time.sleep(3)
        pageHeading = self.driver.find_element_by_xpath("//div[@class='head']/h1").text
        self.driver.find_element_by_id("menu_dashboard_index").click()
        # print(pageHeading)
        return pageHeading

    def logout(self):
        self.driver.find_element_by_id("welcome").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@href='/index.php/auth/logout']").click()
        if(self.driver.find_element_by_name("txtUsername").is_displayed()):
            print("User LOGGED OUT Successfully")
            return True
        else:
            print("User Could NOT LOGOUT of the application")
            return False

o = OHRM()
if (o.loginToApplication("admin", "admin123")):
    print(o.QuickStartNavigation("Abwesenheiten zuweisen"))
    print(o.QuickStartNavigation("Abwesenheitsübersicht (pro Mitarbeiter)"))
    print(o.QuickStartNavigation("Zeiterfassung"))
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

'''
selenium assignment :1
login
click on Assign Leave > get the page heading > Go back to Dashboard
click on Leave List > get the page heading > Go back to Dashboard
click on Timesheet > get the page heading > Go back to Dashboard
logout

selenium assignment :2
Login with Invalid Credentials and capture the login failure message

Selenium assignment 3:
Navigatre to below page and extract the fieldNames and their corresponding input values
https://opensource-demo.orangehrmlive.com/index.php/admin/viewOrganizationGeneralInformation



'''

