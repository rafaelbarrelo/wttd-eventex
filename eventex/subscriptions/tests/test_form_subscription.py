from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_cpf_is_digit(self):
        """CPF most only accept digits"""
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        exception = errors[field][0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, message):
        errors_list = form.errors[field]
        self.assertListEqual([message], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Rafael Barrelo', cpf='12312312312',
                     email='rafaelbarrelo@gmail.com', phone='123123123')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()

        return form
