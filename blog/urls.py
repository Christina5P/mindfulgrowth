from . import views
from django.urls import path
from.views import post

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #path('<slug:slug>/', views.post, name='post'),
    path("post/<int:pk>/", views.blog_detail, name ="blog_category" ),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path('search/', views.category_search, name='category_search'),
    path('post-like/<int:pk>', views.Post, name="post_like"),
    ]