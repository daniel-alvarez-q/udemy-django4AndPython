from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

sections = {
    'sports': '<h1 style="color: #ce5f2d; text-align: center">This is the sports page</h1><br><a href="http://localhost:8000">Home</a>',
    'finance': '<h1 style="color: #ce5f2d; text-align: center">This is the financial section</h1><a href="http://localhost:8000/">Home</a>',
    'politics': "Politics page"
}

def news_view(request, topic):
    try:
        result =  sections[topic]
        return HttpResponse(result)
    except:
        raise Http404("404 GENERIC ERROR") #404.html

def num_page_view(request, num_page):
    try:
        section_list = list(sections.keys())
        topic = section_list[num_page]
        print(topic)
        return HttpResponseRedirect(reverse('topic-page', args=[topic]))
    except:
        raise Http404("404 GENERIC ERROR")

# def add_view(request, num1, num2):
#     return HttpResponse(num1+num2)