# -*- coding: utf-8 -*-
from django.test import TestCase
from guest_book.models import GuestBook


class GuestBookCase(TestCase):
    """
    тест модели Person, выполняются проверки на создание, строковое представление, сохранение удаление объекта
    """
    def setUp(self):
        """
        метод проверки создания объекта
        """
        self.book = GuestBook.objects.create(username='Sema', email='sema@test.com', comment='test')

    def tearDown(self):
        self.book = None

    def testobjectasstring(self):
        """
        метод проверки строкового представления
        """
        self.assertEqual(str(self.book), 'Sema')

    def testsaveobject(self):
        """
        метод проверки сохранения объекта
        """
        self.book.save()
        obj = GuestBook.objects.get(username='Sema', email='sema@test.com',
                                    comment='test')
        self.assertEqual(obj.username, 'Sema')
        self.assertEqual(obj.email, 'sema@test.com')
        self.assertEqual(obj.comment, 'test')

    def testdeletedbject(self):
        """
        метод проверки удаления объекта
        """
        self.book.save()
        GuestBook.objects.filter(username='Sema').delete()
        GuestBook.objects.filter(email='sema@test.com').delete()
        GuestBook.objects.filter(comment='test').delete()
