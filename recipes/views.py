from django.http import HttpResponse
from django.shortcuts import render


def home(requests):
    return render(requests, 'recipes/home.html', context={

        'name': 'Matheus Lucas'
    })


def contato(requests):
    return requests(requests, 'me-apague/temp.html')

def sobre(requests):
    return HttpResponse('sobre 3')

