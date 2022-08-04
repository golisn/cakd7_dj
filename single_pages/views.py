from curses import termname
from pyexpat import model
from django.views.generic import ListView
from blog.models import Post
# Create your views here.
class landing(ListView):
    model = Post
    template_name = 'single_pages/landing.html'

class about(ListView):
    model = Post
    template_name = 'single_pages/about_me.html'