from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post, Category
# Create your views here.


class inputdata(ListView):
    model = Post
    template_name = 'program/inputdata.html'

    def get_context_data(self, **kwargs):
        context = super(inputdata, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# def inputdata(request):
#     return render (request, 'program/inputdata.html')

class result(ListView):
    model = Post
    template_name = 'program/result.html'

    def get_a_b(self, **kwargs):
        li = []
        li.append(self.request.GET['input_a'])
        li.append(self.request.GET['input_b'])
        pl = 0
        for i in li:
            pl += int(i)
        return pl

    def get_context_data(self, **kwargs):
        context = super(result, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['lic'] = self.get_a_b()

        return context


# def result(request):

    # li = []
    # li.append(request.GET['a'])
    # li.append(request.GET['b'])

    # pl = 0
    # for i in li:
    #     pl += int(i)

    # return render (request, 'program/result.html')