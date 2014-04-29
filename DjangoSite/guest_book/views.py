# -*- coding: utf-8 -*-
from guest_book.models import GuestBookForm, GuestBook
from django.shortcuts import render_to_response, render
from django.http import HttpResponse


def add_comment(request):
    if request.method == 'GET':
        value = GuestBookForm(request.GET)
        value.fields['username'].required = True
        value.fields['email'].required = True
        value.fields['comment'].required = True
        if value.is_valid():
            value.save()
            entry = GuestBook.objects.all().order_by('-date')[:5]
            context = {'entry': entry}
            return render_to_response('index.html', {'context': context})
    else:
        value = GuestBookForm()
    return render_to_response('index.html', {'value': value})
    #         return render(request, 'index.html', {'value': value})
    # else:
    #     context = GuestBook.objects.all().order_by('-date')[:5]
    #     return render_to_response('Post.html', {'context': context})


def post(request):
    return HttpResponse("Hello, world!")


def index(request):
    entry = GuestBook.objects.all().order_by('-date')[:5]
    context = {'entry': entry}
    return render_to_response('Post.html', context)





