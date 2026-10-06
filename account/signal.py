from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User,Profile

@receiver(post_save, sender=User)
def create_profile_user(sender, instance, created, **kwargs):
    print("SIGNAL CALLED")
    if created:
        Profile.objects.create(user=instance)