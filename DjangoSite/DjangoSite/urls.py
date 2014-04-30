# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from guest_book.views import add_comment_by_db

urlpatterns = patterns('',
    # Examples:

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_comment/', add_comment_by_db),
    # url(r'^post/', post),
    # url(r'^list_comments', list_comment_by_db, name='Список комментариев')


)
