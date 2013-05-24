from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def homepage(request):
    return render(request, 'welcome.html', {})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'future_datetime.html', {'offset':offset, 'future_time':dt})


def book_list(request):
    db = MySQLdb.connect(user='jacalata_sql1', db='mylittledatabase', passwd='92fbgPXB9jdwgMV', host='v0ym2lpg1o.database.windows.net:1433')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render(request, 'book_list.html', {'names': names})