from django.urls import path, include
from .views import *

# Blog URLS
urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('all_topics/', TopicListView.as_view(), name='all_topics'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author'),
    path('topics_by_category/<str:category>', TopicByCategory.as_view(),
     name='topics_by_category'),
]

# '127.0.0.1:8000/blog/all_topics'
