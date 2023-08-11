"""cupboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import (
    blog_post_create_view
)
from .views import (
    home_page,
    books_detail_page,
    add_books_page,
    about_page
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('detail/', books_detail_page),
    path('add/', add_books_page),
    path('about/', about_page),
    path('blog/', include("blog.urls")),
    path('blog-create/', blog_post_create_view),


    path("home/v1/", include('blog.urls') )

]
