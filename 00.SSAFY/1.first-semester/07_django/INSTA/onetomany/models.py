from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel # 밑에 따로 만든 TimeStamp와 같은 용도로 쓸 수 있는 모듈임


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MagazineArticle(TitleDescriptionModel, TimeStampedModel):
    content = models.TextField()


class Writer(TimeStamp):
    name = models.CharField(max_length=50, default='')


class Book(TimeStamp):
    author = models.ForeignKey(Writer, on_delete=models.PROTECT)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()


class Chapter(TitleDescriptionModel, TimeStampedModel):
    # title, description, created, modified
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Student(models.Model):
    name = models.CharField(max_length=20)


class Message(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.CharField(max_length=30)


class Reply(models.Model):
    content = models.CharField(max_length=30)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)