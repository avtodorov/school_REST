from django.contrib import admin
from django.urls import path
from school_app import views

urlpatterns = [
    path('students/', views.StudentList.as_view(), name='StudentList'),
    path('students/<int:student_id>', views.StudentDetails.as_view(), name='StudentDetails'),
    path('groups/', views.GroupList.as_view(), name='GroupList'),
    path('groups/<int:group_id>', views.GroupDetails.as_view(), name='GroupDetails'),
]
