from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from common.models import City

# Create your models here.
class Person(TimeStampedModel):
    first_name = models.CharField(max_length=128, verbose_name='Nombre')
    last_name = models.CharField(max_length=128, verbose_name='Apellido')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,  verbose_name='Usuario')

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)

    class Meta:
        verbose_name_plural = 'Personas'


class Address(TimeStampedModel):
    street_number = models.IntegerField(verbose_name='Número')
    route = models.CharField(max_length=128, verbose_name='Calle')
    unit = models.CharField(max_length=32, verbose_name='Unidad')
    city  = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Ciudad')
    person  = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name='Persona')

    def __str__(self):
        return '%s %s - %s' % (self.route, self.street_number, self.city)

    class Meta:
        verbose_name_plural = 'Direcciones'
