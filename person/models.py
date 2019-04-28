from django.db import models
from django.conf import settings
from common.models import Address
from model_utils.models import TimeStampedModel


# Create your models here.
class Person(TimeStampedModel):
    first_name = models.CharField(max_length=128, verbose_name='Nombre')
    last_name = models.CharField(max_length=128, verbose_name='Apellido')
    address  = models.OneToOneField(Address, on_delete=models.PROTECT, verbose_name='Dirección')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,  verbose_name='Usuario')

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)

    class Meta:
        verbose_name_plural = 'Personas'
