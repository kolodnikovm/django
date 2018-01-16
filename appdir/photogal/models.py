from django.db import models
from django.contrib.auth.models import AbstractUser
from .helpers import RandomFileName

class User(AbstractUser):
    pass

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)


    def __str__(self):
        return self.tag_name

class Picture(models.Model):
    picture_name = models.CharField(max_length=20)
    upload = models.ImageField(upload_to=RandomFileName('uploads'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.picture_name
