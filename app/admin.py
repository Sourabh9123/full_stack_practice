from django.contrib import admin
from app.models import Student






class studentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender']
    list_display_links =  ['name', 'age', 'gender']


admin.site.register(Student,studentAdmin )