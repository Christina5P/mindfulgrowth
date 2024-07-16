from . import views
from django.urls import path
from.views import Post

"""
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('carousel/', views.carousel, name='carousel'),
    path('blog/', views.PostList.as_view(), name='blog_list'),
    path('blog/search/', views.category_search, name='category_search'),
    path('blog/category/<category>/', views.blog_category, name="blog_category"),
    path('blog/post/<int:pk>/', views.blog_detail, name="blog_detail"),
    path('blog/post/<int:pk>/like/', views.post_like, name='post_like'),
    path('blog/post/<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
    path('blog/', views.courses_index, name='courses'),
    path('index/', views.blog_index, name='blog_index'),
]
"""    


urlpatterns = [

    path('', views.PostList.as_view(), name='home'),
    path('carousel/', views.carousel, name='carousel'),
    path('blog/', views.PostList.as_view(), name='blog_list'),
    path('', views.blog_index, name='blog_index'),
    path('search/', views.category_search, name='category_search'),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("post/<int:pk>/", views.blog_detail, name ="blog_detail" ),
    path('post/<int:pk>/like/', views.post_like, name='post_like'),
    path('post/<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
    #path('contact/', views.contact_view, name='contact'),
    #path('<slug:slug>/', views.post, name='post'),
    path('courses/', views.courses_index, name='courses'),
    path('index/', views.blog_index, name='blog'),

    ]    