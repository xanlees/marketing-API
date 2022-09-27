from .test_setup import TestSetUp
from rest_framework import status

class TestViews(TestSetUp):

    

    def test_product_can_be_added(self):
        url = self.product_url
        res= self.client.post(url, self.product_data, format='json')
        print (res.content)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    # def test_product_can_be_listed(self):
    #     url = self.product_url
    #     res= self.client.get(url)

    #     self.assertEqual(res.status_code, status.HTTP_200_OK)