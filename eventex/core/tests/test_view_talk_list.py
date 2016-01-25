from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Talk, Speaker


class TalkListTest(TestCase):
    def setUp(self):
        self.t1 = Talk.objects.create(title='Título da Palestra', start='10:00',
                                      description='Descrição da palestra.')
        self.t2 = Talk.objects.create(title='Título da Palestra', start='13:00',
                                      description='Descrição da palestra.')

        self.speaker = Speaker.objects.create(name='Henrique Bastos',
                                              slug='henrique-bastos',
                                              website='http://henriquebastos.net')

        self.t1.speakers.add(self.speaker)
        self.t2.speakers.add(self.speaker)

        self.resp = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (2, self.t1.title),
            (2, self.t1.description),
            (2, self.speaker.get_absolute_url()),
            (2, self.speaker.name),
            (1, self.t1.start),
            (1, self.t2.start),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_context(self):
        variables = ['morning_talks', 'afternoon_talks']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.resp.context)


class TalkListGetEmpty(TestCase):
    def test_get_empty(self):
        response = self.client.get(r('talk_list'))
        self.assertContains(response, 'Ainda não existem palestras de manhã.')
        self.assertContains(response, 'Ainda não existem palestras de tarde.')
