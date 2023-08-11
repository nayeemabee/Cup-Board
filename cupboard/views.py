from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404


def home_page(request):
    template_name = "index.html"
    return render(request, template_name)

def books_detail_page(request):
    template_name = "index.html"
    return render(request, template_name)

def add_books_page(request):
    template_name = "index.html"
    return render(request, template_name)

def about_page(request):
    template_name = "index.html"
    return render(request, template_name)

