# Generated by Django 4.2 on 2023-10-23 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_booklikes_booklikes_userlike'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='location',
            field=models.CharField(default='Andijon', max_length=100),
            preserve_default=False,
        ),
    ]
