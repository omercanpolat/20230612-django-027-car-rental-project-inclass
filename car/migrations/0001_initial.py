# Generated by Django 4.2.2 on 2023-06-13 10:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('plate', models.CharField(max_length=16, unique=True)),
                ('brand', models.CharField(max_length=16)),
                ('model', models.CharField(max_length=16)),
                ('year', models.PositiveSmallIntegerField()),
                ('gear', models.BooleanField(choices=[(1, 'Auto'), (0, 'Manual')], default=0)),
                ('rent_per_day', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(1)])),
                ('availabilty', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
