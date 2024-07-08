
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path("", include("blog.urls"), name="blog-urls"),
    path( "post/<int:pk>/", views.blog_detail, name ="blog_category" ),
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('summernote/', include('django_summernote.urls')),
    ]