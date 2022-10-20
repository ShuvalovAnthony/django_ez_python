from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4000)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    is_published = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


# Author.objects.all() - все авторы
# Topic.objects.all() - все топики
# Topic.objects.filter(author=???) фильтр по автору
# где ??? - это запрос всех авторов + индекс автора
# Topic.objects.filter(author=    Author.objects.all()[1]     )



