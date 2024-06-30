from django.contrib.auth.models import  AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    name = models.CharField(_('Name'), max_length=100)
    surname = models.CharField(_('Surname'), max_length=100)
    email = models.EmailField(_('Email Address'), unique=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    username = models.CharField(max_length=150, blank=True, null=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f'{self.name} {self.surname}'

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(_('Profile Image'), upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField(_('Bio'), blank=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return str(self.user)

