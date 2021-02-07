from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Member
from .models import Question
from .models import Solution

import datetime
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


# Create your views here.


def index(request):
    questions = Question.objects
    solutions = Solution.objects
    now = timezone.now()

    quests = []
    i = 0
    for q in reversed(questions.all()):
        if i == 3:
            break
        else:
            if q.matching is not None: i -= 1
            if len(q.title) >= 25:
                q.title = q.title[:25] + "..."
            q.pub_datetime = now - q.pub_datetime
            quests.append(q)
            i += 1

    sols = []
    i = 0
    for s in reversed(solutions.all()):
        if i == 3: break
        if len(s.title) >= 23: s.title = s.title[:23] + "..."
        sols.append(s)
        i += 1

    return render(request, 'index.html', {'quests': quests, 'sols': sols})


def about(request):
    return render(request, 'about.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('id', '')
        password = request.POST.get('pw', '')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['id'], password=request.POST['pw'])
        auth.login(request, user)
        myusers = Member()
        myusers.username = request.POST.get('id', '')
        myusers.password = request.POST.get('pw', '')
        myusers.birthday = request.POST.get('birth', '')
        myusers.save()
        return redirect('index')
    return render(request, 'signup.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return render(request, 'index.html')


def mypage(request):
    return render(request, 'mypage.html')


def question(request):
    questions = Question.objects
    now = datetime.datetime.now()
    return render(request, 'question.html', {'questions': questions})


def solution(request):
    solutions = Solution.objects
    return render(request, 'solution.html', {'solutions': solutions})


def question_detail(request, question_id):
    q_detail = get_object_or_404(Question, pk=question_id)
    return render(request, 'question_detail.html', {'question': q_detail})


def solution_detail(request, solution_id):
    s_detail = get_object_or_404(Solution, pk=solution_id)
    return render(request, 'solution_detail.html', {'solution': s_detail})


def shared(request):
    return render(request, 'shared.html')


def meilisearch(request):
    return render(request, 'meilisearch.html')


def ask(request):
    return render(request, 'ask.html')

