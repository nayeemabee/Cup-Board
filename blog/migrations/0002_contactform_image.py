# Generated by Django 4.1.5 on 2023-03-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='contact_images/'),
        ),
    ]
