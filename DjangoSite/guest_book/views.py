# -*- coding: utf-8 -*-
from guest_book.models import GuestBookForm
from django.shortcuts import render



def add_comment(request):
    if request.method == 'GET':
        form = GuestBookForm(request.GET)
        form.fields['username'].required = True
        form.fields['email'].required = True
        form.fields['comment'].required = True
        if form.is_valid():
            form.save()

        return render(request, 'index.html', {'form': form})
    else:
        form = GuestBookForm(request.GET)
        return render(request, 'index.html', {'form': form})






