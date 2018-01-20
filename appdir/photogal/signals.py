from django.contrib.auth.models import Group

def add_to_regular_group(sender, instance,**kwargs):
    user = instance
    if kwargs["created"]:
        group = Group.objects.get(name='regular')
        user.groups.add(group)