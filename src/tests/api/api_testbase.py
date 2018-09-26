from tests.testbase import TestBase


class APITestBase(TestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.LOG.info("Setting up the Base URI.")
        cls.baseURI = "https://jsonplaceholder.typicode.com"