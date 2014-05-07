# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'Б'
        verbose_name_plural = 'Б'
        db_table = 'blog'

    def __unicode__(self):
        return self.title


class BlogPostForm(ModelForm):
    class Meta:
        models = BlogPost
        fields = ['title', 'body', 'date']
