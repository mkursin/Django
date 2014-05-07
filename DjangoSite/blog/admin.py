from django.contrib import admin
from blog.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'date')

admin.site.register(BlogPost, BlogPostAdmin)




