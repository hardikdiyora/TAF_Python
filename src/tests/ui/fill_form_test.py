from time import sleep

from pages.HomePage import Home
from tests.ui.ui_testbase import UITestBase


class FillFormTest(UITestBase):

    def setUp(self):
        super().setUp()
        self.LOG.info("Navigate to Home page.")
        self._homePage = Home(self.driver, self.wait, self.LOG)

    def test_fill_form(self):
        self.LOG.info("Verify User is able to submit the form 0")
        self._homePage.fill_form_0(name="Hardik", message="Hello ! How are you?")
        assert self._homePage.verify_form_0_submission() == True