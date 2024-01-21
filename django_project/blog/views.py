from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import(
    LoginRequiredMixin, # Login is compulsory for the class view that is using this parameter
    UserPassesTestMixin # The user has to pass a test function to make changes
)
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib import messages

# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

# Class based views
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # Orders the post from newest to oldest
    # ordering = ['date_posted'] # Orders the post from oldest to newest
    paginate_by = 5 # Two posts per page
    # http://127.0.0.1:8000/?page=5 -> To go to page 5 in our website

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date-posted')
        return super().get_queryset()

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user # Setting the author of the form before running the validation on below line
        return super().form_valid(form) # Running form validation on our parent class

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user # Setting the author of the form before running the validation on below line
        return super().form_valid(form) # Running form validation on our parent class
    
    def test_func(self):
        post = self.get_object() # Gets the post that we are trying to update currently
        if self.request.user == post.author: # if current loggedin user == the author of the post
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    
    def test_func(self):
        post = self.get_object() # Gets the post that we are trying to update currently
        if self.request.user == post.author: # if current loggedin user == the author of the post
            return True
        return False
    
def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})