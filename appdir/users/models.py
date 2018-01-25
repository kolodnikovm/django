from django.db import models
from django.contrib.auth.models import AbstractUser


class ExternalUser(AbstractUser):
    
    class Meta:
        permissions = (
            ('can_post_pictures', 'To allow to upload photos'),
            ('can_show_pictures', 'To allow to show uploaded photos')
        )
