# Generated by Django 4.1 on 2022-08-21 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('company', models.CharField(max_length=120)),
                ('cubic_capacity', models.CharField(max_length=120)),
                ('price', models.PositiveIntegerField()),
                ('fuel_capacity', models.CharField(max_length=120)),
                ('mileage', models.CharField(max_length=120)),
            ],
        ),
    ]