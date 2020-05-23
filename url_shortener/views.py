from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from .forms import ShortLinkForm
from .models import ShortLink
import hashlib


def index(request):
    if request.method == 'POST':
        form = ShortLinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.short_link = hashlib.md5(link.link.encode("UTF-8")).hexdigest()[:8]
            if ShortLink.objects.filter(short_link=link.short_link):
                messages.success(request, 'http://127.0.0.1:8000/' + link.short_link)
                return redirect('index')
            link.save()
            messages.success(request, 'http://127.0.0.1:8000/'+link.short_link)
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
