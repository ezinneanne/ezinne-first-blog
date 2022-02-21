"""Defining URL patterns for The Blog."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    # Page for adding a new blog.
    path('new_blog/',views.new_blog,name='new_blog'),
    # Page for editing a blog.
    path("edit_blog/<int:blog_id>/",views.edit_blog,name="edit_blog"),
]