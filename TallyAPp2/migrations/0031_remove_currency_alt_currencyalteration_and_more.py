# Generated by Django 4.1 on 2022-09-17 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TallyAPp2', '0030_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency_alt',
            name='currencyAlteration',
        ),
        migrations.DeleteModel(
            name='currencyAlteration',
        ),
    ]
