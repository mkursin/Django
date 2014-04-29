from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from guest_book.views import add_comment, post, index

urlpatterns = patterns('',
    # Examples:

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^guest_book/', add_comment),
    url(r'^post/', post),
    url(r'^pool/', index),

)
