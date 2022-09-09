# Generated by Django 4.1 on 2022-09-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyAPp2', '0007_employee_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('under_name', models.CharField(blank=True, max_length=50, null=True)),
                ('doj', models.CharField(blank=True, max_length=30, null=True)),
                ('salary', models.CharField(blank=True, max_length=50, null=True)),
                ('doresig', models.CharField(blank=True, max_length=50, null=True)),
                ('empno', models.CharField(blank=True, max_length=20, null=True)),
                ('designation', models.CharField(blank=True, max_length=20, null=True)),
                ('function_name', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.CharField(blank=True, max_length=20, null=True)),
                ('bld_grp', models.CharField(blank=True, max_length=20, null=True)),
                ('father_mother', models.CharField(blank=True, max_length=20, null=True)),
                ('spouse', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('phn', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('bank', models.CharField(blank=True, max_length=50, null=True)),
                ('incometax', models.CharField(blank=True, max_length=20, null=True)),
                ('adhar', models.CharField(blank=True, max_length=20, null=True)),
                ('uan', models.CharField(blank=True, max_length=20, null=True)),
                ('pf', models.CharField(blank=True, max_length=20, null=True)),
                ('pr', models.CharField(blank=True, max_length=20, null=True)),
                ('esi', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
