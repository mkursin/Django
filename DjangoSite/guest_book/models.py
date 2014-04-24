# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm


class GuestBook(models.Model):
    username = models.CharField(verbose_name='Ник', max_length=30, blank=True)
    email = models.EmailField(blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', editable=False)
    comment = models.TextField(verbose_name='Комментарий', blank=True)

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
        db_table = 'guest_book'

    def __unicode__(self):
        return '%s' % self.comment


class GuestBookForm(ModelForm):
    class Meta:
        model = GuestBook
        fields = ['username', 'email', 'comment']
