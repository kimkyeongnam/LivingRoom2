from django.db import models

# Create your models here.

class Member(models.Model):
  username = models.CharField(max_length=30, unique=True, blank=False, null=False)
  password = models.CharField(max_length=30, blank=False, null=False)
  birthday = models.DateField(blank=False, null=False)

  def __str__(self):
        return self.username

class Question(models.Model):
  title = models.CharField(max_length=100, blank=False, null=False)
  contents = models.TextField(blank=False, null=False)
  writer = models.ForeignKey('Member', on_delete=models.SET_DEFAULT, default="탈퇴한 회원", db_column='writer')
  pub_datetime = models.DateTimeField(auto_now_add=True)
  image1 = models.ImageField(upload_to='images/', null=True, blank=True, default=None)
  image2 = models.ImageField(upload_to='images/', null=True, blank=True, default=None)
  fee = models.PositiveIntegerField()
  matching = models.CharField(max_length=30, unique=True, null=True, blank=True, default=None)

  def __str__(self):
        return self.title

class Solution(models.Model):
  title = models.CharField(max_length=100, blank=False, null=False)
  writer = models.ForeignKey('Member', on_delete=models.SET_DEFAULT, default="탈퇴한 회원", db_column='writer')
  q_no = models.ForeignKey('Question', on_delete=models.CASCADE, db_column='q_no')       ## 답변완료된 질문은 삭제되지 않음
  video = models.FileField(upload_to='videos/')
  pub_datetime = models.DateTimeField(auto_now_add=True)
  fee = models.IntegerField()

  def __str__(self):
        return self.title

