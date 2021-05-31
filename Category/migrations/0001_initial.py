# Generated by Django 3.0.5 on 2021-05-27 08:19

import Category.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=500)),
                ('category_logo', models.ImageField(upload_to=Category.models.get_image_filename, verbose_name='image')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
