from django.shortcuts import render
from .models import Author, Category, Topic, Genre
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView



def blog_home(request):
    return render(request, 'blog/blog_home.html')


class TopicListView(ListView):
    model = Topic
    template_name = "blog/all_topics.html"
    context_object_name = "all_topics"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['allowed_viewer'] = User.objects.get(pk=1)
        data['all_genres'] = Genre.objects.all()
        data['greetings'] = 'Hello user!'
        return data

# def get_all_topics(request):
#     all_topics = Topic.objects.all()
#     allowed_viewer = User.objects.get(pk=1)
#     greetings = [
#         'hello',
#         'welcome',
#         'salam aleikum',
#     ]
#     simple_html_el = "<h1>Zagolovok</h1>"

#     return render(request, 'blog/all_topics.html', {
#         'all_topics': all_topics,
#         'allowed_viewer': allowed_viewer,
#         'greetings': greetings,
#         'aboba': 'ABOBA palindrom is ABOBA',
#         'simple_html_el': simple_html_el,
#         })


def get_topics_by_category(request, category):
    #Electronics
    try:
        asked_category = Category.objects.get(title=category)
        topics_by_category = Topic.objects.filter(category=asked_category)
        return render(request, 'blog/get_topics_by_category.html',
        {'topics_by_category': topics_by_category})
    except: # aboba
        return render(request, 'blog/wrong_category.html')


def test(request):
    author = Author.objects.filter(username='aboba') # -> queryset