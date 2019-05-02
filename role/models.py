from django.db import models
from django.conf import settings
from person.models import Person
from model_utils.models import TimeStampedModel

# Create your models here.
class DebtCollector(TimeStampedModel):
    person  = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name='Persona')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,  verbose_name='Usuario')

    def __str__(self):
        return '%s %s' % (self.person.last_name, self.person.first_name)

    class Meta:
        verbose_name_plural = 'Cobradores'

    
class Member(TimeStampedModel):
    person  = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name='Persona')
    debt_collector = models.ForeignKey(DebtCollector, on_delete=models.PROTECT, verbose_name='Cobrador')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,  verbose_name='Usuario')

    def __str__(self):
        return '%s %s' % (self.person.last_name, self.person.first_name)

    class Meta:
        verbose_name_plural = 'Socios'
