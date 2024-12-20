# Generated by Django 4.2.16 on 2024-11-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_userproject_errors_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255, verbose_name='Project Name')),
                ('project_description', models.TextField(verbose_name='Description')),
                ('error_resolution', models.TextField(blank=True, null=True, verbose_name='Error Resolution')),
                ('uploaded_file', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Uploaded File')),
            ],
        ),
    ]
