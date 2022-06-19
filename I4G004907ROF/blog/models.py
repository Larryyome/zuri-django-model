from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=222)
    first_name = models.CharField(max_length=222)
    lastname=models.CharField(max_length=222)
    email= models.EmailField()
    time = models.DateTimeField(auto_now_add=True)
class Post(models.Model):
    Title:models.CharField(max_length=200)
    Text:models.TextField()
    Author:models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date:models.DateField(auto_now_add=True)
    Published_date:models.DateField(auto_now_add=True)
    