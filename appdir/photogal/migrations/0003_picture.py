# Generated by Django 2.0 on 2018-01-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
