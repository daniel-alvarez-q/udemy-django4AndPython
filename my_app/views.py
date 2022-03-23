from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def example_view(request):
    return render(request, 'my_app/example.html')

def variable_view(request):

    my_var = {
        'key1': 'value2',
        'key2': ['item1', 'item2'],
        'key3': {'innerKey1': 'innerValue2'}
    }

    return render(request, 'my_app/variable.html', context=my_var)
