from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def homepage(request):
    values = request.META.items()
    values.sort()
    return render(request, 'welcome.html', {'request': request, 'values': values})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'future_datetime.html', {'offset':offset, 'future_time':dt})


def http_request_templated_view(request):
    values = request.META.items()
    values.sort()
    return render(request, 'request_view.html', {'request': request})

