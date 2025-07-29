from django.dispatch import receiver
from .models import User, Profile
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        
        profile.role = "User"
        profile.gender = "Male"
        profile.email = instance.email
        profile.save()
    else:
        print(f"Profile for {instance.username} already exists, no action taken.")