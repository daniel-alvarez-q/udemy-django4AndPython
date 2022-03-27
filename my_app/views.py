from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def example_view(request):
    return render(request, 'my_app/example.html')

def variable_view(request):

    my_var = {
        'key1': 'value2',
        'key2': ['item1', 'item2', 'item3'],
        'key3': {'iKey1': 'iValue1', 'iKey2': ['iValue2', 'iValue3']},
        'user_logged_in': False
    }

    return render(request, 'my_app/variable.html', context=my_var)
