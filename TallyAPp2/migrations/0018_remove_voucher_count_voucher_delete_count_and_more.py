# Generated by Django 4.1 on 2022-09-09 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TallyAPp2', '0017_payhead'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucher_count',
            name='Voucher',
        ),
        migrations.DeleteModel(
            name='Count',
        ),
        migrations.DeleteModel(
            name='Voucher_count',
        ),
    ]