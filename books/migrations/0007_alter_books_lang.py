# Generated by Django 4.2 on 2023-10-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_exchange_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='lang',
            field=models.CharField(choices=[('Rus tili', 'ru'), ("O'zbek tili", 'uz'), ('Arab tili', 'ar'), ('Turk tili', 'tr'), ('Ingliz  tili', 'eng')], max_length=100),
        ),
    ]