from django.shortcuts import render
from django.http import HttpResponse

from books.models import Book
# Create your views here.


def book_list(request):
    #db = MySQLdb.connect(user='jacalata_sql1', db='mylittledatabase', passwd='92fbgPXB9jdwgMV', host='v0ym2lpg1o.database.windows.net:1433')
    #cursor = db.cursor()
    #cursor.execute('SELECT name FROM books ORDER BY name')
    #names = [row[0] for row in cursor.fetchall()]
    #db.close()
    #return render(request, 'book_list.html', {'names': names})
    books = Book.objects.order_by('title')
    return render(request, 'book_list.html', {'books': books})


def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                {'books': books, 'query': q})
    return render(request, 'search_form.html',
        {'error': error})