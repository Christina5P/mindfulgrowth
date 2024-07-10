from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# models to store name of category for blogpost 

class Post(models.Model):
    
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    author = models.CharField(max_length=600)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts") #to assign many categories to many posts
    slug = models.SlugField(max_length=255, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)     # to show short beginning from textfield

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
    
    


class Comment(models.Model):
    author = models.CharField(max_length=150)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.author}: {self.body[:50]}..."
    

        
class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

