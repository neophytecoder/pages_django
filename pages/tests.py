from django.test import TestCase, SimpleTestCase

# Create your tests here.
class PageTests(SimpleTestCase):
    def test_page(self):
        response = self.client.get("/page/")
        self.assertEquals(response.status_code, 200)

    def test_page_about(self):
        response = self.client.get("/page/about/")
        self.assertEquals(response.status_code, 200)
