from http import client
from unicodedata import name
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient
from rest_framework import status
from faker import Faker
import json

class TestSetUp(APITestCase, TenantTestCase):
    @classmethod
    def setup_tenant(cls, tenant):
        tenant.name = "public"
        tenant.paid_until = "2022-12-31"
        tenant.on_trial = False
        tenant.is_active = True
        return tenant

    def setUp(self):
        self.fake = Faker()
        self.client = TenantClient(self.tenant)
        self.product_url = reverse('product')
        self.product_data =  {
            "translations": json.dumps({
                "en":{
                    "name": self.fake.name(),
                    "description": self.fake.paragraph()
                }
            }),
            "user": 1,
            "price": 100000
        }
        self.register(self.client)
        return super(). setUp()

    def register(self, client):
        register_url = reverse('auth_register')
        user_data = {
            'username': self.fake.first_name(),
            'password': self.fake.password(),
            'email': self.fake.email(),
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name()
        }
        res = client.post(register_url, user_data, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def tearDown(self):
        return super().tearDown()
