from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.conf import settings

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    Model for blogpost with fields for unique title,author,content,
    created, modified, many categories, draft or published,
    short excerpt, likes
    """
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts") #to assign many categories to many posts
    slug = models.SlugField(max_length=255, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)     # to show short beginning from textfield
    likes = models.ManyToManyField(User, related_name='post_like')
    
    class Meta:
        ordering = ["-created_on"]

    # Automatically save Excerpt automatically
    def save(self, *args, **kwargs):
        if not self.excerpt:
            self.excerpt =self.content[:100]    
        super().save(args, **kwargs)    

    #Count number of likes
    def number_of_likes(self):
        return self.likes.count()    

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    """
    Model for Comments with fields for author,content,
    created, modified, many categories, link to blog post
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=150, related_name="comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ["created_on"]

   
    def __str__(self):
        return f"Comment {self.body} by {self.author.username}"
  
        
class Category(models.Model):
    """
    Model for Categories with fields for category name, description,
    created, updated 
    """
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

