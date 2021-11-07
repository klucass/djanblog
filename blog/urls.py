from django.urls import path
from . import views

urlpatterns = [
    path('posts/all', views.all_posts, name='all_posts'),
    path('post/<slug:slug>', views.post, name='post'),
    path('tags/all', views.all_tags, name='all_tags'),
    path('posts/tag/<slug:tag>', views.posts_with_tag, name='posts_with_tag')
]