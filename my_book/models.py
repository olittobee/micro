from django.db import models 
from tkinter import CASCADE
from cgitb import text
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    body = models.TextField()
    image = models.ImageField(upload_to ='my_book_image',blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField

    def __str__(self):
        return self.title

class Comment(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.body[:50]}...'