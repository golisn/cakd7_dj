from curses.ascii import US
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    

    class Meta():
        verbose_name_plural = 'Categories'

    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'



class Post(models.Model):
    title = models.CharField(max_length=20)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    head_image = models.ImageField(upload_to='blog/imges/%Y/%m/%d/', blank = True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank = True)

    # author = models.ForeignKey(User, on_delete=models.CASCADE) 작성자를 지우면 포스트 지우는 코딩
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # 작성자를 지워도 포스트는 남는 코딩

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank=True)

    tags = models.ManyToManyField(Tag, blank=True)

    content = MarkdownxField()

    def __str__(self):
        return f'({self.pk}){self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
    
    def get_content_markdown(self):
        return markdown(self.content)