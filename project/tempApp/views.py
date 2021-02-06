from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def shared(request):
    return render(request, 'shared.html')
