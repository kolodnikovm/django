# Generated by Django 2.0 on 2018-02-24 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0002_picture_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='picture',
            old_name='picture_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag_name',
            new_name='name',
        ),
    ]
