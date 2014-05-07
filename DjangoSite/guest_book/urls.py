# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from guest_book.views import add_comment_by_db, list_comment_by_db

urlpatterns = patterns('',
    # Examples:
    url(r'add_comment', add_comment_by_db),
    url(r'list_comment', list_comment_by_db),
)