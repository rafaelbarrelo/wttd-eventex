from django.conf import settings
from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Rafael Barrelo', cpf='12312312312',
                    email='rafaelbarrelo@gmail.com',
                    phone='11987654321')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = [settings.DEFAULT_FROM_EMAIL, 'rafaelbarrelo@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        itens = ['Rafael Barrelo',
                 '12312312312',
                 'rafaelbarrelo@gmail.com',
                 '11987654321']

        for item in itens:
            with self.subTest():
                self.assertIn(item, self.email.body)
