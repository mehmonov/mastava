# Generated by Django 4.2.5 on 2023-10-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
