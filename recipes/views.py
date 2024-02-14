from django.shortcuts import render


def home(requests):
    return render(requests, 'recipes/home.html', context={

        'name': 'Matheus Lucas'
    })

