from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from .forms import ShortLinkForm
from .models import ShortLink

from django_url_shortener.settings import BASE_URL

import string
import random


def index(request):
    if request.method == 'POST':
        form = ShortLinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            chars = string.ascii_letters + string.digits

            while True:
                link.short_link = ''.join(random.choice(chars) for _ in range(6))
                if not ShortLink.objects.filter(short_link=link.short_link):
                    break

            data_link = ShortLink.objects.filter(link=link.link)

            if data_link:
                link.short_link = data_link[0].short_link
            else:
                link.save()

            messages.success(request, BASE_URL+link.short_link)

            return redirect('index')
    else:
        form = ShortLinkForm()

    return render(request, 'url_shortener/index.html', dict(form=form))


def short_url(request, url_id):
    try:
        full_link = ShortLink.objects.get(short_link=url_id).link
    except ObjectDoesNotExist:
        return redirect('index')
    return HttpResponseRedirect(full_link)
