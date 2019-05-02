from django.contrib import admin
from .models import DebtCollector, Member

# Register your models here.
admin.site.register(DebtCollector)
admin.site.register(Member)
