from blog.models import ContactForm
from rest_framework import serializers


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'