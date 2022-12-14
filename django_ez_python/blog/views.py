from django.shortcuts import render, redirect
from .models import Author, Category, Topic, Genre
from django.contrib.auth.models import User
from users.models import CustomUser
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import *
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.http import Http404, HttpResponse
from django.urls import reverse
from .utils import generate_password


def test(request):
    input_data = request.POST.get('data')
    if input_data: password = generate_password(input_data)
    else: password = None
    
    return render(
        request,
        'pass/pass_gen.html',
        context={
            'password': password,
            'pass_len': str(input_data),
            })


def test2(request):
    print(request.POST.getlist('checks'))
    return render(
        request,
        'test/test2.html',
        context={
            'hello': 'hello'
            })


class CategoryCreateView(CreateView):
    model = Category
    fields = ['title']
    template_name = 'category/category_form.html'




def blog_home(request):
    return render(request, 'blog/blog_home.html')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author/author_confirm_delete.html'
    success_url = reverse_lazy('blog_home')


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name', 'nickname', 'genre', 'country', 'birthday']
    template_name = 'author/author_form.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/author_form.html'

    def get_success_url(self) -> str:
        return reverse('author_create')
    


class AuthorDetailView(DetailView): # detailView - single object objects.get() 
    model = Author
    template_name = "author/author_detail.html"
    context_object_name = "author"

    def get(self, request, *args, **kwargs):
        self.author_pk = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs) # ???????????? ??????????
        data['topics'] = Topic.objects.filter(author=self.author_pk) # ???? ?????????? topics - ?????????????????? ?????? ???????????? ????????????
        return data


class TopicDetailView(DetailView):
    model = Topic
    template_name = "topic/topic_detail.html"
    context_object_name = "topic"

    def get(self, request, *args, **kwargs):
        print(self)
        return super().get(request, *args, **kwargs)



class TopicListView(ListView): # ListView - objecst.all() objects.filter() - queryset
    model = Topic
    template_name = "blog/all_topics.html"
    context_object_name = "all_topics"

    def get(self, request, *args, **kwargs) -> HttpResponse:
        self.author_id = int(request.GET.get('author_id', '0'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.author_id :
            data['all_topics'] = data['all_topics'].filter(author=self.author_id)
        data['allowed_viewer'] = CustomUser.objects.get(pk=1)
        data['greetings'] = 'Hello user!'
        return data


class TopicByCategory(ListView):
    model = Topic
    template_name = "blog/get_topics_by_category.html"
    context_object_name = "topics_by_category"

    def get(self, request, *args, **kwargs): # blog/topic_byt_category/Python - Python (?????????? url) - ???????????????? ????
        request_category = kwargs['category']  # ???? ???????????? get 
        try:
            self.category_id = Category.objects.get(title=request_category).id
        except:
            raise Http404("Url does not exist") 
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['topics_by_category'] = Topic.objects.filter(category=self.category_id)
        return data


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/register.html'
    success_url =  '/blog'


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'auth/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('blog_home')



def get_topics_by_category(request, category):
    #Electronics
    try:
        asked_category = Category.objects.get(title=category)
        topics_by_category = Topic.objects.filter(category=asked_category)
        return render(request, 'blog/get_topics_by_category.html',
        {'topics_by_category': topics_by_category})
    except: # aboba
        return render(request, 'blog/wrong_category.html')


def logout_view(request):
    logout(request)





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


# def author_profile(request, author_id):
#     try:
#         author = Author.objects.get(pk=author_id)
#         error_msg = ""
#     except:
#         author = None
#         error_msg = "Author doesnt exist"
#     return render(request, 'author/author_detail.html',
#     {
#         'author': author,
#         'error': error_msg,
#         }
#         )