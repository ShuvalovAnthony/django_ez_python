import django
from django.contrib import admin
from .models import Topic, Author, Category


admin.site.register(Topic)
admin.site.register(Author)
admin.site.register(Category)