# Generated by Django 2.2 on 2019-04-30 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_person_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.Address', verbose_name='Dirección'),
        ),
    ]