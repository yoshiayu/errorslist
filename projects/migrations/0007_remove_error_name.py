# Generated by Django 4.2.16 on 2024-11-25 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_error_remove_userproject_error_log_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='error',
            name='name',
        ),
    ]
