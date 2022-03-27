#Main views for the whole project will be listed here
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'base.html')

def not_found_error_view (request,exception): 
    return render (request, 'error_view.html', status=404)