from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Rafael Barrelo',
            cpf='12312312312',
            email='rafaelbarrelo@gmail.com',
            phone='11-123456789',
        )
        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_contex(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        content = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)

        with self.subTest():
            for expected in content:
                self.assertContains(self.resp, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get('/inscricao/0/')
        self.assertEqual(404, resp.status_code)