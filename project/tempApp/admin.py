from django.contrib import admin

from .models import Member
from .models import Question
from .models import Solution


# Register your models here.
admin.site.register(Member)
admin.site.register(Question)
admin.site.register(Solution)