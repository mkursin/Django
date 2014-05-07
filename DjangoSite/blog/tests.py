# -*- coding: utf-8 -*-
from django.test import TestCase
from blog.models import BlogPost


class BlogPostCase(TestCase):
    """
    тест модели BlogPost, выполняются проверки на создание, строковое представление, сохранение удаление объекта
    """
    def setUp(self):
        """
        метод проверки создания объекта
        """
        self.blog = BlogPost.objects.create(title='test', body='testing')

    def tearDown(self):
        self.blog = None

    def test_object_as_string(self):
        """
        метод проверки строкового представления
        """
        self.assertEqual(str(self.blog), 'test')

    def test_save_object(self):
        """
        метод проверки сохранения объекта
        """
        self.blog.save()
        data = BlogPost.objects.get(title='test')
        self.assertEqual(data.title, 'test')

    def test_save_body(self):
        """
        метод проверки сохранения объекта
        """
        self.blog.save()
        data = BlogPost.objects.get(body='testing')
        self.assertEqual(data.body, 'testing')

    def test_delete_title(self):
        """
        метод проверки удаления объекта
        """
        self.blog.save()
        BlogPost.objects.filter(title='test').delete()

    def test_delete_body(self):
        self.blog.save()
        BlogPost.objects.filter(body='testing').delete()



