# Generated by Django 4.1 on 2022-09-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyAPp2', '0012_accounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
