from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, upload_to='fotos/profile/%y/%m/%d/')
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
