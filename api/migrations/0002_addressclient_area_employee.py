# Generated by Django 3.2.3 on 2022-10-25 17:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(default=datetime.datetime.now)),
                ('charge', models.CharField(max_length=50)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('state', models.IntegerField(choices=[(1, 'Activo'), (0, 'Inactivo')], default=1)),
                ('date_register', models.DateField(default=datetime.datetime.now, editable=False)),
                ('date_modify', models.DateField(default=datetime.datetime.now)),
                ('employee_modify', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee_modify', to='api.employee')),
                ('employee_register', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee_register', to='api.employee')),
            ],
        ),
        migrations.CreateModel(
            name='AddressClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('reference', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('date_register', models.DateField(default=datetime.datetime.now, editable=False)),
                ('date_modify', models.DateField(default=datetime.datetime.now)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.area')),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.client')),
            ],
        ),
    ]