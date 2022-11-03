from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(max_length=1000)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, verbose_name='Автор')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    is_published = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta: 
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True)
    genre = models.ForeignKey('Genre', on_delete = models.CASCADE, blank=True, null=True)
    birthday = models.DateField()
    country = models.ForeignKey('Country', on_delete = models.CASCADE, blank=True, null=True) #если страна больше не поддерживается, удаляем всех авторов, потом хочу переделать


    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.title
