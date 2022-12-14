# Generated by Django 4.1 on 2022-09-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyAPp2', '0020_delete_simple_units'),
    ]

    operations = [
        migrations.CreateModel(
            name='unit_compound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=100)),
                ('f_unit', models.CharField(max_length=100, null=True)),
                ('conversion', models.IntegerField()),
                ('s_unit', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='unit_simple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=100)),
                ('formal_name', models.CharField(max_length=100)),
                ('uqc', models.CharField(max_length=100)),
                ('decimal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='uqcs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uqc_name', models.CharField(max_length=100)),
            ],
        ),
    ]
