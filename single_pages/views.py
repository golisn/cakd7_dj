from curses import termname
from pyexpat import model
from django.views.generic import ListView
from blog.models import Post
from blog.models import Category
# Create your views here.
class landing(ListView):
    model = Post
    template_name = 'single_pages/landing.html'
    def get_context_data(self, **kwargs):
        context = super(landing, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


class about(ListView):
    model = Post
    template_name = 'single_pages/about_me.html'
    def get_context_data(self, **kwargs):
        context = super(about, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context