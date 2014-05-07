# -*- coding: utf-8 -*-
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost


def archive_blog_db(request):
    posts = BlogPost.objects.all().order_by('-date')
    t = loader.get_template('blog/index.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))







