from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path( "post/<int:pk>/", views.blog_detail, name ="blog_category" ),
    ]