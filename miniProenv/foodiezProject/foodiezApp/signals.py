from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from .models import User, Profile


@receiver(post_save, sender=User,)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    


