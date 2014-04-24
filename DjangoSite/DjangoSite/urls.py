from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from guest_book.views import contact

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'messages.views.guest_book', name='guest_book'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^guest_book/', contact),

)
