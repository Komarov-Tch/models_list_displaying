import datetime as dt

from django.shortcuts import render

from books.models import Book


def books_date_view(request, pub_date):
    year = int(pub_date.split('-')[0])
    month = int(pub_date.split('-')[1])
    day = int(pub_date.split('-')[2])
    date_book = dt.date(year=year, month=month, day=day)
    book = Book.objects.filter(pub_date=date_book)
    template = 'books/date_list.html'

    forvard_date = Book.objects.values('pub_date').distinct().order_by('pub_date').filter(pub_date__gt=date_book)
    if forvard_date:
        forvard_date = str(forvard_date[0]['pub_date'])
    back_date = Book.objects.values('pub_date').distinct().order_by('pub_date').filter(pub_date__lt=date_book)
    if back_date:
        back_date = str(back_date[len(back_date) - 1]['pub_date'])
    context = {'books': book,
               'forvard_date': forvard_date,
               'back_date': back_date,
               }
    return render(request, template, context)


def books_view(request):
    books = Book.objects.all()

    template = 'books/date_list.html'
    context = {'books': books}
    return render(request, template, context)
