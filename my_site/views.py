#Main views for the whole project will be listed here
from django.http import HttpResponse


def home(request):
    return HttpResponse(
        '<h1 style="color: #50232e; text-align: center">This is the home of our Django app!</h1>'
    )