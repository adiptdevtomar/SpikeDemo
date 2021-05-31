# Generated by Django 3.0.5 on 2021-05-27 08:19

import Products.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('price', models.DecimalField(decimal_places=2, max_digits=80)),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('buyCount', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to=Products.models.get_image_filename, verbose_name='image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.CategoryModel')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
