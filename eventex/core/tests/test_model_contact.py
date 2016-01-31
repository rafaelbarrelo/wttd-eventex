from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb-pic'
        )

    def test_email(self):
        Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL, value='henrique@bastos.net')
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE, value='123123123')
        self.assertTrue(Contact.objects.exists())

    def test_choice(self):
        """Contact kind should be limeted to E or P"""
        contact = Contact.objects.create(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='henrique@bastos.net')
        self.assertEqual(contact.value, str(contact))


class ContactMangerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='henrique@bastos.net')
        s.contact_set.create(kind=Contact.PHONE, value='123456789')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['henrique@bastos.net']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phone(self):
        qs = Contact.objects.phones()
        expected = ['123456789']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
