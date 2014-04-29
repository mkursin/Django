# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm


class GuestBook(models.Model):
    """
    модель отзывов
    """
    # id = models.IntegerField(verbose_name='№ комментария', editable=False, primary_key=True, auto_created=True)
    username = models.CharField(verbose_name='Имя', max_length=30, blank=True)
    email = models.EmailField(blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', editable=False)
    comment = models.CharField(verbose_name='Комментарий', blank=True, max_length=255, unique=True)

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
        db_table = 'guest_book'
        app_label = 'commentsbyguest'

    def __unicode__(self):
        return self.username


class GuestBookForm(ModelForm):
    """
    форма модели отзывов
    """
    class Meta:
        model = GuestBook
        fields = ['username', 'email', 'comment']


class Post(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False, verbose_name='№ поста')
    name = models.CharField(max_length=30, verbose_name='Имя')
    date = models.DateTimeField(verbose_name="Время написания", auto_now_add=True)
    text = models.TextField(verbose_name='Пост', max_length=100000)

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
        db_table = 'post_from_blog'

    def __unicode__(self):
        return self.name


class PostForm(ModelForm):

    class Meta:
        models = Post
        fields = ['id', 'name', 'date', 'text']