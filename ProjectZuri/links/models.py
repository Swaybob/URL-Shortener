from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from .utils import generate_random_id
from .managers import ActiveLinkManager


UserModel = get_user_model()

# Create your models here.


class Links(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank=True, unique=True)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    active = models.BooleanField()

    objects = models.Manager()
    public = ActiveLinkManager()

    def save(self, *args, **kwargs):
        self.identifier = slugify(generate_random_id())
        super().save(*args, **kwargs)
