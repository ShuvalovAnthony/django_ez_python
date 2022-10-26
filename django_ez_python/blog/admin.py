from django.contrib import admin
from .models import Topic, Author, Category, Genre, Country
from django import forms



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = []


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'nickname', 'birthday', 'genre', 'country')
    list_display = ('name', 'nickname', 'birthday', 'genre', 'country')


admin.site.register(Topic)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Author, AuthorAdmin)
