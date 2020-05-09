from selenium import webdriver
from selenium.webdriver.common.by import By

from SampleScripts_OR.ObjectRepo import ObjectRepository
from SampleScripts_ComUtils.CommonUtilities import ComUtils
import time

class OHRM():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\PycharmProjects\\March2020\\drivers\\chromedriver.exe")

    def loginToApplication(self, username, password):
        OR = ObjectRepository()
        CU = ComUtils()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # self.driver.find_element_by_name("txtUsername").send_keys(username)
        # self.driver.find_element_by_name("txtPassword").send_keys(password)
        # self.driver.find_element_by_name("Submit").click()

        # with Object repository
        # self.driver.find_element_by_name(OR.usernameTxt_name).send_keys(username)
        # self.driver.find_element_by_name(OR.passwordTxt_name).send_keys(password)
        # self.driver.find_element_by_name(OR.submitBtn_name).click()

        # with different way of element actions - using find_element(param1, param2)
        # self.driver.find_element(By.NAME, OR.usernameTxt_name).send_keys(username)
        # self.driver.find_element(By.NAME, OR.passwordTxt_name).send_keys(password)
        # self.driver.find_element(By.NAME, OR.submitBtn_name).click()

        # with different way of element actions - Using CommonUtilities
        CU.passTextToElement(By.NAME, OR.usernameTxt_name, username, self.driver)
        CU.passTextToElement(By.NAME, OR.passwordTxt_name, password, self.driver)
        CU.clickElements(By.NAME, OR.submitBtn_name, self.driver)
        # if(self.driver.find_element_by_id("welcome").is_displayed()):
        if(CU.checkElementDisplayed((By.ID), "welcome", self.driver) == True):
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

    def fetchGeneralInformationPageDetails(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewOrganizationGeneralInformation")
        genInfoPageVisible = self.driver.find_element_by_id("genInfoHeading").is_displayed()
        if(genInfoPageVisible == True):
            # orgName = self.driver.find_element_by_xpath("//label[@for='organization_name']").text
            # orgEmail = self.driver.find_element_by_xpath("//label[@for='organization_email']").text
            orgName = self.driver.find_element_by_id("organization_name").get_attribute("value")
            orgEmail = self.driver.find_element_by_id("organization_email").get_attribute("value")
            # orgCountry = self.driver.find_element_by_id("organization_country").get_attribute("value")
            orgCountry = self.driver.find_element_by_xpath("//option[@selected='selected']").text
            pageDetails = "Page details:\nOrganization Name: " + orgName \
                          + "\nOrganization Email: " + orgEmail \
                          + "\nOrganization Country: " + orgCountry
            # print(pageDetails)
            return pageDetails
        else:
            print("Page not loaded")
            return ""

o = OHRM()
if (o.loginToApplication("admin", "admin123")):
    # print(o.QuickStartNavigation("Abwesenheiten zuweisen"))
    # print(o.QuickStartNavigation("Abwesenheitsübersicht (pro Mitarbeiter)"))
    # print(o.QuickStartNavigation("Zeiterfassung"))
    print(o.fetchGeneralInformationPageDetails())
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

