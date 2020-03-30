from django.db import models
from faker import Faker

faker = Faker()


class Client(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ('name', )

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            cls.objects.create(name=faker.name())


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    # related_name을 안정해주면? Client 객체인 client에서  Hotel을 조회할 때 client.hotel_set.all() 이런 식으로 접근해야함. related_name을 정해주면? client.hotels.all() 이렇게 가능.
    clients = models.ManyToManyField(Client, related_name='hotels')

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            cls.objects.create(name=faker.company())


class Student(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id}: {self.name[:20]}'


class Lecture(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.title[:30]}'


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student.name}: {self.lecture.title}'
