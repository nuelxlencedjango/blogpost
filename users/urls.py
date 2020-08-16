from django.urls import path
from .import views 
#from .views import (
#    HomeView,
#)


#app_name ="info"


urlpatterns = [
   
    path('register/',views.register ,name='blog-register'),
    path('profile/',views.profile ,name='blog-profile'),
    #path('login/',views.about ,name='blog-login'),
]
