from django.contrib import admin

# Register your models here.
from .models import Subject, Course, Module, Content

admin.site.register(Subject)

admin.site.register(Course)

admin.site.register(Module)

admin.site.register(Content)