# Generated by Django 4.2.16 on 2024-11-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errors', '0003_alter_error_created_at_alter_error_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='error',
            name='name',
            field=models.CharField(max_length=255, verbose_name='名前'),
        ),
        migrations.AlterField(
            model_name='error',
            name='solution',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='error',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
    ]
