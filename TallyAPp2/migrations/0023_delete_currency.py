# Generated by Django 4.1 on 2022-09-16 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TallyAPp2', '0022_rename_currency_default_currencyalteration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Currency',
        ),
    ]
