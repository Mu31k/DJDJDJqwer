from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    conter = {'qw': 'qwerty',
             'r': '1231232432423423423',
             }

    return render(request, 'polls/index.html', conter)


def about(request):
    return render(request, 'polls/about.html')