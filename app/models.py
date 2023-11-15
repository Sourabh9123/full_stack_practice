from django.db import models



Gender = (
    ('unknown', 'Unknown'),
    ('Male','Male'),
    ('Female','Female'),
)


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=20, choices=Gender , default='unknown')
    created_at = models.DateTimeField(auto_now_add=True)