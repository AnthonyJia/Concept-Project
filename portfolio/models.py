from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)
    bio = models.TextField(max_length=255, blank=True)
    creative_fields = models.ManyToManyField('CreativeField', blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Profile"

class CreativeField(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class PortfolioLink(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.name