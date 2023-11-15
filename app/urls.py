from django.urls import path
from app.views import student_view, deletestudent

urlpatterns = [
    path('students/',student_view, name='Students'),
    path('students/<int:pk>/',deletestudent, name='deletestudent'),
]
