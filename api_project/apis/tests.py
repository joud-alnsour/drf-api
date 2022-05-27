from django.test import TestCase
from .models import Api

# Testing the model
class ApiTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testapi = Api.objects.create(title = "test_api", description="Testing api")
        testapi.save()


    def test_apis_model(self):
        api = Api.objects.get(id=1)
        actual_title = api.title
        self.assertEqual(actual_title, "test_api")
