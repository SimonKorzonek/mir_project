from django.test import SimpleTestCase
from contact.forms import ContactForm

class TestForm(SimpleTestCase):
    def test_contact_valid_data(self):
        form = ContactForm(data={
            'email':'email@email.com',
            'name':'name',
            'content':'content'})
        self.assertTrue(form.is_valid())

    def test_contact_no_data(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)