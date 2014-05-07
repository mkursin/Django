# -*- coding: utf-8 -*-
from django.conf.urls import patterns,  url
from blog.views import archive_blog_db

urlpatterns = patterns('', url(r'^$', archive_blog_db),)
