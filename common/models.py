from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
# Create your models here.


class Country(TimeStampedModel):
    name = models.CharField(max_length=128, verbose_name='Nombre')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,  verbose_name='Usuario')

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = 'Países'


class Province(TimeStampedModel):
    name = models.CharField(max_length=128, verbose_name='Nombre')
    country = models.ForeignKey(Country, on_delete=models.PROTECT,  verbose_name='País')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,  verbose_name='Usuario')

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name_plural = 'Provincias'


class City(TimeStampedModel):
    zip_code = models.CharField(max_length=32, verbose_name='Código Postal')
    name = models.CharField(max_length=128, verbose_name='Nombre')
    province = models.ForeignKey(Province, on_delete=models.PROTECT,  verbose_name='Provincia')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,  verbose_name='Usuario')

    def __str__(self):
        return '(%s) - %s' % (self.zip_code, self.name)

    class Meta:
        verbose_name_plural = 'Ciudades'
