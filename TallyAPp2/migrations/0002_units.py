# Generated by Django 4.1 on 2022-09-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyAPp2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('symbol', models.CharField(blank=True, max_length=20, null=True)),
                ('formal_name', models.CharField(blank=True, max_length=50, null=True)),
                ('uqc', models.CharField(blank=True, max_length=50, null=True)),
                ('decimal', models.IntegerField(blank=True, null=True)),
                ('first_unit', models.CharField(blank=True, max_length=50, null=True)),
                ('conversion', models.CharField(blank=True, max_length=30, null=True)),
                ('second_unit', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
