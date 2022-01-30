from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from school_app.models import Student, Group
from .seriailizers import StudentSerializer, StudentDetailsSerializer, GroupSerializer, GroupDetailsSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404


# Create your views here.
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailsSerializer

    def get_object(self):
        return get_object_or_404(Student, pk=self.kwargs.get('student_id'))


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetails(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupDetailsSerializer
