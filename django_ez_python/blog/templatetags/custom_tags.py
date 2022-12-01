from django import template
from ..models import Topic, Genre, Author

register = template.Library()


@register.filter
def upper(value):
    return value.upper()


@register.filter(is_safe=True)
def underscore(value):
    return value.replace(' ', '_')


@register.simple_tag(name='authors_topics')
def authors_topics(id=1):
    return Topic.objects.filter(author=id)


@register.simple_tag
def all_authors(name='all_authors'):
    return Author.objects.all()