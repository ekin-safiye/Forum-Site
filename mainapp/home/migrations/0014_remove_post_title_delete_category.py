# Generated by Django 5.0.1 on 2024-01-31 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_category_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]