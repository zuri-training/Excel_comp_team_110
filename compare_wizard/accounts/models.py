from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_countries.fields import CountryField

GENDER_CHOICES = (
    ('prefer not to say', 'Prefer not to say'),
    ('female', 'Female'),
    ('others', 'Others'),
    ('male', 'Male'),
)
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='prefer not to say')
    country = CountryField(blank_label='(select country)')
    avatar = models.ImageField(null=True, blank= True, default='default.png', upload_to='profile_images')
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 180 or img.width > 180:
            new_img = (180, 180)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    def __str__(self):
        return self.user.username

