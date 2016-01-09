from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModel(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Rafael Barrelo',
            phone='11-123123123',
            email='rafaelbarrelo@gmail.com',
            cpf='12312312312'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)
