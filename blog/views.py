from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/in_list.html'
class PostDetail(DetailView):
    model = Post
    template_name = 'blog/in_detail.html'

# def index(request):
#     return render(
#         request,
#         'blog/index.html',
#     )