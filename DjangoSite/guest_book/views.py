# -*- coding: utf-8 -*-
from guest_book.models import GuestBookForm
from django.shortcuts import render, redirect


def contact(request):
    if request.method == 'POST':
        form = GuestBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success/')
        return render(request, 'index.html', {'form': form})
    else:
        form = GuestBookForm()
        return render(request, 'index.html', {'form': form})



