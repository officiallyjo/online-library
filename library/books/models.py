from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author =models.CharField(max_length = 100)
    book = models.FileField(upload_to='pdfs')
    blurb = models.TextField()
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    date = models.DateField(auto_now_add=True, null=True)
    time_posted = models.DateTimeField(auto_now_add=True, null=True)



    def __str__(self):
        return self.title

    
class BookShelf(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"Shelf for {self.user.username}"
