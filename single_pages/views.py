from django.views.generic import ListView
from blog.models import Post, Category

# Create your views here.
class landing(ListView):
    model = Post
    template_name = 'single_pages/landing.html'
    recent_posts = Post.objects.order_by('-pk')[:5]

    def get_context_data(self, **kwargs):
        context = super(landing, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['recent_posts'] = landing.recent_posts
        return context


class about(ListView):
    model = Post
    template_name = 'single_pages/about_me.html'
    def get_context_data(self, **kwargs):
        context = super(about, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# from django.shortcuts import render
# from blog.models import Post

# def landing(request):
#     recent_posts = Post.objects.order_by('-pk')[:3]

#     return render(
#         request,
#         'single_pages/landing.html',
#         {
#             'recent_posts' : recent_posts,
#         }
#     )
    
# def about_me(request):
#     return render(
#         request,
#         'single_pages/about_me.html'
#     )