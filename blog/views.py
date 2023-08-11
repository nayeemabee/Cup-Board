from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost, ContactForm
from blog.serializers import ContactFormSerializer
from rest_framework import viewsets


# Create your views here.
# CRUD --> CREATE, RETRIEVE, UPDATE, DELETE

# GET --> RETRIEVE, LIST
# POST --> CREATE, UPDATE, DELETE

def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    context = {"object_list": qs}
    template_name = "index.html"
    return render(request, template_name, context)

def blog_post_create_view(request):
    template_name = "index.html"
    context = {"form": None}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "index.html"
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "index.html"
    context = {"object": obj, "form": None}
    return render(request, template_name, context)

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "index.html"
    context = {"object": obj}
    return render(request, template_name, context)


class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
