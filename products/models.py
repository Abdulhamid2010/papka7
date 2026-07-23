from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=False, default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=False, null=True)
    age = models.PositiveIntegerField(default=18, blank=True)
    bio = models.TextField()
    birth_place = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True)

    REQUIRED_FIELDS = ['email', 'phone_number', 'age']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username