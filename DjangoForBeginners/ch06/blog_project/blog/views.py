from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
	model = Post
	fields = ['title', 'body']
	template_name = 'post_edit.html'
