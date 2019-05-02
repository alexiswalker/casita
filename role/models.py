from django.db import models
from django.conf import settings
from person.models import Person
from model_utils.models import TimeStampedModel

# Create your models here.
class DebtCollector(TimeStampedModel):
    person  = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name='Persona')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,  verbose_name='Usuario')

class Member(TimeStampedModel):
    person  = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name='Persona')
    debt_collector = models.ForeignKey(DebtCollector, on_delete=models.PROTECT, verbose_name='Cobrador')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,  verbose_name='Usuario')
