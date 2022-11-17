from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True) #unique - только индивидульные записи

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})
    

    class Meta:
        verbose_name = 'категория(ю)'
        verbose_name_plural = 'категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tag", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'тэг' # в админке  отображение в ед.числе
        verbose_name_plural = 'тэги' # в админке  отображение в мн.числе
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True) #blank - можно не заполнять
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= 'Опубликовано') #auto_now_add=True - при создание будет выставленна дата
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    views = models.IntegerField(default=0, verbose_name= 'Количество просмотров')
    category = models.ForeignKey(Category, on_delete = models.PROTECT, related_name='posts') #related_name='posts' - название связи
    tags = models.ManyToManyField(Tag, blank =True, related_name='posts')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['-created_at']