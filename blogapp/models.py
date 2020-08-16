from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField()
    date_posted =models.DateTimeField(default=timezone.now)
    author  = models.ForeignKey(User ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title   #, 'by', self.author

    def get_absolute_url(self):
        return reverse('post-detail' ,kwargs={'pk' :self.pk})    

#DATABASE QUEERYSET 
 # from django.db import models
 #from django.contrib.auth.models import User
 # User.objects.all() -to fetch all data 
 # User.objects.first() -first value
 # User.objects.filter(id=id or username="nuel")
 # User.objects.filter(id=id or username="nuel").first () first value from the row
 #User.id ,User.pk
 # use = User.objects.get(id=id) - get the id of the product
 #use.save()

    