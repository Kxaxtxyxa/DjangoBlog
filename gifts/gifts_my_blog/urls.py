from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("index", views.index, name="index"),
    path("blog", views.blog, name="blog"),
    path("about", views.about, name="about"),
    path("feedback", views.feedback, name="feedback"),
]