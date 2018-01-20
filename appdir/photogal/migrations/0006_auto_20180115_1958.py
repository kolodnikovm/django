# Generated by Django 2.0 on 2018-01-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0005_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='picture',
            name='tags',
            field=models.ManyToManyField(to='photogal.Tag'),
        ),
    ]
