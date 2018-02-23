from django.db import models
from django.db.models import signals
from django.utils.text import slugify

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=40)
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Channel(models.Model):
    title = models.CharField(unique=True, max_length=191)
    platform = models.CharField(max_length=50, default=None)
    type = models.CharField(max_length=191) # Web, IOS, Android
    slug = models.SlugField(max_length=60, unique=True)
    archived = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


def channel_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)


signals.pre_save.connect(channel_pre_save_receiver, sender=Channel)


