# Generated by Django 2.2 on 2019-04-30 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20190430_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='common.Address', verbose_name='Dirección'),
        ),
    ]