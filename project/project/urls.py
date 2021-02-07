"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import tempApp.views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tempApp.views.index, name='index'),
    path('about/', tempApp.views.about, name='about'),
    path('login/', tempApp.views.login, name='login'),
    path('logout/', tempApp.views.logout, name = 'logout'),
    path('signup/', tempApp.views.signup, name='signup'),
    path('mypage/', tempApp.views.mypage, name='mypage'),
    path('question/', tempApp.views.question, name='question'),
    path('solution/', tempApp.views.solution, name='solution'),
    path('question/<int:question_id>',tempApp.views.question_detail, name='question_detail'),
    path('solution/<int:solution_id>',tempApp.views.solution_detail, name='solution_detail'),
    path('shared/', tempApp.views.shared, name='shared'),
    path('ask/', tempApp.views.ask, name='ask'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
