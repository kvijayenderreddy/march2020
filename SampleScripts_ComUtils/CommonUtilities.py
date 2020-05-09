

class ComUtils:

    def passTextToElement(self, identifier, identifierValue, textToPass, driver):
        driver.find_element(identifier, identifierValue).send_keys(textToPass)

    def clickElements(self, identifier, identifierValue, driver):
        driver.find_element(identifier, identifierValue).click()

    def checkElementDisplayed(self, identifier, identifierValue, driver):
        return driver.find_element(identifier, identifierValue).is_displayed()


