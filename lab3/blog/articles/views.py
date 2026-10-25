from django.shortcuts import render
from .models import Advert


def archive(request):
    return render(request, 'archive.html', {"posts": Advert.objects.all()})
