from . import views
from django.urls import path
from.views import Post

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('', views.PostList.as_view(), name='home'),
    #path('<slug:slug>/', views.post, name='post'),
    path("post/<int:pk>/", views.blog_detail, name ="blog_detail" ),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path('search/', views.category_search, name='category_search'),
    path('post/<int:pk>/like/', views.post_like, name='post_like'),
    path('post/<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
     path('carousel/', views.carousel, name='carousel'),
    ]