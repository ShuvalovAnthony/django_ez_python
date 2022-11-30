from django.urls import path, include
from .views import *

# Blog URLS
urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('all_topics/', TopicListView.as_view(), name='all_topics'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic'),

    # category/<int:pk> - DetailView
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    # category_update/<int:pk>
    # category_delete/<int:pk>

    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author'),
    path('author_create/', AuthorCreateView.as_view(), name='author_create'),
    path('author_update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('author_delete/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),
    
    
    path('topics_by_category/<str:category>/', TopicByCategory.as_view(),
     name='topics_by_category'),


    path('test/', test, name='test'),
]

# '127.0.0.1:8000/blog/all_topics'
