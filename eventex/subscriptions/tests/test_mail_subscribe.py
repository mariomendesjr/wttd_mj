from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Mario Junior', cpf='12345678901',
                    email='mariojfmendesjr@gmail.com', phone='41-98815-3035')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'mariojfmendesjr@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_body(self):
        contents = [
            'Mario Junior',
            '12345678901',
            'mariojfmendesjr@gmail.com',
            '41-98815-3035'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
