from django.contrib import admin
from guest_book.models import GuestBook, Post


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'date', 'comment')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'text')

admin.site.register(GuestBook, GuestBookAdmin)
admin.site.register(Post, PostAdmin)

