# Generated by Django 4.2.16 on 2024-11-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
