import requests as req

from tests.api.api_testbase import APITestBase


class UsersAPITest(APITestBase):

    def setUp(self):
        self.url = self.baseURI + "/users"

    def test_users_endpoint(self):
        self.LOG.info("Verify the /users endpoint GET request result")
        response = req.request('GET', self.url)
        assert response.status_code == 200
        res_data = response.json()
        for item in res_data:
            if item['company']['name'].endswith('Group'):
                self.LOG.info(item['company']['name'])
        assert response.elapsed.total_seconds() * 1000 < 200
