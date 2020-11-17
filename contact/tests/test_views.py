from django.test import TestCase, Client
from django.urls import reverse
from contact.models import ContactRequest

class TestViews(TestCase):
    def test_contact(self):
        ContactRequest.objects.create(email='email@email.com')
        response = self.client.post(reverse('contact'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(ContactRequest.objects.first().email, 'email@email.com' )

    def test_contact_no_data(self):
        response = self.client.post(reverse('contact'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(ContactRequest.objects.count(), 0)