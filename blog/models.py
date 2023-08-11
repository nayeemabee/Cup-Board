from django.db import models

# Create your models here.

class BlogPost(models.Model):
    # id = models.IntegerField()   #Pk
    student_name = models.CharField(max_length=50)
    books_name = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)


class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    mobile_number= models.CharField(max_length=12)
    address= models.TextField(max_length=250)
    image= models.ImageField(upload_to='contact_images/', null=True, blank=True)



