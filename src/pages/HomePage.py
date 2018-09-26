from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import Locators

class Home(object):

    def __init__(self, driver, wait, LOG):
        self.driver = driver
        self.wait = wait
        self.LOG = LOG

        # Initialization of Web elements
        self.name_0 = driver.find_element(By.CSS_SELECTOR, Locators.form_0_tb)
        self.message_0 = driver.find_element(By.CSS_SELECTOR, Locators.form_0_ta)
        self.btn_0 = driver.find_element(By.CSS_SELECTOR, Locators.form_0_btn)

    def fill_name(self, name):
        self.LOG.info("Filling the Name field.")
        self.name_0.clear()
        self.name_0.send_keys(name)

    def fill_message(self, message):
        self.LOG.info("Filling the Message text area.")
        self.message_0.clear()
        self.message_0.send_keys(message)

    def fill_form_0(self, name, message):
        self.fill_name(name)
        self.fill_message(message)
        self.LOG.info("Submitting the form.")
        self.btn_0.click()

    def verify_form_0_submission(self):
        try:
            self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, Locators.form_0_success_msg)
                                                             , "Form filled out successfully"))
            return True
        except:
            return False


