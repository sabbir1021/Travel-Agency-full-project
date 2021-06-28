from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    picture = models.FileField()
    slide_image = models.FileField()
    def __str__(self):
        return self.name

class Articale(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    duration = models.IntegerField()
    price = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE , related_name="article_countries")
    details = RichTextUploadingField()
    image = models.FileField()
    single_image = models.FileField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=150)
    message = RichTextUploadingField()
    image = models.FileField()

    def __str__(self):
        return self.name

class BlogCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Blog(models.Model):
    categorys = models.ForeignKey(BlogCategory, on_delete=models.CASCADE , related_name="blog_categorys")
    title = models.CharField(max_length=150)
    details = RichTextUploadingField()
    image = models.FileField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    post_comment = models.TextField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.post_comment
    
class Subscribe(models.Model):
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.email

class ArticaleContact(models.Model):
    post = models.ForeignKey(Articale , on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.name


class Review(models.Model):
    post = models.ForeignKey(Articale, on_delete=models.CASCADE , related_name="review_article")
    name = models.CharField(max_length=150)
    mark = models.FloatField()
    comment = models.TextField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.name