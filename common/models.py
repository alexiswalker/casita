from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
# Create your models here.


class Country(TimeStampedModel):
    name = models.CharField(max_length=128, verbose_name='Nombre')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario')
