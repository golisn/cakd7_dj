from curses.ascii import US
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    head_image = models.ImageField(upload_to='blog/imges/%Y/%m/%d/', blank = True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.pk}){self.title} :: {self.author}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'