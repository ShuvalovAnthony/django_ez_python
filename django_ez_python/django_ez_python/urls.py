from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

# Main URLS
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]


'127.0.0.1:8000/blog/home'



