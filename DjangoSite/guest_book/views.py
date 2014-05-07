# -*- coding: utf-8 -*-
from guest_book.models import GuestBookForm, GuestBook
from django.shortcuts import render_to_response


list_comments = GuestBook.objects.all().order_by('-date')
error = 'error'


def add_comment_by_db(request):
    if request.method == 'GET':
        form = GuestBookForm(request.GET)
        form.fields['username'].required = True
        form.fields['email'].required = True
        form.fields['comment'].required = True
        if form.is_valid():
            form.save()
            return render_to_response('book/post.html', {'list_comments': list_comments})
    else:
        form = GuestBookForm()
    return render_to_response('book/index.html', {'form': form})


def list_comment_by_db(request):
    list_comment_context = {'list_comments': list_comments}
    return render_to_response('book/post.html', list_comment_context)








