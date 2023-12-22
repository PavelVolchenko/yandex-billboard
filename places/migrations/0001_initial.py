# Generated by Django 5.0 on 2023-12-22 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description_short', models.CharField(blank=True, max_length=200)),
                ('description_long', models.TextField(blank=True)),
                ('coordinates_lng', models.DecimalField(blank=True, decimal_places=14, max_digits=17)),
                ('coordinates_lat', models.DecimalField(blank=True, decimal_places=14, max_digits=16)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='places.place')),
            ],
        ),
    ]
