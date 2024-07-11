from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import generic, View
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Category, Post, Comment
from django.urls import path, include
from django.contrib.auth.decorators import login_required

class PostList(generic.ListView):
    """
    A view to list all posts with status 'published'.
    Generic ListView is a standard view
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def blog_index(request):
    """
    Display all blog posts ordered by creation date in descending order.
    Render from index.html
    """
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }

    return render(request, "blog/index.html", context)
    
    
def blog_category(request, category):
    """
    Display blog posts filtered by category name.
    """
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }

    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    """
    Display details of a single blog post and its associated comments and likes
    """
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    number_of_likes = post.likes.count()

    post_is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post_is_liked = True

    context = {
        "post": post,
        "comments": comments,
        "number_of_likes": number_of_likes,
        "post_is_liked": post_is_liked,
    }

    return render(request, "blog/detail.html", context)

def category_search(request):
    """
    Search for categories based on a query string.
    """
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

@login_required
def post_like(request, pk):
    """
    Handle the liking and unliking of a blog post by the user.
    """
    post = get_object_or_404(Post, pk=pk)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))

@login_required
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes.remove(request.user)
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))


