from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def mypage(request):
    return render(request, 'mypage.html')


def question(request):
    return render(request, 'question.html')


def solution(request):
    return render(request, 'solution.html')


def shared(request):
    return render(request, 'shared.html')
