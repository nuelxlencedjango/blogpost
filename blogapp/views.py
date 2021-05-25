from django.shortcuts import render ,redirect ,get_object_or_404
from django.views.generic import (
    ListView ,DetailView, CreateView, UpdateView ,DeleteView
)
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from .models import *
# Create your views here.

#
def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request ,'home.html' ,context) 

class PostListView(ListView):
    model = Post # model name
    template_name = 'home.html'  # template name/path
    context_object_name ='posts' # context properties
    ordering =['-date_posted']   # arraned according date posted

    #pagination
    paginate_by =5

   # fetching posts from a particular poster
class UserPostListView(ListView):
    model = Post # model name
    template_name = 'user_posts.html'  # template name/path
    context_object_name ='posts' # context properties
    ordering =['-date_posted']   # arraned according date posted

    #pagination
    paginate_by =5

    # getting queryset from the db
    def get_queryset(self):
        user = get_object_or_404(User ,username =self.kwargs.get('username')) # getting the username ,if not ,return 404
        return Post.objects.filter(author = user).order_by('-date_posted')  # arraned according date posted

class PostDetailView(DetailView):
    model = Post 
    template_name = 'post_detail.html' 
    

# creating a post class
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields =['title' ,'content']
    template_name = 'post_form.html' 

    # creating instance of user to make a post
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_invalid(form)


# creating a post class
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields =['title' ,'content']
    template_name = 'post_form.html' 

    # creating instance of user to make a post
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_invalid(form)


# updating a post class
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    fields =['title' ,'content']
    template_name = 'post_form.html' 

    # creating instance of user to make a post
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_invalid(form)   

        #authenticating the author of the post
        def test_func(self):
            post = self.get_object() # object -current user
            if self.request.user == post.author: # author of the post
                return True
            return False    



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/'
    #template_name = 'post_detail.html' 

    #authenticating the author of the post
    def test_func(self):
        post = self.get_object() # object -current user
        if self.request.user == post.author: # author of the post
            return True
        return False    


def about(request):

    return render(request ,'about.html')  

def login(request):

    return render(request ,'login.html')       


def logout(request):

    return render(request ,'logout.html')    