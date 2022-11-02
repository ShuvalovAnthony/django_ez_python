from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from blog.views import RegisterUser, LoginUser, logout
from django.contrib.auth.views import LogoutView


# Main URLS
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]


'127.0.0.1:8000/blog/home'



