from django import template
from ..models import Topic

register = template.Library()


@register.filter
def upper(value):
    return value.upper()


@register.filter
def underscore(value):
    return value.replace(' ', '_')


@register.simple_tag(name='authors_topics')
def authors_topics(id=1):
    return Topic.objects.filter(author=id)