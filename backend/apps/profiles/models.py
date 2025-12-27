from django.db import models
from django.contrib.auth.models import User

class ProfessionalProfile(models.Model):
    """
    Represents the professional profile shown publicly.
    """

    # Link profile to authenticated user
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    # Professional details
    name = models.CharField(max_length=100)
    email = models.EmailField()

    # Image uploaded to /media/profile_images/
    profile_picture = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True
    )

    address = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    certifications = models.TextField(blank=True)

    def __str__(self):
        return self.name
