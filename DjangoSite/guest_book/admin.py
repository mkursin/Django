from django.contrib import admin
from guest_book.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'date', 'comment')

admin.site.register(GuestBook, GuestBookAdmin)
