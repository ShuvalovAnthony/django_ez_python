from django.contrib import admin
from .models import *
from django import forms
from django.utils.safestring import mark_safe
from .forms import AuthorForm


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'nickname', 'birthday', 'genre', 'country')
    list_display = ('name', 'nickname', 'birthday', 'genre', 'country')


class TopicAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'is_published', 'get_photo', 'create_time', 'update_time',)
    # search_fields =
    # list_editable 
    # list_filter
    readonly_fields = ('create_time', 'update_time', 'get_photo')
    fields = (
        'title', 'content', 'author',
        'category', 'is_published', 'photo', 'get_photo', 'update_time',
    )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="150">')

    get_photo.short_description = 'Фото'

admin.site.register(Topic, TopicAdmin)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Hashtag)
