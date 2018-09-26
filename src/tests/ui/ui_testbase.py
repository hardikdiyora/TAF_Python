import json
from selenium import webdriver as wb
from selenium.webdriver.support.wait import WebDriverWait

from tests.testbase import TestBase


class UITestBase(TestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        with open('/Users/hardikkumar.diyora/PycharmProjects/Automation_Task/src/config.json') as f:
            config = json.load(f)
        if config['browser'].lower() == 'chrome':
            cls.driver = wb.Chrome()
        elif config['browser'].lower() == 'firefox':
            cls.driver = wb.Firefox()
        else:
            cls.LOG.info("Browser is not specified in config.json file")
        cls.LOG.info("Opening the Browser")
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.LOG.info("Quiting the Browser")
        cls.driver.close()
        super().tearDownClass()

    def setUp(self):
        self.LOG.info("Opening the Home Page.")
        self.driver.get("https://www.ultimateqa.com/filling-out-forms/")