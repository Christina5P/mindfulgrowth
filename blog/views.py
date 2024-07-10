from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Post, Comment
from django.urls import path, include


# View function to display post in different ways

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }

    return render(request, "blog/index.html", context) # render from right html
    
    

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }

    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/detail.html", context)


def category_search(request):
    query = request.GET.get('q')
    if query:
        categories = Category.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        categories = Category.objects.all()
    
    context = {
        'categories': categories,
        'query': query,
    }
    return render(request, 'blog/category_search.html', context)