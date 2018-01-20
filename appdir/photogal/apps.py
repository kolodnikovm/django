from django.apps import AppConfig


class PhotogalConfig(AppConfig):
    name = 'photogal'

    def ready(self):
        from .models import User
        from django.db.models.signals import post_save
        from .signals import add_to_regular_group
        post_save.connect(add_to_regular_group, sender=User, weak=False)
