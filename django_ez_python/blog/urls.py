from django.urls import path, include
from .views import TopicListView, get_topics_by_category, blog_home

# Blog URLS
urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('all_topics/', TopicListView.as_view(), name='all_topics'),
    path('topics_by_category/<str:category>', get_topics_by_category,
     name='topics_by_category')
]

# '127.0.0.1:8000/blog/all_topics'
