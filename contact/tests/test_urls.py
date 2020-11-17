from django.test import SimpleTestCase
from django.urls import resolve, reverse
from contact.views import ContactView

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func.view_class, ContactView)
