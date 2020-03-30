"""
django 문서에서 추천하는 project 구성 순서. User 모델 확장 가능성을 염두에 두라는 얘기다.
1. $ django-admin startproject MY_PROJECT
2. $ django-admin startapp
3. accounts/models.py => 아래 코드 작성
4. settings.py => INSTALLED APPS += 'accounts'
5. settings.py => AUTH_USER_MODEL = 'accounts.User'
"""


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    followings = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='followers',
        blank=True,

    )