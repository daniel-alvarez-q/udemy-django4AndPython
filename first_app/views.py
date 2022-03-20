from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

def simple_view(request):
    return render(request, 'first_app/example.html')

# def add_view(request, num1, num2):
#     return HttpResponse(num1+num2)