# Generated by Django 4.2.5 on 2023-10-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/books'),
        ),
    ]
