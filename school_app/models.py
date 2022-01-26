from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'students'


class Group(models.Model):
    group_name = models.CharField(max_length=20)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.group_name} group'

    class Meta:
        verbose_name_plural = 'groups'
