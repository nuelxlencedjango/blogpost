from django.urls import path
from .views import *
from .import views 
#from .views import (
#    HomeView,
#)


#app_name ="info"


urlpatterns = [
    path('' , PostListView.as_view() ,name="blog-home"),
    path('post/<int:pk>/' , PostDetailView.as_view() ,name="post-detail"),
    path('post/new/' , PostCreateView.as_view() ,name="post-create"),
    path('post/<int:pk>/update/' , PostUpdateView.as_view() ,name="post-update"),
    path('post/<int:pk>/delete/' , PostDeleteView.as_view() ,name="post-delete"),
  
    #path('' , views.home ,name='blog-home'),
  
    path('about/',views.about ,name='blog-about'),
    path('training/',views.about ,name='blog-training'),
    path('registration/',views.about ,name='blog-registration'),
    path('contact/',views.about ,name='blog-contact'),
    path('login/',views.login ,name='blog-login'),
    path('logout/',views.logout ,name='blog-logout')
]
