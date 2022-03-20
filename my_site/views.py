#Main views for the whole project will be listed here
from django.http import HttpResponse


def home(request):
    return HttpResponse(
        '<h1 style="color: #50232e; text-align: center">This is the home of our Django app!</h1><a href="http://localhost:8000/first_app/sports">Sports</a><hr><a href="http://localhost:8000/first_app/finance">Finance</a><hr><a href="http://localhost:8000/first_app/politics">Politics</a>'
    )